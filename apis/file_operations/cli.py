import typer
import uvicorn

def run() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    typer.run(run)
