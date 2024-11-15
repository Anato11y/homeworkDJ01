from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Добро пожаловать на главную страницу</h1>")
def data(request):
    return HttpResponse("<h1>Это страница Data</h1>")

def test(request):
    return HttpResponse("<h1>Это страница Test</h1>")
