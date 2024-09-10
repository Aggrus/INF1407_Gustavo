from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    # processamento antes de mostrar a home page
    hourMinutes = datetime.datetime.now()
    time = {'hora':  hourMinutes.hour, 'minuto': f"{hourMinutes.minute:02d}"}
    return render(request, 'MeuApp/home.html', time)

def segundaPagina(request):
    # processamento antes de mostrar a segunda página
    return render(request, 'MeuApp/segunda.html')