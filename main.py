
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize_news', methods=['POST'])
def summarize_news():
    category = request.form['category']
    # Generate the summary using an LLM
    summary = generate_summary(category)
    return render_template('news.html', summary=summary, category=category)

@app.route('/news')
def news():
    category = request.args.get('category')
    if category == 'Financial':
        summary = "Summarized Financial News: [Generated Summary]"
    elif category == 'Politics':
        summary = "Summarized Politics News: [Generated Summary]"
    elif category == 'Sports':
        summary = "Summarized Sports News: [Generated Summary]"
    else:
        return "Invalid category."
    return render_template('news.html', summary=summary, category=category)

def generate_summary(category):
    # Placeholder function to generate a summary using an LLM
    return "[Generated Summary]"

if __name__ == '__main__':
    app.run(debug=True)
