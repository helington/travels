from models import Frete

# Create your views here.


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
        freights_in_month = [Frete.objects.filter(date__month=i)]
        if not freights_in_month:
            freights_per_month[months[i - 1]] = freights_in_month
    return freights_per_month


print(organize_freights())
