from flask import render_template
from app import app
from .request import get_news
from flask import render_template,request,redirect,url_for


@app.route('/')

def index():

  news = get_news()
  return render_template('index.html',articles= news)

# def sources():
  
#   sources = get_sources()
#   return render_template('sources.html', sources= sources)  
 

@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = searched_articles(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',movies = searched_articles)
  



