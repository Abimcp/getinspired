from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def create_piece(request):
    if request.method == 'GET':
        image_url = "https://picsum.photos/800?grayscale"
        req = requests.get(image_url)
        data = req.json()
        print(data)

        quote_url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

        querystring = {"term":"wat"}

        headers = {
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
            'x-rapidapi-key': "e8b49f6b14msha99db12bcfde212p1af358jsn1c58b79630d0"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        quote_data = response.json()
        print(data)

