# Day 3 – Docker & Docker Compose

## What I Learned

- How Docker containers work and how they differ from virtual machines
- Built and ran a custom Docker container using a `Dockerfile`
- Learned the difference between `CMD` and `ENTRYPOINT`
- Used environment variables (`-e VAR=value`) to configure containers
- Passed command line arguments into containers
- YAML, a more readable file format from JSON or XML
- Created a `docker-compose.yml` to run multiple services together
- Learned the basics of YAML syntax

## Docker Projects Completed

- `hello-docker/`: Simple script wrapped in Alpine Linux container
- `hello-env`: Script that prints a name passed via environment variable
- `hello-cli`: Script that prints a name passed via command-line argument
- `compose-lab/`: Multi-container app with Flask + Redis using Docker Compose

## File Breakdown

### `hello-docker/`

- `app.sh`: prints a hello message
- `Dockerfile`: wraps script in a minimal Alpine image

### `compose-lab/`

- `app.py`: Python app that connects to Redis and counts visits
- `Dockerfile`: container for Python + Flask
- `requirements.txt`: Python dependencies
- `docker-compose.yml`: connects `web` and `redis` services

## What I Struggled With

- Understanding `ENTRYPOINT` vs `CMD`
- Why Docker needed `chmod +x`

## GitHub Activity

- All files pushed to `devops-playground/day3/`
