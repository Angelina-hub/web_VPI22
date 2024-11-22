from django.db import models

class Establishment(models.Model):
       name = models.CharField(max_length=255) 
       address = models.CharField(max_length=255)  
       city = models.CharField(max_length=100)  
       phone_number = models.CharField(max_length=20, blank=True)  
       establishment_type = models.CharField(max_length=100) 
       image = models.ImageField()

       def __str__(self):
           return self.name
       

class Feedback(models.Model):
    username = models.CharField(max_length=50)    
    title = models.CharField(max_length=50)    
    feedback = models.CharField(max_length=500)    
    rating = models.IntegerField()

