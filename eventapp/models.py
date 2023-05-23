from django.db import models
import datetime
from tinymce.models import HTMLField
# Create your models here.

class contact(models.Model):
    firstname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    class Meta:
        db_table="contact"

class booking(models.Model):
   FirstName=models.CharField(max_length=100)
   LastName=models.CharField(max_length=100)
   EventDate=models.CharField(max_length=100)
   ContactNumber=models.CharField(max_length=100)
   NoofGuests=models.CharField(max_length=100)
   Email=models.CharField(max_length=50)
   EventTime=models.CharField(max_length=200)
   venueEventAddress=models.TextField()
   selectevent=models.CharField(max_length=100)
   selectdecoration=models.CharField(max_length=100)
   selectpackages=models.CharField(max_length=100)
   TellusYourNeeds=models.CharField(max_length=100)
   class Meta:
        db_table="booking"

class eventrequest(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    message=models.TextField()
    class Meta:
        db_table="eventrequest"  

class blogs(models.Model):
    title=models.CharField(max_length=100)
    description=HTMLField()
    photo=models.ImageField(upload_to='blog/')
    post_by=models.CharField(max_length=200,default="Admin")
    post_on=models.DateField(default=datetime.date.today())
    class Meta:
        db_table="blogs"
    def __str__(self):
        return self.title
    
class events(models.Model):
    title=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='events/')
    class Meta:
        db_table="events"
    def __str__(self):
        return self.title
        
            
class decoration(models.Model):
    type=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='decoration/')
    price=models.CharField(max_length=100,default="")
    class Meta:
        db_table="decoration"
    def __str__(self):
        return self.type
    
MENUHEAD=(
    ('Drinks','Drinks'),
    ('Starters','Starters'),
    ('Soups','Soups'),
    ('Sandwiches','sandwiches'),
    ('salads','salads'),
    ('chats','chats'),
    ('Rotis','Rotis'),
    ('Rices','Rices'),
    ('Main course','Main course'),
    ('Desserts','Desserts'),
)
class menu(models.Model):
    heading=models.CharField(max_length=100,choices=MENUHEAD)
    items=HTMLField(default="")
    photo=models.ImageField(upload_to='menu/',default="")
    class Meta:
        db_table="menu"
    def __str__(self):
        return self.items
class FAQs(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="FAQs"
    def __str__(self):
        return self.question
class packages(models.Model):
    photo=models.ImageField(upload_to='packages/',default="")
    name=models.CharField(max_length=100)
    
    description=HTMLField()
    startingprice=models.CharField(max_length=100)
    Numberofguest=models.CharField(max_length=100)
    choices=models.CharField(max_length=100,default="")
    class Meta:
        db_table="packages"
    def __str__(self):
        return self.name
    

class Vendor(models.Model):
    title=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='Vendor/',default="")
    
    class Meta:
        db_table="Vendor"
    def __str__(self):
        return self.title   

class Vendordetail(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='packages/',default="")
    location=models.CharField(max_length=100,default="")
    price=models.CharField(max_length=100)
    description=HTMLField()
    vendorid=models.ForeignKey(Vendor,on_delete=models.CASCADE,blank=True,null=True)
    
    class Meta:
        db_table="Vendordetail"
    def __str__(self):
        return self.name
        
MYTAG=(
    ('best','best'),
    ('featured','featured'),
    ('latest','latest'),
    ('new','new'),
)  
    