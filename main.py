from flask import Flask, render_template, request
from sibuddhi import ask_bot
from sibuddhi import get_all_questions
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    all_questions = get_all_questions()
    formatted_questions = [(q[0], q[1], markdown.markdown(q[2], extensions=['extra', 'nl2br'])) for q in all_questions]
    return render_template('index.html', all_questions=formatted_questions)

@app.route("/ask", methods=['POST'])
def ask():
    question = request.form["question"]
    response = ask_bot(question)
    formatted_response = markdown.markdown(response, extensions=['extra', 'nl2br'])

    all_questions = get_all_questions()
    formatted_questions = [(q[0], q[1], markdown.markdown(q[2], extensions=['extra', 'nl2br'])) for q in all_questions]

    return render_template('index.html', question=question, response=formatted_response, all_questions=formatted_questions)

if __name__ == '__main__':
    app.run(debug=True)
