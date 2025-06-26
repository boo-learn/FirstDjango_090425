from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from MainApp.models import Item


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

def item_create(request):
    if request.method == "GET":
        return render(request, 'create_item.html')

    if request.method == "POST": # Получили данные от формы
        # print(f"FORM DATA:  {request.POST}")
        name = request.POST.get("name")
        brand = request.POST.get("brand")
        count = request.POST.get("count")
        description = request.POST.get("description")

        item = Item(name=name, brand=brand, count=count, description=description)
        item.save()

        return redirect('items-list')
