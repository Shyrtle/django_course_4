from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'url_app/index.html')

def other(request):
    return render(request, 'url_app/other.html')

def relative_url_templates(request):
    return render(request, 'url_app/relative_url_templates.html')
