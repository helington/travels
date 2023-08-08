from models import Frete
# Create your views here.

def organizeFreights():
    months = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    freightsPerMonth = {}
    for i in range(1, 13):
        freightsInMonth = [Frete.objects.filter(date__month=i)]
        if not freightsInMonth:
            freightsPerMonth[months[i - 1]] = freightsInMonth
    return freightsPerMonth

print(organizeFreights())