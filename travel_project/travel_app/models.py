from django.db import models


class TravelPlace(models.Model):
    name= models.CharField(max_length=255)
    image=models.ImageField(upload_to='places')
    description= models.TextField()

    def __str__(self):
        return self.name
    

class TeamMembers(models.Model):
    member_name= models.CharField(max_length=255)
    member_image=models.ImageField(upload_to='members')
    member_description= models.TextField()

    def __str__(self):
        return self.member_name
    


