"""
URL configuration for new_event project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from event_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('buy_tickets/',views.buy_tickets,name='buy_tickets'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('index',views.index,name='index'),
    path('privacy/',views.privacy,name='privacy'),
    path('schedule/',views.schedule,name='schedule'),
    path('speaker_details/',views.speaker_details,name='speaker_details'),
    path('speakers/',views.speakers,name='speakers'),
    path('sponsors/',views.sponsors,name='sponsors'),
    path('starter_page/',views.starter_page,name='starter_page'),
    path('terms/',views.terms,name='terms'),
    path('tickets/',views.tickets,name='tickets'),
    path('venue/',views.venue,name='venue'),
]
