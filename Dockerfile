# Use Python 3.12 slim image as base
FROM ghcr.io/astral-sh/uv:python3.12-alpine

# Set working directory
WORKDIR /app

# Copy pyproject.toml
COPY pyproject.toml .

# Install dependencies using uv
RUN uv sync

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py

# Run the application
CMD ["uv", "run", "python", "app.py"]
