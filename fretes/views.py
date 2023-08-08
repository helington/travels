from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from .models import Frete

# Create your views here.


def organizeFreights():
    months = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]
    freightsPerMonth = {}
    for i in range(1, 13):
        freightsInMonth = Frete.objects.filter(date__month=i)
        if freightsInMonth:
            freightsPerMonth[months[i - 1]] = freightsInMonth
    return freightsPerMonth


def index(request):
    months = organizeFreights
    return render(request, "fretes/index.html", {"months": months})


def generate_pdf(request):
    freights = organizeFreights()
    month_names = list(freights.keys())

    response = HttpResponse(content_type="application/pdf")
    response[
        "Content-Disposition"
    ] = f'attachment; filename="Fretes de {month_names[0]} a {month_names[1]}.pdf"'
    # NOTE: Isso vai quebrar se o banco de dados estiver vazio.
    # O ideal é não mostrar o botão de renderizar o PDF nesse caso.
    # Caso essa função seja chamada mesmo nesse caso, `month_names` vazio ainda precisa ser tratado
    #
    # TODO: Tratar caso de `month_names` vazio
    # TODO: Adicionar datas no arquivo PDF

    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    pdf_content = []
    for month, freights_in_month in freights.items():
        heading = Paragraph(f"<b>{month}</b>", styles["Heading1"])
        pdf_content.append(heading)

        for freight in freights_in_month:
            pdf_content.append(Paragraph(f"• {freight.title}", styles["Normal"]))

        pdf_content.append(Spacer(0, 10))

    doc.build(pdf_content)
    return response


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
    return render(
        request,
        "fretes/addFreightPage.html",
        {"freight": freight, "isEditing": isEditing},
    )


def addFreight(request):
    isEditing = False
    if request.method == "POST":
        title = request.POST["title"]
        date = request.POST["date"]

        freigth = Frete(title=title, date=date)
        freigth.save()

    return render(request, "fretes/addFreightPage.html", {"isEditing": isEditing})
