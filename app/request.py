from app import app
import urllib.request,json 
from .models import news
from .models import sources

News=news.News
Sources=sources.Sources

api_key = '49750cbf3ad34b9f9e69e796e5b42e8e'
base_url= 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
sources_url= 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'

def get_news():
  get_news_url = base_url.format(api_key)

  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['articles']:
      news_results_list = get_news_response['articles']
      news_results = process_results(news_results_list)
  return news_results

def process_results(news_list):
  news_results = []
  for news_item in news_list:
    author = news_item.get("author")
    title = news_item.get("title")
    description = news_item.get("description")
    url = news_item.get("url")
    urlToImage = news_item.get("urlToImage")
    publishedAt = news_item.get("publishedAt")
    content = news_item.get("content")

    news_object = News(author, title, description, url, urlToImage, publishedAt, content)
    news_results.append(news_object)
  return news_results  
  
  
def get_sources():
  get_sources_url = sources_url.format(api_key)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    sources_results = None

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      news_results = process_results(sources_results_list)
  return sources_results

def process_results(sources_list):
  sources_results = []
  for sources_item in sources_list:
    id = sources_item.get("id")
    name = sources_item.get("name")
    description = sources_item.get("description")
    url = sources_item.get("url")
    category = sources_item.get("category")
    language = sources_item.get("language")
    country = sources_item.get("country")

    sources_object = News(id, name, description, url, category, language, country)
    sources_results.append(sources_object)
  return sources_results  




