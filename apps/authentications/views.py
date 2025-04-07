from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('announcement-list')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {
            'username': username  # to persist username in form
        }

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('announcement-list')
            else:
                context['error'] = "Invalid username or password."
                return render(request, 'login.html', context)
        except Exception as e:
            context['error'] = "An error occurred during login. Please try again."
            return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
