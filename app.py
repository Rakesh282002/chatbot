"""
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Responses to greetings
greeting_responses = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
greeting_keywords = ["hello", "hi", "hey", "greetings"]

# Responses to questions about tourism
tourism_responses = {
    "What are the best places to visit in the city?": "There are many great places to visit in the city, including the museum, the park, and the historic district.",
    "What is the most popular tourist attraction in the city?": "The most popular tourist attraction in the city is the famous monument located downtown.",
    "What are some good hotels in the city?": "There are many great hotels in the city. Some of the most popular ones include the luxury hotel, the boutique hotel, and the budget hotel.",
    "What is the best time of year to visit the city?": "The best time of year to visit the city is in the spring or fall when the weather is mild and the tourist crowds are smaller."
}

# Responses to questions about famous places
famous_places_responses = {
    "What is the most famous monument in the world?": "The most famous monument in the world is the Eiffel Tower located in Paris, France.",
    "What is the most famous natural wonder in the world?": "The most famous natural wonder in the world is the Grand Canyon located in Arizona, USA.",
    "What is the most famous building in the world?": "The most famous building in the world is the Burj Khalifa located in Dubai, UAE.",
    "What is the most famous theme park in the world?": "The most famous theme park in the world is Disney World located in Orlando, USA."
}

# Function to generate a response to user input
def generate_response(user_input):
    # Check if user input is a greeting
    for word in user_input.split():
        if word.lower() in greeting_keywords:
            return random.choice(greeting_responses)

    # Check if user input is a question about tourism
    for question in tourism_responses:
        if user_input.lower() == question.lower():
            return tourism_responses[question]

    # Check if user input is a question about famous places
    for question in famous_places_responses:
        if user_input.lower() == question.lower():
            return famous_places_responses[question]

    # If no predefined response exists, generate a generic response
    return "I'm sorry, I didn't understand your question."


@app.route("/")
def index():
    return render_template("bot.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg")
    bot_response = generate_response(user_input)
    return str(bot_response)


if __name__ == "__main__":
    app.run(debug=True)
"""


"""
#speech code
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "audio_data" not in request.files:
            return redirect(request.url)

        file = request.files["audio_data"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None) 
    return render_template('speech.html', transcript=transcript)

if __name__ == '__main__':
    app.run(debug=True)

"""



"""
#3rd code useful only 
from flask import Flask, request, render_template
import openai
import os

# Set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "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"

# Initialize the OpenAI API with your API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to ask a question and get the user's response
def ask_question(question):
    response = ""
    while response == "":
        response = request.form.get(question)
    return response
# Create a Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return render_template("home.html")

# Define a route for the chatbot page
@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        # Get the user's input from the form
        place = request.form.get("place")

        # Ask the user a series of questions based on their initial response
        questions = [
            f"What is the main purpose of your trip to {place}?",
            "When do you plan to travel?",
            "How many people are traveling with you?",
            "What is your budget for this trip?",
            "What activities are you interested in?",
            "Do you have any specific dietary requirements?",
        ]

        user_responses = {}
        for question in questions:
            user_responses[question] = ask_question(question)

        # Generate a response based on the user's inputs
        prompt = f"I want to plan a trip to {place}. {user_responses[questions[0]]} I plan to travel in {user_responses[questions[1]]}. There are {user_responses[questions[2]]} people traveling with me. My budget is {user_responses[questions[3]]}. I am interested in {user_responses[questions[4]]}. I have {user_responses[questions[5]]} dietary requirements."
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=50
        )
        text = response.choices[0].text.strip()

        # Render the chatbot page with the final response
        return render_template("chatbot.html", response=text)

    else:
        # Render the chatbot page with the initial question
        return render_template("chatbot.html")

if __name__ == "__main__":
    app.run(debug=True)

"""





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

# Function to generate a response to user input
def generate_response(user_input):
    # Check if user input is a greeting
    for word in user_input.split():
        if word.lower() in greeting_keywords:
            return random.choice(greeting_responses)

    # Check if user input is a question about tourism
    for question in tourism_responses:
        if user_input.lower() == question.lower():
            return tourism_responses[question]

    # Check if user input is a question about famous places
    for question in famous_places_responses:
        if user_input.lower() == question.lower():
            return famous_places_responses[question]

    # If no predefined response exists, generate a generic response
    return "I'm sorry, I didn't understand your question."
# Function to generate a response to user input
"""
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
        engine="davinci", prompt=prompt, max_tokens=200, n=1, stop=None, temperature=0.3
    ).choices[0].text.strip()
    # If no response generated, generate a generic response
    if not response:
        return "I'm sorry, I didn't understand your question."
    #return "I'm sorry, I didn't understand your question."
    return response

if __name__ == "__main__":
    app.run(debug=True)


