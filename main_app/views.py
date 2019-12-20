from django.shortcuts import render
from .models import Artist
import requests
import os




# Create your views here.
def show(request):
    artist = request.POST['name_field']
    myKey = os.environ['SECRET_KEY']
    appKey = os.environ['APP_ID']
    req = requests.get(f"http://rest.bandsintown.com/artists/{artist}?app_id={appKey}")
    print('----------------<(^_^)>-----------------------')    
    req = req.json()
    print (req['name'])
    print('----------------<(^_^)>-----------------------')
    return render(request, 'artists/index.html')


def home(request):
    print(request)
    myKey = os.environ['SECRET_KEY']
    appKey = os.environ['APP_ID']
    req = requests.get(f"http://eventful.com/json/events?q=music&l=TX&t=December+2019app_id=gssq2hLc4npkxj69")
    print(req)
    print('----------------<(^_^)>-----------------------')    
    req = req.json()
    print('----------------<(^_^)>-----------------------')
    print(req)
    return render(request, 'index.html')
    # make request to eventul api



def about(request):
    return render(request, 'about.html')

def artists_index(request):
    artists = Artist.objects.all()
    return render(request, 'artists/index.html', { 'artists': artists })