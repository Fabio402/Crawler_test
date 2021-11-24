from django.http import JsonResponse
from .utils import Crawler


def search_lenovo(request):
    """
    Faz a busca dos notebooks Lenovo e os ordena de forma crescente em relação ao preço

    Parameters:

    Returns:
        dict: Os notebooks Lenovo em ordem crescente de preço
    """
    crawler = Crawler()
    response = crawler.searching_notebooks()
    lista = [i for i in response if 'lenovo' in i['title']]
    lista = sorted(lista, key=lambda x: x['price'])
    return JsonResponse({'notebooks': lista})
