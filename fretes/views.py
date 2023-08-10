from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .utils  import organize_freights, remove_invalid_freights
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from .models import Frete

# Create your views here.

remove_invalid_freights()

def index(request):
    months = organize_freights
    isEmpty = False
    if not months:
        isEmpty = True
    return render(request, "fretes/index.html", {"months": months, "isEmpty": isEmpty})


def generate_pdf(request):
    freights = organize_freights()
    month_names = list(freights.keys())

    response = HttpResponse(content_type="application/pdf")
    response[
        "Content-Disposition"
    ] = f'attachment; filename="Fretes de {month_names[0]} a {month_names[1]}.pdf"'


    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    pdf_content = []
    for month, freights_in_month in freights.items():
        heading = Paragraph(f"<b>{month}</b>", styles["Heading1"])
        pdf_content.append(heading)

        for freight in freights_in_month:
            pdf_content.append(Paragraph(f"<strong>{freight.makeDate()}</strong>: {freight.title}", styles["Normal"]))

        pdf_content.append(Spacer(0, 10))

    doc.build(pdf_content)
    return response


def removef_reight(request, freight_id):
    freight = Frete.objects.get(id=freight_id)
    freight.delete()

    return HttpResponseRedirect(reverse("index"))


def edit_freight(request, freight_id):
    is_editing = True
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
        "fretes/add_freightPage.html",
        {"freight": freight, "is_editing": is_editing},
    )


def add_freight(request):
    is_editing = False
    message = ""
    errorMessage = False
    if request.method == "POST":
        title = request.POST["title"]
        date = request.POST["date"]

        
        if len(Frete.objects.filter(date=date)) > 0:
            message = "Já existe um frete agendado nesta data!"
            errorMessage = True
        else:
            message = "Frete agendado com sucesso!"
            freigth = Frete(title=title, date=date)
            freigth.save()

    return render(request, "fretes/add_freightPage.html", {"is_editing": is_editing, "message": message, "isErrorMessage": errorMessage})


def whatsapp(request):
    return render(request, "fretes/whatsapp_page.html")