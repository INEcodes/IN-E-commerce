from typing import Type
from django.db import models

class BaseRepository:
    def __init__(self, model: Type[models.Model]):
        self.model = model
        
    def get(self, **kawrgs):
        return self.model.objects.get(**kawrgs)
    
    def filter(self, **kawrgs):
        return self.model.objects.filter(**kawrgs)
    
    def create(self, **kawrgs):
        return self.model.objects.create(**kawrgs)
    
    def update(self, instance, **kawrgs):
        for key, value in kawrgs.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()