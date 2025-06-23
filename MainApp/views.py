from django.shortcuts import render, HttpResponse

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]

def home(request):
    text = "<h1>Welcome!</h1>"
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
        html += f"<li>{item['name']}</li>"

    html += "</ol>"
    return HttpResponse(html)