from rest_framework import serializers
from .models import CompletedQuote

class CompletedQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedQuote
        fields = ( 'quote', 'font_family', 'font_weight', 'font_style', 'picture_url')