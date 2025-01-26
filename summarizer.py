import os
import time
from anthropic import Anthropic
from typing import Optional

class RateLimiter:
    def __init__(self, max_calls=5, period=60):
        self.max_calls = max_calls
        self.period = period
        self.calls = []

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            # Remove old call timestamps
            self.calls = [t for t in self.calls if current_time - t < self.period]
            
            if len(self.calls) >= self.max_calls:
                raise Exception("Rate limit exceeded. Please wait before trying again.")
            
            self.calls.append(current_time)
            return func(*args, **kwargs)
        return wrapper

class ClaudeSummarizer:
    def __init__(self, api_key: Optional[str] = None):
        self.client = Anthropic(api_key=api_key or os.getenv('ANTHROPIC_API_KEY'))

    @RateLimiter()
    def summarize(self, text: str, max_length: int = 300) -> str:
        """
        Summarize input text using Claude API
        
        Args:
            text (str): Text to summarize
            max_length (int): Desired summary length
        
        Returns:
            str: Generated summary
        """
        try:
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=max_length,
                messages=[
                    {
                        "role": "user", 
                        "content": f"Please provide a concise summary of the following text. Keep it under {max_length} tokens:\n\n{text}"
                    }
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating summary: {str(e)}"