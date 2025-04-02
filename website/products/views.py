from django.shortcuts import render, get_object_or_404
from core.models import *
from .models import *

def product_watch(request,brand,myid):
    
    if brand.lower() == 'rolex':
        code = rolex_collection.objects.filter(id=myid).values('rolex_code').first()
        code = code['rolex_code']
        watch_obj = get_object_or_404(watch_collection,watch_code__iexact = code)
        
    elif brand.lower() == 'hublot':
        code = hublot_collection.objects.filter(id=myid).values('hublot_code').first()
        code = code['hublot_code']
        watch_obj = get_object_or_404(watch_collection,watch_code__iexact = code)
               
    return render(request,'products/watch_page.html',{'watch':watch_obj,
                                                      'brand_name':brand})
