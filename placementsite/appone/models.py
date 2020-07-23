from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50,default="")
    rollno=models.CharField(max_length=20,default="")
    gpa=models.CharField(max_length=5,default="")
    phn=models.CharField(max_length=12,default="")
    res=models.FileField(upload_to="appone/media",default="")
    
    def __str__(self):
        return self.name
