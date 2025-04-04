import requests
import json
import time

# The advertiser ID that we know has 34 videos
target_id = "AR14017378248766259201"

# Wait for the server to start
time.sleep(2)

# Test with different advertiser names
advertisers = ["Google", "YouTube", "AR14017378248766259201"]

for advertiser_name in advertisers:
    print(f"\nTesting with advertiser: {advertiser_name}")
    
    try:
        response = requests.post(
            "http://localhost:8000/scrape",
            json={"advertiser_name": advertiser_name},
            timeout=120  # Longer timeout for the scraping process
        )
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=2))
            
            # Check if this has videos
            if data.get("has_videos"):
                print(f"✅ {advertiser_name} has {data.get('video_count')} videos!")
            else:
                print(f"❌ {advertiser_name} has no videos")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception occurred: {str(e)}") 