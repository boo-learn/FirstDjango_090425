from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

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
    context = {
        "items": items
    }
    return render(request, 'items_list.html', context)

def item_detail(request, id):
    for item in items:
        if item['id'] == id:
            context = {
                "item": item
            }
            return render(request, 'item.html', context)
