import os
from flask import Flask, render_template, request
from google import genai
from google.genai import types

app = Flask(__name__)

# Load Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

# Load your Markdown user guide
with open("sample_user_guide.md", "r", encoding="utf-8") as f:
    user_guide = f.read()

# Simple cache to avoid repeated API calls for the same question
cache = {}

def ask_gemini(question):
    if question in cache:
        return cache[question]
    prompt = (
        "Answer the user's question using ONLY the information from the following Markdown user guide. "
        "If the answer is not present, state that the guide does not contain this information, "
        "and suggest contacting Technical Support or the Community Forum as listed in the Additional Resources section.\n\n"
        f"{user_guide}\n\n"
        f"User question: {question}\n"
        "Answer:"
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=256,
            temperature=0.2
        )
    )
    answer = response.text
    cache[question] = answer
    return answer

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    question = ""
    if request.method == "POST":
        question = request.form.get("question", "")
        if question:
            answer = ask_gemini(question)
    return render_template("askguide.html", answer=answer, question=question)

if __name__ == "__main__":
    app.run(debug=True)
