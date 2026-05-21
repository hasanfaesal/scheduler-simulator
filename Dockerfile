# Use Python 3.11 slim as base
FROM python:3.11-slim

# Prevent Python from writing pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for Tkinter (headless support) and matplotlib
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    libx11-6 \
    libxft2 \
    libxext6 \
    libfontconfig1 \
    libfreetype6 \
    libpng16-16 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Copy requirements first for layer caching
COPY requirements.txt .
RUN uv pip install --system --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Default: run headless simulation (useful for containerized demos)
# Override at runtime with: docker run --cpus="1.0" --memory="512m" scheduler-sim
CMD ["python", "main.py", "--headless"]
