from django.shortcuts import render, redirect
from .models import Guest
from .forms import GuestForm

# Create your views here.

def index(request):
    form = GuestForm()
    context = {'form': form}
    return render(request, 'guests/index.html', context)

def create(request):
    if request.method=='POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email_address = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            guest = Guest(name=name, email_address=email_address, message=message)
            guest.save()
    return redirect('/list/')

def list(request):
    guests = Guest.objects.all()
    context = {'guest_list': guests}
    return render(request, 'guests/guest_list.html', context)
