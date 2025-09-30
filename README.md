 # News Sentiment Analyzer

A simple web application built with Flask that analyzes the sentiment (positive, negative, or neutral) of a given piece of news text using a pre-trained machine learning model.

## Features

- Simple, clean web interface to input text for analysis.
- Real-time sentiment prediction using a scikit-learn model.
- RESTful API endpoint (`/predict`) for programmatic access.
- Single-page application feel with JavaScript-driven form submission.

## Project Structure

```
.
├── app.py                  # Main Flask application logic and API endpoints
├── sentiment_model.pkl     # Pre-trained sentiment analysis model
├── vectorizer.pkl          # Pre-trained text vectorizer (TF-IDF)
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Frontend HTML, CSS, and JavaScript
```

## Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

- Python 3.8+
- `pip` and `venv`

### 2. Clone the Repository

First, clone the repository to your local machine (or simply download the project files).

### 3. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project-specific dependencies.

```bash
# Navigate to the project directory
cd path/to/finacial-statment

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

With your virtual environment activated, install the required Python packages.

```bash
pip install -r requirements.txt
```

## Running the Application

1.  **Start the Flask development server:**
    ```bash
    python app.py
    ```
2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

You should see the web interface where you can enter news text and click "Analyze Sentiment" to see the result.

## API Usage

You can also interact with the model directly via its API endpoint.

### Endpoint: `/predict`

- **Method:** `POST`
- **Data Format:** `multipart/form-data`

- **Form Field:**
  - `news`: (string) The news text you want to analyze.

#### Example Request (using cURL)

```bash
curl -X POST -F "news=The company announced record-breaking profits and a surge in stock value." http://127.0.0.1:5000/predict
```

#### Success Response (200 OK)

The API will return a JSON object with the original text and the predicted sentiment.

```json
{
  "news": "The company announced record-breaking profits and a surge in stock value.",
  "sentiment": "positive"
}
```

#### Error Response (400 Bad Request)

If the `news` field is missing or empty, the API will return an error.

```json
{
  "error": "No news text provided or text is empty"
}
```
