from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')
def buy_tickets(request):
    return render(request,'buy_tickets.html')
def contact(request):
    return render(request,'contact.html')
def gallery(request):
    return render(request,'gallery.html')
def index(request):
    return render(request,'index.html')
def privacy(request):
    return render(request,'privacy.html')
def schedule(request):
    return render(request,'schedule.html')
def speaker_details(request):
    return render(request,'speaker_details.html')
def speakers(request):
    return render(request,'speakers.html')
def sponsors(request):
    return render(request,'sponsors.html')
def starter_page(request):
    return render(request,'starter_page.html')
def terms(request):
    return render(request,'terms.html')
def tickets(request):
    return render(request,'tickets.html')
def venue(request):
    return render(request,'venue.html')

