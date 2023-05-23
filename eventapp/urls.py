from django.urls import path, include
from eventapp import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('home/',views.homeview),
    path('aboutus/',views.aboutusview.as_view()),
    path('booking/',views.bookingview),
    path('insertbooking/',views.insertbooking),
    path('contact/',views.contactview.as_view()),
    path('insertcontact/',views.insertcontact),
    
    
    path('inserteventrequest/',views.inserteventrequest),
    path('blogs/',views.blogview),
    path('Vendor/',views.Vendorview),
    path('blogdetail/<int:id>',views.blogdetail),
    path('Vendordetail/<int:id>',views.Vendordetailview),
    path('FAQs/',views.FAQsview),
    path('events/',views.eventview),
    path('decoration/',views.decorationview),
    path('menu/',views.menuview),
    path('signup/',views.signupview),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('packages/',views.packagesview),
    
]
