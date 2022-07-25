
from .serializers import SearchSerializers ,WatchSerializers
from .models import Search, Watch
from rest_framework import viewsets ,status
from rest_framework.response import Response

# Create your views here.
class SearchViewSet(viewsets.ModelViewSet):
    
    
    lookup_url_kwarg = "watchid"
    queryset = Search.objects.all()
    serializer_class =  SearchSerializers


    def list(self, request, *args, **kwargs):
        response = {'message': "You can't search like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 


    def create(self, request, *args, **kwargs):
        response = {'message': "You can't search like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 

    def update(self, request, *args, **kwargs):
        response = {'message': "You can't search like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 

    def destroy(self, request, *args, **kwargs):
        response = {'message': "You can't search like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 

    def retrieve(self, request, *args, **kwargs):
        key_word = self.kwargs.get(self.lookup_url_kwarg)
        print(2)
        Search(key_word=key_word).save()
        return super().retrieve(request, *args, **kwargs)



class WatchViewSet(viewsets.ModelViewSet):
    lookup_url_kwarg = "watchid"
    queryset = Watch.objects.all()
    serializer_class =  WatchSerializers  

    def list(self, request, *args, **kwargs):
        response = {'message': "You can't search like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 


    def create(self, request, *args, **kwargs):
        response = {'message': "You can't search like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 

    def update(self, request, *args, **kwargs):
        response = {'message': "You can't search like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 

    def destroy(self, request, *args, **kwargs):
        response = {'message': "You can't search like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 


    def retrieve(self, request, *args, **kwargs):
        wathid = self.kwargs.get(self.lookup_url_kwarg)
        print(2)
        Watch(watchid=wathid).save()
        return super().retrieve(request, *args, **kwargs)
    
   