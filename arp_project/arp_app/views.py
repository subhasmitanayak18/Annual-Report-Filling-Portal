from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            if user.check_password(password):
                login(request, user)

                role = user.role.role.strip().lower()
                division = user.division.division.strip() if user.division else ""

                print("ROLE:", role)
                print("DIVISION:", division)

                if role == 'admin':
                    return redirect(reverse('admin:index'))
                elif role == 'filling_user' and division == 'Water, Air and Noise Monitoring Network':
                    return redirect('chapter3')
                elif role == 'filling_user' and division == 'Water, Air and Noise Monitoring Network':
                    return redirect('chapter5')
                elif role == 'filling_user' and division == 'Committees Constituted by the Central Board  and their Activities':
                    return redirect('chapter4')
                elif role == 'filling_user' and division == 'Present State of Environment; Environmental':
                    return redirect('chapter6')
                elif role == 'filling_user' and division == 'Environmental Researches':
                    return redirect('chapter7')
                elif role == 'filling_user' and division == 'Environmental Training':
                    return redirect('chapter8')
                elif role == 'filling_user' and division == 'Environmental Awareness and Public Participation':
                    return redirect('chapter9')
                elif role == 'filling_user' and division == 'Environmental Standards':
                    return redirect('chapter10')
                elif role == 'filling_user' and division == 'Prosecutions Launched, Convictions Secured & Directions issued for Closure of Polluting Industries':
                    return redirect('chapter11')
                elif role == 'filling_user' and division == 'Finance and Accounts':
                    return redirect('chapter12')
                
            
                
            else:
                print("Incorrect password")
                messages.error(request, 'Invalid password.')
        except User.DoesNotExist:
            print("User not found")
            messages.error(request, 'User with this email does not exist.')

    return render(request, 'arp_app/login.html')

def chapter3_view(request):
    return render(request, 'arp_app/chapter3.html')

def chapter5_view(request):
    return render(request, 'arp_app/chapter5.html')

def chapter4_view(request):
    return render(request, 'arp_app/chapter4.html')

def chapter6_view(request):
    return render(request, 'arp_app/chapter6.html')

def chapter7_view(request):
    return render(request, 'arp_app/chapter7.html')

def chapter8_view(request):
    return render(request, 'arp_app/chapter8.html')

def chapter9_view(request):
    return render(request, 'arp_app/chapter9.html')

def chapter10_view(request):
    return render(request, 'arp_app/chapter10.html')

def chapter11_view(request):
    return render(request, 'arp_app/chapter11.html')

def chapter12_view(request):
    return render(request, 'arp_app/chapter12.html')

def home_view(request):
    return render(request, 'arp_app/home.html')

