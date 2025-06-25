from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseNotFound
from MainApp.models import Item

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]

def home(request):
    return render(request, "index.html")


def about(request):
    text = "Автор: <strong>Евгений Юрченко</strong>"
    return HttpResponse(text)

def items_list(request):
    items =Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        "item": item
    }
    return render(request, 'item.html', context)
