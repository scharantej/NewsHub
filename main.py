
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
  articles = get_recent_articles()
  return render_template("index.html", articles=articles)

def get_recent_articles():
  url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY"
  response = requests.get(url)
  articles = response.json()["articles"]
  return articles

if __name__ == "__main__":
  app.run()
