#!/usr/bin/env python3
"""
Simple script to test if the server is running by calling the /ping endpoint.
"""

import json
import sys
import requests


def test_ping(host="localhost", port=9001):
    """
    Send a request to the /ping endpoint and print the response.
    """
    url = f"http://{host}:{port}/ping"
    print(f"Testing connection to: {url}")
    
    try:
        response = requests.get(url, timeout=5)
        
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Server is running!")
            print("\nResponse data:")
            data = response.json()
            print(json.dumps(data, indent=2))
            return True
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            print(f"Error: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection error: The server is not running or not accessible")
        return False
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test the server's /ping endpoint")
    parser.add_argument("--host", default="localhost", help="Server hostname")
    parser.add_argument("--port", type=int, default=9001, help="Server port")
    
    args = parser.parse_args()
    success = test_ping(args.host, args.port)
    
    sys.exit(0 if success else 1) 