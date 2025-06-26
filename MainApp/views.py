from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from MainApp.models import Item, Color


def home(request):
    return render(request, "index.html")


def about(request):
    text = "Автор: <strong>Евгений Юрченко</strong>"
    return HttpResponse(text)

def items_list(request):
    items = Item.objects.all().prefetch_related('colors')
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
        colors = Color.objects.all()
        context = {
            "colors": colors
        }
        return render(request, 'create_item.html', context)

    if request.method == "POST": # Получили данные от формы
        # print(f"FORM DATA:  {request.POST}")
        name = request.POST.get("name")
        brand = request.POST.get("brand")
        count = request.POST.get("count")
        description = request.POST.get("description")
        colors_id = request.POST.getlist('colors')

        item = Item(name=name, brand=brand, count=count, description=description)
        item.save()
        for color_id in colors_id:
            color = Color.objects.get(id=color_id)
            item.colors.add(color)

        return redirect('items-list')
