# Day 4 - Flask + Redis Counter App (Dockerized)

This is a simple two-container app using Flask and Redis to simulate a microservice setup. It demonstrates how a Python web app can connect to a Redis key-value store, all containerized and orchestrated with Docker Compose.

## Features

- Flask app increments a Redis counter on each visit
- Redis stores hit count
- Run locally with Docker and Docker Compose

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-docker-app.git
   cd python-docker-app
   ```
2. Build and run the services:

   ```
   docker-compose up --build
   ```

3. Visit http://localhost:5000

## What I Learned

- Dockerizing Python apps
- Learning about Redis (it's so fast)
- Using Redis for state
- Managing multi-container apps with Docker Compose
