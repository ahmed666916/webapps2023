from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        # Handle the form submission and registration logic here
        # Retrieve the form data using request.POST
        # Perform validation, create a new user, etc.
        # Redirect the user to a success page or perform any other desired action

        # Example: 
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        currency = request.POST.get('currency')

        # Perform your registration logic here

        return render(request, 'registration_success.html')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        # Handle the form submission and login logic here
        # Retrieve the form data using request.POST
        # Perform validation, authenticate the user, etc.
        # Redirect the user to a dashboard or perform any other desired action

        # Example:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform your login logic here

        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

