from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.


def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーはすでに登録されています'})
    else:
        print(User.objects.all())
    return render(request, 'signup.html', {})
