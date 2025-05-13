#!/bin/bash
echo "Starting the Flask + Redis app..."
docker-compose down
docker-compose up --build

