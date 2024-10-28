#!/bin/bash

# Deployment script for the project

# Function to display usage
usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help        Show this help message"
    echo "  -e, --env         Specify the environment (development, production)"
}

# Default environment
ENVIRONMENT="development"

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h|--help) usage; exit 0 ;;
        -e|--env) ENVIRONMENT="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; usage; exit 1 ;;
    esac
    shift
done

echo "Deploying application in $ENVIRONMENT environment..."

# Example deployment steps
if [ "$ENVIRONMENT" == "production" ]; then
    echo "Building production assets..."
    # Add commands to build production assets here
fi

echo "Starting application..."
# Add commands to start the application here
# e.g., python src/main.py

echo "Deployment completed successfully!"
