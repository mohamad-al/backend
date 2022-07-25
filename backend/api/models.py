from typing import Any
from django.db import models

from .makejson.makejson import Search as mSearch
from .makejson.makejson import Watch as mWatch
# Create your models here.
class Search(models.Model):
    
    key_word = models.CharField(primary_key=True,max_length= 20)
    
    def __str__(self):
        return self.key_word
    def msearch(self):
        msearch = mSearch(self.key_word)
        return msearch.getresult() 




class Watch(models.Model):
    watchid = models.CharField(primary_key=True,max_length= 20)
    def __str__(self):
        return self.watchid
    def watch(self):
        mwatch = mWatch(self.watchid)
        return mwatch.getresult()
