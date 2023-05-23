from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from eventapp.forms import *
from django.contrib.auth import login
# Create your views here.

def homeview(request):
    eve=events.objects.all()
    return render(request,"home.html",{'eve':eve})

    
class aboutusview(TemplateView):
    template_name="aboutus.html"
    
class contactview(TemplateView):
    template_name="contact.html"
    
def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/')
    else:
        form=contactform()
    return render(request,"contact.html",{'form':form})
def inserteventrequest(request):
    if request.method=='POST':
        form=eventrequestform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form=eventrequestform()
    return render(request,"home.html",{'form':form})

def insertbooking(request):
    if request.method=='POST':
        form=bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/booking/')
    else:
        form=bookingform()
    return render(request,"booking.html",{'form':form})

def Vendorview(request):
    V=Vendor.objects.all()
    return render(request,"Vendor.html",{'V':V})

def blogview(request):
    blg=blogs.objects.all()
    return render(request,"blog.html",{'blg':blg})

def bookingview(request):
    d=decoration.objects.all()
    e=events.objects.all()
    p=packages.objects.all()
    return render(request,"booking.html",{'d':d,'e':e,'p':p})

def blogdetail(request,id):
    blg=blogs.objects.get(id=id)
    return render(request,"blogdetail.html" ,{'blg':blg})
    
def FAQsview(request):
    F=FAQs.objects.all()
    return render(request,"FAQs.html",{'F':F})

def eventview(request):
    eve=events.objects.all()
    return render(request,"events.html",{'eve':eve})
  

def decorationview(request):
    dec=decoration.objects.all()
    return render(request,"decoration.html",{'dec':dec})


def menuview(request):
    M=menu.objects.all()
    return render(request,"menu.html",{'M':M})


def signupview(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/home/')
            
        
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})
    


def packagesview(request):
    p=packages.objects.all()
    return render(request,"packages.html",{'p':p})


def Vendordetailview(request,id):
    V=Vendordetail.objects.filter(vendorid_id=id)
    return render(request,"Vendordetail.html",{'V':V})

