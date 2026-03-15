from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'aligarh'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dec5c220a1484ecad760df171e3f884a'
    PARAMS = {'units':'metric'}


    try:
        data = requests.get(url, PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()

        return render(request, 'index.html', {'description':description, 'icon':icon, 'city':city,  'temp':temp, 'day':day, 'exception_occurred':False})
    except:
        exception_occurred = True
        messages.error(request, 'Entered data is not available to API')
        day = datetime.date.today()

        return render(request, 'index.html', {'description':'clear sky', 'icon':'01d', 'city':'aligarh', 'temp':25, 'day':day, 'exception_occurred':True})

    