from django.shortcuts import render
from . models import * #imports every model
# Create your views here. 
#functions expect request and direct the incoming request to the requested html-file
def shop(request):
    articles = Article.objects.all()
    context = {'articles': articles}                    #context hands over a dictionary for the view to use in the render process to work and "display" it properly on the website in the way it shall "display it"
    return render(request, 'shop/shop.html', context)

def basket(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, done = False)
        articles = order.orderedarticle_set.all()
    else:
        articles = []
        order = []
    context = {'articles':articles, 'order':order}  
    return render(request, 'shop/basket.html',context)

def checkout(request):
    return render(request, 'shop/checkout.html')

def imprint(request):
    return render(request, 'shop/imprint.html')

