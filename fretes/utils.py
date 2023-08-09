from .models import Frete
from datetime import date

def remove_invalid_freights():
    freights = Frete.objects.all()
    today = date.today()
    for freight in freights:
        if freight.date < today:
            freight.delete()


def organize_freights():
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
    freights_per_month = {}
    for i in range(1, 13):
        freights_in_month = Frete.objects.filter(date__month=i)
        if freights_in_month:
            freights_per_month[months[i - 1]] = freights_in_month
    return freights_per_month