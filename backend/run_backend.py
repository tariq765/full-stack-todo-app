#!/usr/bin/env python3
"""
Backend API Startup Script

This script starts the FastAPI backend server for the Todo application.
"""

import uvicorn
import os
from pathlib import Path

def main():
    print("[INFO] Starting Todo Backend API...")
    print(f"Loading configuration from: {Path(__file__).parent}")

    # Check if .env file exists
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        print(f"[SUCCESS] Environment file found: {env_file}")
    else:
        print(f"[ERROR] Environment file not found: {env_file}")
        print("Please create a .env file based on .env.example")

    # Start the server
    print("\nStarting server on http://localhost:8000")
    print("Press Ctrl+C to stop the server\n")

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,  # Changed from 3000 to 8000 to avoid conflicts
        reload=True,
        reload_dirs=["src"],
        log_level="info"
    )

if __name__ == "__main__":
    main()