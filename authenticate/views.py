from django.shortcuts import render

# Create your views here.
def authenticate(request):
    return render(request, 'authenticate/authenticate.html', {})