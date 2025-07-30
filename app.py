from flask import Flask, render_template, jsonify
from datetime import datetime
import openai

app = Flask(__name__)

def generate_prompt(date):
    return f"Give one fun and obscure cricket trivia fact about {date.strftime('%B %d')}."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/trivia', methods=['GET'])
def trivia():
    today = datetime.now()
    trivia_list = []

    for _ in range(5):
        response = openai.Completion.create(
            model="gpt-4",
            prompt=generate_prompt(today),
            max_tokens=100
        )
        trivia_list.append(response.choices[0].text.strip())

    return jsonify({
        "date": today.strftime('%Y-%m-%d'),
        "trivia": trivia_list
    })

if __name__ == '__main__':
    app.run(debug=True)
