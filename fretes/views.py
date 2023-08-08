from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Frete

# Create your views here.

def organizeFreights():
    months = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    freightsPerMonth = {}
    for i in range(1, 13):
        freightsInMonth = Frete.objects.filter(date__month=i)
        if len(freightsInMonth) != 0:
            print(len(freightsInMonth))
            freightsPerMonth[months[i - 1]] = freightsInMonth
    return freightsPerMonth

for key, value in organizeFreights().items():
    print(key)
    for freight in value:
        print(value)
    print

def index(request):
    months = organizeFreights
    return render(request, "fretes/index.html", {
        "months": months
    })

def removeFreight(request, freight_id):
    freight = Frete.objects.get(id=freight_id)
    freight.delete()

    return HttpResponseRedirect(reverse("index"))

def editFreight(request, freight_id):
    isEditing = True
    freight = Frete.objects.get(id=freight_id)
    if request.method == "POST":

        title = request.POST["title"]
        date = request.POST["date"]

        freight.title = title
        freight.date = date
        freight.save()

        return HttpResponseRedirect(reverse("index"))
    return render(request, "fretes/addFreightPage.html", {
        "freight": freight,
        "isEditing": isEditing
    })

def addFreight(request):
    isEditing = False
    if request.method == "POST":
        title = request.POST["title"]
        date = request.POST["date"]

        freigth = Frete(title=title, date=date)
        freigth.save()

    return render(request, "fretes/addFreightPage.html", {
        "isEditing": isEditing
    })
