from django.db import models

# Create your models here.
class market(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=255,default='',unique=True)
    phone=models.CharField(max_length=11)
    email=models.EmailField(default='',null=True)
    date=models.DateField(auto_now=True)
    visited=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)

    def __str__(self):
        #list1=[self.name ,self.address,self.email,self.phone]
        return self.name #,self.address,self.email,self.phone



class item(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    description =  models.TextField(default='',null=True)
    imageurl = models.ImageField(upload_to='mbt/media/dishes')
    date=models.DateField(auto_now=True)
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    market=models.ForeignKey(market)

    def __str__(self):
        return self.name
