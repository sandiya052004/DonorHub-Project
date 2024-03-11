from django.shortcuts import render, redirect
from .models import DonationRequest
from .forms import DonationRequestForm
from django.contrib.auth.models import User, auth
from .models import Organization

def index(request):
    
    return render(request, 'index.html')

def donation_requests(request):
    
    donation_requests = DonationRequest.objects.all()
    return render(request, 'donation_request_list.html', {'donation_requests': donation_requests})

def create_donation_request(request):
    if request.method == 'POST':
        
        form = DonationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_requests')
    else:
        
        form = DonationRequestForm()
    return render(request, 'create_donation_request.html', {'form': form})

def user_profile(request):
    
    return render(request, 'user_profile.html')
def home(request):
    
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
        
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def add_organization(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_information = request.POST.get('contact_information')
        organization_type = request.POST.get('organization_type')
        location = request.POST.get('location')
        
        organization = Organization.objects.create(
            name=name,
            contact_information=contact_information,
            organization_type=organization_type,
            location=location
        )
        organization.save()
        return redirect('home')
    return render(request, 'add_organization.html')


