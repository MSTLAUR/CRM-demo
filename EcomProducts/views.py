from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import newProductModels
from .form import userProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
import json
from django.core.serializers import serialize

# Create
@login_required
def create_item(request):
    if request.method == 'POST':
        form = userProductForm(request.POST)
        print(request.POST)  # Print all POST data
        print(form.errors)   # Print form validation errors
        if form.is_valid():
            form.save()
            messages.success(request, "Congrats! Keep creating! The world needs more people like you!!!")
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
  




# Read
@login_required
def item_list(request):
    # Get all products
    productList = newProductModels.objects.all()
    
    # Convert products to JSON for Alpine.js
    products_json = serialize('json', productList)
    # Convert serialized data to Python objects
    products_data = json.loads(products_json)
    # Extract just the fields we need
    products_list = [
        {
            'id': item['pk'],
            'name': item['fields']['name'],
            'price': item['fields']['price'],
            'description': item['fields']['description'],
            'video_link': item['fields']['video_link'],
           
          
            # Add other fields you need
            # 'description': item['fields']['description'],
            # 'category': item['fields']['category'],
            # etc...
        }
        for item in products_data
    ]
    # Convert to JSON for template
    products_json_final = json.dumps(products_list)

    context = {
        'productList': productList,  # For regular template use
        'products_json': products_json_final  # For Alpine.js
    }
    
    return render(request, 'ecomproducts/seeAll.html', context)




#What is the instance down bellow? (instance=instance)
# Update
@login_required
def update_item(request, pk):
    item = get_object_or_404(newProductModels, pk=pk)
    if request.method == 'POST':
        form = userProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "🐱‍👤 Modification success 🟢")
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = userProductForm(instance=item)
    return render(request, 'ecomproducts/seeAll.html', {'form': form, 'item': item})


# Delete
@login_required
def delete_item(request, pk):
    item = get_object_or_404(newProductModels, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "☠ You've destroyed what had been and it's now a 👻 ")
        return JsonResponse({'success': True})
    return render(request, 'ecomproducts/seeAll.html', {'item': item})


