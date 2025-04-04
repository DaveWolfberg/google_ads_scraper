#!/usr/bin/env python3
"""
Startup script for Google Ads Transparency Scraper.
This script:
1. Checks if Playwright browsers are installed
2. Starts the FastAPI server
"""

import os
import sys
import subprocess
from install_browsers import install_browsers

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded environment variables from .env file")
except ImportError:
    print("💡 dotenv package not found. Using default environment variables.")


def check_requirements():
    """Check if all requirements are met."""
    try:
        # We're only importing these to check if they're installed
        # pylint: disable=unused-import,import-outside-toplevel
        import fastapi
        import playwright
        import requests
        import bs4
        import pytesseract
        import PIL
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False


def start_server():
    """Start the FastAPI server."""
    # Get configuration from environment or use defaults
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "9001"))
    
    print(f"🚀 Starting FastAPI server on http://{host}:{port}")
    print("Press CTRL+C to stop the server")
    
    # Start uvicorn server
    subprocess.run(
        [
            "uvicorn", 
            "main:app", 
            "--host", host, 
            "--port", str(port),
            "--reload"
        ],
        check=True
    )


def main():
    """Main entry point."""
    print("🔍 Google Ads Transparency Scraper")
    
    # Check if requirements are installed
    if not check_requirements():
        return 1
    
    # Check if Playwright browsers are installed
    try:
        if not install_browsers():
            print("⚠️ Continuing without installing browsers")
    except Exception as e:
        print(f"⚠️ Error checking/installing browsers: {e}")
        print("The application may still work if browsers are already "
              "installed")
    
    try:
        # Start the server
        start_server()
        return 0
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
        return 0
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 