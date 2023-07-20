from django.shortcuts import render

# Create your views here. 
#functions expect request and direct to the requested html-file
def shop(request):
    return render(request, 'shop/shop.html')

def basket(request):
    return render(request, 'shop/basket.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def imprint(request):
    return render(request, 'shop/imprint.html')