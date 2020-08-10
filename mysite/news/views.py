from django.shortcuts import render

# Create your views here.
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year':year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, month):
    pass

def article_detail(request):
    pass