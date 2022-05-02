from flask import render_template
from app import app
from .request import get_news
from .request import get_sources

@app.route('/')

def index():

  news = get_news()
  return render_template('index.html',articles= news)

def sources():

  sources = get_sources()
  return render_template('sources.html', articles= sources)



