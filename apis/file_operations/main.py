from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()

UPLOAD_DIRECTORY = "./uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_location = os.path.join(UPLOAD_DIRECTORY, filename)
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_location, media_type='application/octet-stream', filename=filename)

@app.delete("/delete/{filename}")
async def delete_file(filename: str):
    file_location = os.path.join(UPLOAD_DIRECTORY, filename)
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail="File not found")
    os.remove(file_location)
    return {"info": f"file '{filename}' deleted"}
