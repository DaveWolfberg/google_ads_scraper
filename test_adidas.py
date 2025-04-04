import requests
import json

# Test specifically for adidas
print("Testing with advertiser: adidas")
    
try:
    response = requests.post(
        "http://localhost:8000/scrape",
        json={"advertiser_name": "adidas"},
        timeout=120  # Longer timeout for the scraping process
    )
    print(f"Response status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2))
        
        # Check if this has videos
        if data.get("has_videos"):
            print(f"✅ adidas has {data.get('video_count')} videos!")
        else:
            print(f"❌ adidas has no videos")
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Exception occurred: {str(e)}") 