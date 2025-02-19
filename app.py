from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of funny jokes
jokes = [
    "Why don't skeletons fight each other? They don't have the guts! 💀",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
    "Parallel lines have so much in common. It’s a shame they’ll never meet! 📏",
    "I told my wife she should embrace her mistakes. She gave me a hug. 🤗",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call cheese that isn’t yours? Nacho cheese! 🧀",
    "Why don’t eggs tell jokes? Because they might crack up! 🥚",
    "What did the grape say when it got stepped on? Nothing, it just let out a little wine! 🍇",
    "I used to be a baker, but I couldn't make enough dough! 🍞",
    "Why did the math book look sad? It had too many problems! 📖"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_joke')
def get_joke():
    joke = random.choice(jokes)
    return jsonify({'joke': joke})

if __name__ == '__main__':
    app.run(debug=True)

