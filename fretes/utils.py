from .models import Frete
from datetime import date

def send_pdf_to_whatsapp(phonenumber):
    pass

def remove_invalid_freights():
    freights = Frete.objects.all()
    today = date.today()
    for freight in freights:
        if freight.date < today:
            freight.delete()


def organize_freights(json=False):
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
    freights_per_month = {} if not json else []
    for i in range(1, 13):
        freights_in_month = Frete.objects.filter(date__month=i)
        if freights_in_month:
            if not json:
                freights_per_month[months[i - 1]] = freights_in_month
            else:
                row = {
                    "month": months[i - 1],
                    "freights": [freight_in_month.serialize() for freight_in_month in freights_in_month]
                }
                freights_per_month.append(row)

    return freights_per_month