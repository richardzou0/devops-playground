# Day 6 – Docker Versioning, CI/CD Review, and Fly.io Deployment

Practiced versioning and redeploying my Dockerized Flask + Redis app to simulate a full CI/CD workflow:

## What I Accomplished

- Copied my Flask app into `day6/flask-v2/` for versioned development
- Built and pushed a versioned Docker image: `flask-redis-app:v2.0`
- Learned how to build for the correct platform (`linux/amd64`) for cloud deployment
- Updated `fly.toml` to pull from Docker Hub instead of rebuilding locally
- Successfully deployed `v2.0` of my app to Fly.io

## Skills Practiced

- Docker image tagging and version control
- Multi-architecture Docker builds with `buildx`
- CI/CD flow refinement with Docker Hub integration
- Troubleshooting deployment architecture issues
- Production deployment using Fly.io

Rebuilding the Docker image for the correct architecture was a useful real-world problem to solve. I also now feel more comfortable managing Docker image versions, and using Fly.io’s deployment process without relying on Fly’s build system.
