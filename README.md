# Ai-text-summarizer
# created an ai text summarizer website using codeium and anthropic
 # Claude Text Summarization App

## Prerequisites
- Python 3.8+
- Anthropic API Key

## Setup Instructions
1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install flask anthropic
   ```
4. Replace `your_anthropic_api_key_here` in `app.py` with your actual Anthropic API key
5. Run the application:
   ```
   python app.py
   ```
6. Open `http://localhost:5000` in your browser

## Features
- Text summarization using Claude API
- Responsive web interface
- Character limit validation
- Client-side and server-side error handling
- Copy to clipboard functionality

## Security Note
This is a development example. For production, use environment variables and implement proper security measures.
