# Google Ads Transparency Scraper

A FastAPI application that scrapes advertiser data from Google Ads Transparency Center.

## Features

- Searches for advertisers by name
- Extracts advertiser ID from Google Ads Transparency Center
- Collects all DOM tags from the advertiser page
- Performs OCR on images found on the page
- Returns structured JSON data

## Prerequisites

- Python 3.8+
- Tesseract OCR installed on your system

### Installing Tesseract OCR

**MacOS:**
```
brew install tesseract
```

**Ubuntu/Debian:**
```
sudo apt-get install tesseract-ocr
```

**Windows:**
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```
   playwright install chromium
   ```

## Running the Application

Start the FastAPI server:
```
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### POST /scrape

Scrapes advertiser data from Google Ads Transparency Center.

**Request Body:**
```json
{
  "advertiser_name": "nike"
}
```

**Response:**
```json
{
  "advertiser_id": "AR14017378248766259201",
  "tags": ["html", "head", "body", "div", "img", ...],
  "image_text": ["advertisement text 1", "advertisement text 2", ...]
}
```

## Error Handling

The API handles errors such as:
- Advertiser not found
- No search results
- Failed OCR processing 