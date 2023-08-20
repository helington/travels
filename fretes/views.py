import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .utils  import organize_freights, remove_invalid_freights
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from django.views.decorators.csrf import csrf_exempt

from .models import Frete

# Create your views here.

remove_invalid_freights()

def index(request):
    return render(request, "fretes/index.html")

@csrf_exempt
def all_freights(request):
    freights = organize_freights()
    return JsonResponse(freights, safe=False)

def freight_by_id(request, freight_id):
    try:
        freight = Frete.objects.get(id=freight_id)
    except Frete.DoesNotExist:
        return JsonResponse({"error": "Freight not found."}, status=404)
    
    if request.method == "GET":
        return JsonResponse(freight.serialize())

    elif request.method == "PUT":
        data = json.loads(request.body)
        title = data.get("title")
        date = date.get("date")
        if title is not None:
            freight.title = title
        if date is not None:
            freight.date = date

        freight.save
        return HttpResponse(status=204)

def new_freight(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    title = data.get("title", "")
    date = data.get("date", "")

    freight = Frete(
        title=title,
        date=date
    )

    freight.save()

    return JsonResponse({"message": "POST registred succesfully."}, status=201)

def generate_pdf(request, content_disposition):
    freights = organize_freights()
    month_names = list(freights.keys())

    response = HttpResponse(content_type="application/pdf")
    response[
        "Content-Disposition"
    ] = f'{"inline" if content_disposition == "view" else "attachment"}; filename="Fretes de {month_names[0]} a {month_names[1]}.pdf"'


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

def freights_by_month(request, freight_month):
    freights = Frete.objects.filter(date__month=freight_month)
    return JsonResponse([freight.serialize() for freight in freights], safe=False)