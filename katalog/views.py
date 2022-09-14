from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog,
        'nama': 'Muhammad Fariz Eda Andhika',
        'npm': '2106653546'
    }
    return render(request, "katalog.html", context)