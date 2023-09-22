from django.shortcuts import render,redirect
from django.http import HttpResponse
from .compare import get_product_data

def home_view(request):
    return render(request,'home.html')

def product_form_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('text')
        if search_query is not None:
            products = get_product_data(search_query)
            return render(request, 'index.html', {'products': products})
        else:
          return redirect("/product_view")
    
    else:
        pass

    return render(request, 'index.html')


# def product_form_view(request):
#     if request.method == 'POST':
        
#         # print(request.POST['text'])
#         search_query=request.POST.get('text')
#         products = get_product_data(search_query)

#         return render(request,'index.html',{'products':products})
#         # return HttpResponse("done")
    
#     else:
        
#         pass

#     return render(request, 'index.html')

