from django.shortcuts import render
<<<<<<< HEAD

def home(request):
    return render(request,'core/home.html')
=======
from .models import *

def home(request):
    product_list = {'headphones' : headphone.objects.all(),
                    'watches' : watch.objects.all(),
                    "clothes" : clothes.objects.all()}
    
    return render(request,'core/home.html',product_list)

def product_watch(request):
    watch_collection_list = {
        "rolex_collection": rolex_collection.objects.all(),
        "hublot_collection": hublot_collection.objects.all(),
    }
    return render(request,'core/product_watch.html',watch_collection_list)

>>>>>>> branch
