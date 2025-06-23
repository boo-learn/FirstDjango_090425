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
    text = """
    <h1>Welcome!</h1>
    <a href='/items'>Список товаров</a>
    """
    return HttpResponse(text)


def about(request):
    text = "Автор: <strong>Евгений Юрченко</strong>"
    return HttpResponse(text)

# result = """
# Список товаров:
# <ul>
#     <li>Кроссовки abibas</li>
#     <li>Куртка кожаная</li>
#     <li>Coca-cola 1 литр</li>
#     <li>Картофель фри</li>
#     <li>Кепка</li>
# </ul>
# """

def items_list(request):
    html = """
    Список товаров:
    <ol>
    """
    for item in items:
        html += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"

    html += "</ol>"
    return HttpResponse(html)


def item_detail(request, id):
    for item in items:
        if item['id'] == id:
            html = f"""
            <h2>{item['name']}</h2>
            Количество: {item['quantity']}
            <a href='/items'>Назад</a>
            """
            return HttpResponse(html)

    return HttpResponseNotFound(f"Товар с id={id} не найден")