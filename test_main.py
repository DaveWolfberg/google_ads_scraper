"""
Tests for the Google Ads Transparency Scraper API.
"""
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

from main import app


class TestScraper(unittest.TestCase):
    """Test cases for the scraper API."""

    def setUp(self):
        """Set up the test client."""
        self.client = TestClient(app)

    @patch("main.get_advertiser_id")
    @patch("main.scrape_advertiser_page")
    @patch("main.extract_text_from_images")
    async def test_scrape_success(
        self, mock_extract_text, mock_scrape_page, mock_get_id
    ):
        """Test the scrape endpoint with a successful response."""
        # Mock the responses
        mock_get_id.return_value = "AR12345678901234567890"
        mock_scrape_page.return_value = (
            ["html", "body", "div"], 
            ["http://example.com/image.jpg"]
        )
        mock_extract_text.return_value = ["example text from image"]

        # Make the request
        response = self.client.post(
            "/scrape", 
            json={"advertiser_name": "nike"}
        )

        # Assert the response
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["advertiser_id"], "AR12345678901234567890")
        self.assertEqual(data["tags"], ["html", "body", "div"])
        self.assertEqual(data["image_text"], ["example text from image"])

    @patch("main.get_advertiser_id")
    async def test_advertiser_not_found(self, mock_get_id):
        """Test the scrape endpoint when advertiser is not found."""
        # Mock the response
        mock_get_id.return_value = None

        # Make the request
        response = self.client.post(
            "/scrape", 
            json={"advertiser_name": "nonexistent_advertiser"}
        )

        # Assert the response
        self.assertEqual(response.status_code, 404)
        self.assertIn("No advertiser found", response.json()["detail"])

    def test_empty_advertiser_name(self):
        """Test the scrape endpoint with an empty advertiser name."""
        # Make the request
        response = self.client.post(
            "/scrape", 
            json={"advertiser_name": "  "}
        )

        # Assert the response
        self.assertEqual(response.status_code, 400)
        self.assertIn("empty", response.json()["detail"])


if __name__ == "__main__":
    unittest.main() 