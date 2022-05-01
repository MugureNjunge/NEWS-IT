from app import app
import urllib.request,json 
from .models import news

News=news.News

api_key = '49750cbf3ad34b9f9e69e796e5b42e8e'
base_url= 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

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


