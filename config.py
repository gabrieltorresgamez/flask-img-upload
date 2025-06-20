import os
from dotenv import load_dotenv

load_dotenv()


class AppConfig:
    S3_ENDPOINT_URL = os.environ.get("S3_ENDPOINT_URL")
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    S3_BUCKET = os.environ.get("S3_BUCKET")
    S3_REGION = os.environ.get("S3_REGION", "us-east-1")  # Default region
    FLASK_DEBUG = bool(int(os.environ.get("FLASK_DEBUG", "0")))
    PORT = int(os.environ.get("PORT", "8080"))

    IMAGE_CATEGORIES = [
        "Label1",
        "Label2",
        "Label3",
        "Label4",
        "Label5",
    ]
