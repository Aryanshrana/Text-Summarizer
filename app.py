from flask import Flask, render_template, request
from summary import summarizer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    original_word_count = None
    summary_word_count = None

    if request.method == 'POST':
        input_text = request.form['input_text']
        summary, _, original_word_count, summary_word_count = summarizer(input_text)

    return render_template('index.html', summary=summary, original_word_count=original_word_count, summary_word_count=summary_word_count)

if __name__ == "__main__":
    app.run(debug=True)
