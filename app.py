from flask import Flask, render_template, request
import openai
import random
app = Flask(__name__)
# Set up OpenAI API key
openai.api_key = "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"

"""
# Responses to greetings
greeting_responses = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
greeting_keywords = ["hello", "hi", "hey", "greetings"]
"""

# Function to generate a response to user input

@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg")
    # Generate response using OpenAI's GPT-3 API
    #prompt = f"What is the answer to the question: {user_input}"
    prompt = f"{user_input}"
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3", prompt=prompt, max_tokens=450, n=1, stop=None, temperature=0.3
    ).choices[0].text.strip()
    # If no response generated, generate a generic response
    if not response:
        return "I'm sorry, I didn't understand your question."
    #return "I'm sorry, I didn't understand your question."
    return response

if __name__ == "__main__":
    app.run(debug=True)


