from rest_framework import viewsets
from .serializers import CompletedQuoteSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
import urbandictionary as ud
import random
import math
from .models import CompletedQuote
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def show():
    
    image_url = "https://picsum.photos/800?grayscale"
    
    rand = ud.random()
    for instance in rand:
        ud_quote = instance.example
        break

    font_family = ["Arial, sans-serif;", 'Helvetica, sans-serif;','Gill Sans, sans-serif;',\
        'Lucida, sans-serif;','Helvetica Narrow, sans-serif;','Times, serif;','Times New Roman, serif;',\
            'Palatino, serif;','Bookman, serif;','New Century Schoolbook, serif;','Andale Mono, monospace;',\
                'Courier New, monospace;','Courier, monospace;','Lucidatypewriter, monospace;','Fixed, monospace;',\
                    'Comic Sans, Comic Sans MS, cursive;','Zapf Chancery, cursive;''Coronetscript, cursive;','Florence, cursive;',\
                        'Parkavenue, cursive;','Impact, fantasy;','Arnoldboecklin, fantasy;',\
                            'Oldtown, fantasy;','Blippo, fantasy;','Brushstroke, fantasy;'
]

    font_weight = ["bold", 'normal']
    font_style = ['normal', 'italic', 'oblique']
    
    def random_item(list):
        x = len(list)
        i = math.floor(random.random())
        i = i*x
        return list[i]
    fam = random_item(font_family)
    weight = random_item(font_weight)
    style = random_item(font_style)

    quotes = CompletedQuote.objects.all()
    quotes.delete()
    newInstance = CompletedQuote(quote = ud_quote, font_family = fam, font_weight = weight, font_style = style, picture_url = image_url)
    newInstance.save()
    

    
    


class QuoteList(APIView):
    
    def get(self, request, format=None):
        show()
        quote = CompletedQuote.objects.all()
        serializer = CompletedQuoteSerializer(quote, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompletedQuote(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
