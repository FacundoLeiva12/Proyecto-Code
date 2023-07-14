from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')

def primera(request):
    
    return render(request, 'primera.html')


def segunda(request):
    
    return render(request, 'segunda.html')   