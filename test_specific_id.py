import asyncio
import logging
from main import check_advertiser_videos

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

async def test_video_detection():
    """Test video detection for a specific advertiser ID"""
    advertiser_id = "AR14017378248766259201"  # The specific ID from the example
    
    print(f"Testing video detection for advertiser ID: {advertiser_id}")
    has_videos, video_count = await check_advertiser_videos(advertiser_id)
    
    print(f"Results:")
    print(f"  - Has videos: {has_videos}")
    print(f"  - Video count: {video_count}")

if __name__ == "__main__":
    asyncio.run(test_video_detection()) 