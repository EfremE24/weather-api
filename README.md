# Tiny Flask Weather API

## 1) Executive Summary

Problem: Sometimes you need a quick way to describe what the weather is like based on a temperature number, without using a full weather service or large API.

Solution: This project provides a tiny Flask API that takes a temperature value and returns a simple text message describing the weather. It is lightweight, easy to run, and fully containerized using Docker to ensure consistent behavior on any machine.

## 2) System Overview

Course Concept(s): Flask REST API, Docker containerization, reproducible environments.

### Architecture Diagram
Client (curl or browser) --> Flask Weather API --> Temperature Classification Logic

### Data/Models/Services
- No database used.
- Input: temperature via query parameter.
- Output: JSON with temperature and a weather message.
- No external datasets or persistent storage.

## 3) How to Run (Local)

### One-Command Run

This project includes a run.sh script that allows the entire application to be started with a single command. The script automatically builds the Docker image and then starts the container.

After cloning the repository and navigating into the project directory, run:

./run.sh

What this script does:

-Builds the Docker image (weather-api:latest)

-Starts the container on port 8080

-Launches the Flask API inside Docker

-Makes the API available at: http://localhost:8080

Once the script is running, open a new terminal tab and do not close the one running run.sh. Test the API using curl
### Health Check
curl http://localhost:8080/health

### Weather Endpoint Examples
curl "http://localhost:8080/weather?temp=72"

curl "http://localhost:8080/weather?temp=-5"

curl "http://localhost:8080/weather?temp=95"
These commands will return messages describing weather conditionsfor the tempeartures you input.
## 4) Design Decisions

- The project intentionally uses no database to remain minimal, stateless, and easy to containerize.
- Temperature ranges were chosen to clearly separate categories.
- The API includes error handling for missing temperature values or invalid numeric input.
- No personal data is collected. The API is containerized for isolation and includes a /health endpoint for basic health monitoring.

## 5) Results and Evaluation

- The API was tested using curl with a variety of temperatures.
- Tests covered all temperature categories including freezing, cold, nice, pretty hot, hot, and dangerously hot.
- Screenshots showing terminal output are stored in the /assets folder.
- The application starts quickly, performs consistently, and produces correct JSON responses.

## 6) What’s Next

- Add support for Celsius input and automatic conversion.
- Add a larger set of descriptive categories.
- Add optional emojis for improved user experience.

## 7) Links (Required)

GitHub Repository: https://github.com/EfremE24/weather-api

