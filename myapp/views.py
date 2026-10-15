from django.shortcuts import render
import requests
from datetime import datetime, timedelta
from newsproj.settings import NEWS_API_KEY

# Create your views here.
def index_view(request):
    from_date=(datetime.now() - timedelta(days=1))
    
    print(from_date.strftime('%Y-%m-%d'))
    
    request_url=f"https://newsapi.org/v2/everything?q=delhi&from={from_date.strftime('%Y-%m-%d')}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    news_data=requests.get(request_url).json()
    
    baja={
        'raja':news_data.get("articles")
    }
    
    return render(request,'pages/index.html',baja)


def search_menu(request):
    
    if request.method=='POST':
        query=request.POST.get("query")
        
        from_date=(datetime.now() - timedelta(days=1))
        
        
        request_url=f"https://newsapi.org/v2/everything?q={query}&from={from_date.strftime('%Y-%m-%d')}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
        news_data=requests.get(request_url).json()
    
    
        baja={
        'raja':news_data.get("articles")
    }
    
    return render(request,'pages/index.html',baja)

    # return redirect('index_page')