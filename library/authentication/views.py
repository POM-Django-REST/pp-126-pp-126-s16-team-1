from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from authentication.models import CustomUser
from django.urls import reverse

def get_current_user(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None
    return None

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        role = request.POST.get('role')  # expected value: 'librarian' or 'visitor'
        # Map role string to integer (librarian=1, visitor=0)
        role_int = 1 if role == 'librarian' else 0
        
        # Check if the email is already registered.
        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse("Email already registered.")
        # Create a new user using the manager so that the password is hashed.
        CustomUser.objects.create_user(email=email, password=password,
                                       first_name=first_name,
                                       last_name=last_name,
                                       middle_name=middle_name,
                                       role=role_int,
                                       is_active=True)
        return redirect(reverse('login'))
    return render(request, 'authentication/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        role = request.POST.get('role')
        role_int = 1 if role == 'librarian' else 0

        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse('Email already registered')
        CustomUser.objects.create_user(email=email, password=password,
                                       first_name=first_name,
                                       last_name=last_name,
                                       middle_name=middle_name,
                                       role=role_int,
                                       is_active=True)
        return redirect(reverse('login'))
    return render(request, 'authentication/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                request.session['user_id'] = user.id
                return redirect(reverse('users_list'))
            else:
                return HttpResponse("Invalid credentials.")
        except CustomUser.DoesNotExist:
            return HttpResponse("User does not exist.")
    return render(request, 'authentication/login.html')

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect(reverse('login'))

def users_list(request):
    current_user = get_current_user(request)
    if not current_user or current_user.role != 1:
        return HttpResponse("Access denied. Librarians only.")
    users = CustomUser.objects.all()
    return render(request, 'authentication/users_list.html', {'users': users})

def user_details(request, user_id):
    current_user = get_current_user(request)
    if not current_user or current_user.role != 1:
        return HttpResponse("Access denied. Librarians only.")
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'authentication/user_details.html', {'user': user})
