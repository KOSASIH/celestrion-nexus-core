#!/bin/bash

# Environment setup script

# Function to display usage
usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help        Show this help message"
    echo "  -r, --requirements Specify the requirements file (default: requirements.txt)"
}

# Default requirements file
REQUIREMENTS_FILE="requirements.txt"

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h|--help) usage; exit 0 ;;
        -r|--requirements) REQUIREMENTS_FILE="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; usage; exit 1 ;;
    esac
    shift
done

echo "Setting up the environment..."

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing dependencies from $REQUIREMENTS_FILE..."
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "Requirements file not found: $REQUIREMENTS_FILE"
    exit 1
fi

echo "Environment setup completed successfully!"
