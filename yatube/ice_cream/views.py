from django.http import HttpResponse


# Главная страница
def index(request):
    html_content = '<html><head><title>Анфиса для друзей</title></head><body>'
    html_content += '<h1>Главная страница</h1>'
    html_content += '</body></html>'    
    return HttpResponse(html_content) 


def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')