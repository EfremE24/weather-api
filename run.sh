#!/bin/bash
set -e

IMAGE_NAME="weather-api:latest"

echo "Building Docker image..."
docker build -t "$IMAGE_NAME" .

echo "Running container on http://localhost:8080 ..."
docker run --rm -p 8080:8080 "$IMAGE_NAME"

