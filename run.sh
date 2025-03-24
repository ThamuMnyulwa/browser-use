#!/bin/bash

# Create and activate virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install playwright browsers
playwright install

# Run the Python script
python examples/agent_browsing.py 