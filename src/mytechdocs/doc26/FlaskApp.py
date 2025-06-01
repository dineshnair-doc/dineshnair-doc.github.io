from flask import Flask, request, render_template, redirect, url_for
from google import genai
import os

app = Flask(__name__)

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set!")

# Initialize client with explicit API key
client = genai.Client(api_key=GOOGLE_API_KEY)

chat_history = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    global chat_history
    if request.method == 'POST':
        user_input = request.form['message']
        prompt = f"{user_input}. Please answer in two sentences or less."

        try:
            # Note: As per the latest google-genai, you might need to use .models.generate_content()
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite",
                contents=prompt
            )
            # Check how to access the actual text from response; might vary!
            # If response.text is not available, try response.candidates[0].content.parts[0].text
            ai_answer = getattr(response, 'text', None)
            if ai_answer is None:
                try:
                    ai_answer = response.candidates[0].content.parts[0].text
                except (AttributeError, IndexError):
                    ai_answer = "Error: Could not parse Gemini response."
        except Exception as e:
            ai_answer = f"Error: Could not get a response from Gemini AI. Please try again. ({e})"
            print(f"Gemini API error: {e}")

        chat_history.append({
            'question': user_input,
            'answer': ai_answer
        })
    return render_template('index.html', history=chat_history)

@app.route('/clear')
def clear_chat():
    global chat_history
    chat_history = []
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(debug=True)
