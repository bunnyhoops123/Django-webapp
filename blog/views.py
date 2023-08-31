from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Sumukh Varma',
        'title': 'Blog Post 1',
        'content': 'First post created',
        'date_posted': 'August 29, 2023',
    },
     {
        'author':'Sacchi Varma',
        'title': 'Blog Post 2',
        'content': 'Second post created',
        'date_posted': 'August 31, 2023',
    }
]



# Create your views here.
def blog(request):  
    context = {
        'posts':posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
