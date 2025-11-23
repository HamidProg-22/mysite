from django.shortcuts import render

# Create your views here.


# login
def login_view(request):
    return render(request, 'accounts/login.html')

# logout
# def logout_view(request):
#    pass

# signup
def signup_view(request):
    return render(request, 'accounts/signup.html')
