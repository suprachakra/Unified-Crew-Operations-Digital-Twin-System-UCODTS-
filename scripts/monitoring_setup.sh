#!/bin/bash
# monitoring_setup.sh
# Script to initialize Prometheus and Grafana for UCODTS monitoring

echo "Starting monitoring setup..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi

# Start Prometheus container
echo "Starting Prometheus..."
docker run -d --name prometheus -p 9090:9090 -v $(pwd)/../infrastructure/monitoring/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus

# Start Grafana container
echo "Starting Grafana..."
docker run -d --name grafana -p 3000:3000 grafana/grafana

echo "Monitoring systems started successfully."
