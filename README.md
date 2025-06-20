# Flask S3 Image Uploader

A simple Flask web application that allows users to upload images to an S3-compatible storage service with categorization.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/gabrieltorresgamez/flask-img-upload.git
cd flask-img-upload
```

### 2. Configure Environment Variables

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Edit the `.env` file with your S3 credentials:

```
S3_ENDPOINT_URL=https://your-s3-endpoint.com
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
S3_BUCKET=your-bucket-name
S3_REGION=your-region
PORT=8080
FLASK_DEBUG=1
```

### 3. Customize Image Categories

Edit the `IMAGE_CATEGORIES` list in `config.py` to customize the categories shown in the dropdown menu:

```python
IMAGE_CATEGORIES = [
    "Label1",
    "Label2",
    "Label3",
    # Add more categories as needed
]
```

## Running the Application

### Using Docker Compose (Recommended)

The easiest way to run the application is with Docker Compose:

```bash
docker compose up --build
```

This will:
1. Build the Docker image
2. Start the container
3. Make the application available at http://localhost:8080

### Running Directly with Python

If you prefer to run the application directly:

1. Install uv using the [installation guide](https://docs.astral.sh/uv/getting-started/installation/).

2. Create a virtual environment and install dependencies:

```bash
uv sync
```

3. Run the application:

```bash
uv run python app.py
```

The application will be available at http://localhost:8080 (or the port specified in your `.env` file).
