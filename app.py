import os
from flask import Flask, render_template, request, jsonify, flash
from summarizer import ClaudeSummarizer

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure secret key for flash messages

# Initialize summarizer (replace with your actual API key)
summarizer = ClaudeSummarizer(api_key="your_anthropic_api_key_here")

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Get text from request
        text = request.form.get('text', '').strip()
        
        # Validate input
        if not text:
            return jsonify({
                'error': True, 
                'message': 'Please provide some text to summarize.'
            }), 400
        
        if len(text) > 5000:  # Prevent excessive input
            return jsonify({
                'error': True, 
                'message': 'Text is too long. Maximum 5000 characters allowed.'
            }), 400
        
        # Generate summary
        summary = summarizer.summarize(text)
        
        return jsonify({
            'error': False, 
            'summary': summary
        })
    
    except Exception as e:
        return jsonify({
            'error': True, 
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)