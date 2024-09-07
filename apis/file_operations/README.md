# FastAPI File Management

This project provides a simple FastAPI application for file upload, download, and deletion.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Typer

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required packages:
   ```
   pip install fastapi uvicorn typer
   ```

## Usage

1. Start the server:
   ```
   python cli.py
   ```

2. The server will be running at `http://0.0.0.0:8000`.

## API Endpoints

### Upload File

- **URL**: `/upload/`
- **Method**: `POST`
- **Description**: Upload a file.
- **Request**: `multipart/form-data`
  - `file`: The file to upload.
- **Response**: JSON with file information.

### Download File

- **URL**: `/download/{filename}`
- **Method**: `GET`
- **Description**: Download a file.
- **Response**: The requested file.

### Delete File

- **URL**: `/delete/{filename}`
- **Method**: `DELETE`
- **Description**: Delete a file.
- **Response**: JSON with deletion information.

## Notes

- Uploaded files are stored in the `./uploaded_files` directory.
- Ensure the `uploaded_files` directory exists or will be created by the application.

## License

This project is licensed under the MIT License.
