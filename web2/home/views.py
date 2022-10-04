from django.shortcuts import render
from django.http import HttpResponse

# viet ham xu ly gui response den may user
def index(request):
    return render(request, 'pages/home.html') #ham index vao home.html
def solutions(request):
    return render(request, 'pages/solutions.html') 
def partner(request):
    return render(request, 'pages/partner.html')     
def about(request):
    return render(request, 'pages/about.html') 
def contact(request):
    return render(request, 'pages/contact.html')  
def news(request):
    return render(request, 'pages/news.html')    
def product(request):
    return render(request, 'pages/product.html')  
   