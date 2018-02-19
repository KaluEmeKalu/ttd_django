from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):
	return render(request, 'lists/home.html')

def view_list(request):
	items = Item.objects.all()
	return render(request, 'lists/list.html', {'items': items})

def new_list(request):
	list_ = List.objects.create()
	text = request.POST['item_text']
	Item.objects.create(text=text, list=list_)
	return redirect('lists:view_list')