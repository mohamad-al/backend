from rest_framework import serializers
from .models import Search ,Watch

class SearchSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Search
        fields = ('key_word','msearch') 

class WatchSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Watch
        
        fields = ('watchid','watch') 