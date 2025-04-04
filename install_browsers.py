#!/usr/bin/env python3
"""
Helper script to install Playwright browsers.
Run this script after installing the dependencies and before starting the app.
"""

import subprocess
import sys


def install_browsers():
    print("Installing Playwright browsers...")
    try:
        subprocess.run(
            ["playwright", "install", "chromium"], 
            check=True, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Successfully installed Chromium browser for Playwright")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing Playwright browsers: {e}")
        print(f"Error output: {e.stderr.decode('utf-8')}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = install_browsers()
    sys.exit(0 if success else 1) 