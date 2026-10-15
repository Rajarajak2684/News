from django.shortcuts import render
import requests
from datetime import datetime, timedelta

# Create your views here.
def index_view(request):
    from_date=(datetime.now() - timedelta(days=1))
    
    print(from_date.strftime('%Y-%m-%d'))
    
    request_url=f"https://newsapi.org/v2/everything?q=delhi&from={from_date.strftime('%Y-%m-%d')}&sortBy=publishedAt&apiKey=5185ffd4aad846d798b1187a1713eb6b"
    news_data=requests.get(request_url).json()
    
    baja={
        'raja':news_data.get("articles")
    }
    
    return render(request,'pages/index.html',baja)


def search_menu(request):
    
    if request.method=='POST':
        query=request.POST.get("query")
        
        from_date=(datetime.now() - timedelta(days=1))
        
        
        request_url=f"https://newsapi.org/v2/everything?q={query}&from={from_date.strftime('%Y-%m-%d')}&sortBy=publishedAt&apiKey=5185ffd4aad846d798b1187a1713eb6b"
        news_data=requests.get(request_url).json()
    
    
        baja={
        'raja':news_data.get("articles")
    }
    
    return render(request,'pages/index.html',baja)

    # return redirect('index_page')