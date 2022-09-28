from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'list_film' : data_watchlist,
        'nama': 'Muhammad Fariz Eda Andhika',
        'npm': '2106653546',
        'message' : extra(),
    }

    return render(request, "mywatchlist.html", context)

def extra():
    daftar_watchlist = MyWatchList.objects.all().values("watched")
    # Initial values
    jumlah_yes = 0
    jumlah_no = 0
    for i in daftar_watchlist:
        if i['watched'] == 'Yes':
            jumlah_yes += 1
        else:
            jumlah_no += 1
    
    if jumlah_no >= jumlah_yes:
        return "Wah, kamu masih sedikit menonton!"
    return "Selamat, kamu sudah banyak menonton!"


def show_type(request, type):
    data = MyWatchList.objects.all()
    if(type == 'xml'):
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    else:
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")