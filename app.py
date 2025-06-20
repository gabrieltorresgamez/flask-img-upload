from flask import Flask, request, render_template
import os
import boto3
from botocore.config import Config
from datetime import datetime
from urllib.parse import quote_plus
from config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)
s3 = boto3.client(
    "s3",
    endpoint_url=app.config["S3_ENDPOINT_URL"],
    aws_access_key_id=app.config["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=app.config["AWS_SECRET_ACCESS_KEY"],
    region_name=app.config["S3_REGION"],
    config=Config(signature_version="s3v4"),
)


@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        image = request.files["image"]
        category = request.form["category"]

        if image:
            # Sanitize category string to be safe for filenames
            category_safe = "".join(
                c if c.isalnum() or c in (" ", ".", "_") else "_" for c in category
            )
            # Truncate to prevent excessively long filenames
            category_safe = category_safe[:50]

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_extension = os.path.splitext(image.filename)[1]
            # URL-encode the filename for S3 compatibility (e.g., spaces become '+')
            base_filename = quote_plus(f"{timestamp}_{category_safe}{file_extension}")

            # Define S3 object key, placing files in an 'images' virtual folder
            s3_key = f"images/{base_filename}"

            try:
                s3.upload_fileobj(
                    image,
                    app.config["S3_BUCKET"],
                    s3_key,
                )
                image_url = (
                    f"{app.config['S3_ENDPOINT_URL']}/"
                    f"{app.config['S3_BUCKET']}/{s3_key}"
                )
                print(f"Image uploaded to: {image_url}")
                return render_template(
                    "success.html",
                    redirect_url="/",  # URL to redirect to (our main upload page)
                    delay_seconds=3,  # Seconds before redirection
                )

            except Exception as e:
                return f"An error occurred: {e}"

    # Pass categories list to the HTML template for dropdown population
    return render_template("upload.html", categories=app.config["IMAGE_CATEGORIES"])


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=app.config["PORT"],
        debug=app.config["FLASK_DEBUG"],
    )
