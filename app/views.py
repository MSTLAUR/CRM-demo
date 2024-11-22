from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from EcomProducts.models import Item
from django.template import loader
from EcomProducts.form import ItemForm




def home_page_view(request, *args, **kwargs):
  item_list = Item.objects.all()

  context ={
        'item_list':item_list,
}
  return render(request,'EcomProducts/index.html',context)

def single(request, item_id):
    item = Item.objects.get(pk=item_id)  # Safer to use get_object_or_404
    context = {
    'item': item,
}
    return render(request, 'EcomProducts/single.html', context)


def form_submit(request):
  form = ItemForm(request.POST or None)

  if form.is_valid():
    form.save()
  return redirect('home')

  return render(request,'EcomProducts/form.html', {'form':form})






def checkout(request, *args, **kwargs):
  item_list = Item.objects.all()

  context ={
        'item_list':item_list,
}
  return render(request,'EcomProducts/checkout.html',context)







