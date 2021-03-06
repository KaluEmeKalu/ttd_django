from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):
	return render(request, 'lists/home.html')

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	context = {'list': list_}
	return render(request, 'lists/list.html', context)

def new_list(request):
	list_ = List.objects.create()
	text = request.POST['item_text']
	Item.objects.create(text=text, list=list_)
	return redirect('/lists/{}/'.format(list_.id))


def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	text=request.POST['item_text']
	Item.objects.create(
		text=text,
		list=list_
	)
	return redirect('/lists/{}/'.format(list_.id))