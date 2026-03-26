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
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)

                role = user.role.role.strip().lower()
                division = user.division.division.strip() if user.division else ""

                print("ROLE:", role)
                print("DIVISION:", division)

                if role == 'admin':
                    return redirect(reverse('admin:index'))
                elif role == 'filling_user' and division == 'Mediation and Coordination':
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
                    messages.error(request, f'No page configured for role "{role}" / division "{division}".')
                
            
                
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
    if request.method == 'POST':
        request.session['chapter5_data'] = {
            'strengthening': request.POST.get('strengthening', ''),
            'polluted_river': request.POST.get('polluted_river', ''),
            'ganga_authority': request.POST.get('ganga_authority', ''),
            'objectives': request.POST.get('objectives', ''),
            'ganga_quality': request.POST.get('ganga_quality', ''),
            'others': request.POST.get('others', ''),
            'manual_quality': request.POST.get('manual_quality', ''),
            'air_monitoring': request.POST.get('air_monitoring', ''),
            'parameters_monitored': request.POST.get('parameters_monitored', ''),
            'status_air': request.POST.get('status_air', ''),
            'ncap': request.POST.get('ncap', ''),
            'noise_monitoring': request.POST.get('noise_monitoring', ''),
        }
        return redirect('chapter5_submitted')
    return render(request, 'arp_app/chapter5.html')

def chapter5_submitted_view(request):
    data = request.session.get('chapter5_data', {})
    return render(request, 'arp_app/chapter5_submitted.html', {'data': data})

def chapter4_view(request):
    if request.method == 'POST':
        request.session['chapter4_data'] = {
            'section_4_1': request.POST.get('section_4_1', ''),
            'section_4_2': request.POST.get('section_4_2', ''),
            'section_4_3': request.POST.get('section_4_3', ''),
            'section_4_4': request.POST.get('section_4_4', ''),
            'section_4_5': request.POST.get('section_4_5', ''),
            'section_4_6': request.POST.get('section_4_6', ''),
            'section_4_7': request.POST.get('section_4_7', ''),
        }
        return redirect('chapter4_submitted')
    return render(request, 'arp_app/chapter4.html')

def chapter4_submitted_view(request):
    data = request.session.get('chapter4_data', {})
    return render(request, 'arp_app/chapter4_submitted.html', {'data': data})

def chapter6_view(request):
    if request.method == 'POST':
        request.session['chapter6_data'] = {
            'cetp': request.POST.get('cetp', ''),
            'cdwm': request.POST.get('cdwm', ''),
            'ewaste': request.POST.get('ewaste', ''),
            'ewaste_activities': request.POST.get('ewaste_activities', ''),
            'waste_tyre': request.POST.get('waste_tyre', ''),
            'waste_tyre_activities': request.POST.get('waste_tyre_activities', ''),
            'battery_waste': request.POST.get('battery_waste', ''),
            'battery_intro': request.POST.get('battery_intro', ''),
            'battery_epr': request.POST.get('battery_epr', ''),
            'flyash': request.POST.get('flyash', ''),
            'hazardous': request.POST.get('hazardous', ''),
            'hazardous_sop': request.POST.get('hazardous_sop', ''),
            'contaminated_assessment': request.POST.get('contaminated_assessment', ''),
            'biomedical': request.POST.get('biomedical', ''),
            'biomedical_scenario': request.POST.get('biomedical_scenario', ''),
            'biomedical_implementation': request.POST.get('biomedical_implementation', ''),
        }
        return redirect('chapter6_submitted')
    return render(request, 'arp_app/chapter6.html')

def chapter6_submitted_view(request):
    data = request.session.get('chapter6_data', {})
    return render(request, 'arp_app/chapter6_submitted.html', {'data': data})

def chapter7_view(request):
    if request.method == 'POST':
        request.session['chapter7_data'] = {}
        return redirect('chapter7_submitted')
    return render(request, 'arp_app/chapter7.html')

def chapter7_submitted_view(request):
    data = request.session.get('chapter7_data', {})
    return render(request, 'arp_app/chapter7_submitted.html', {'data': data})

def chapter8_view(request):
    if request.method == 'POST':
        request.session['chapter8_data'] = {
            'training_orientation': request.POST.get('training_orientation', ''),
        }
        return redirect('chapter8_submitted')
    return render(request, 'arp_app/chapter8.html')

def chapter8_submitted_view(request):
    data = request.session.get('chapter8_data', {})
    return render(request, 'arp_app/chapter8_submitted.html', {'data': data})

def chapter9_view(request):
    if request.method == 'POST':
        request.session['chapter9_data'] = {
            'exhibitions': request.POST.get('exhibitions', ''),
            'wed_celebration': request.POST.get('wed_celebration', ''),
            'public_grievances': request.POST.get('public_grievances', ''),
        }
        return redirect('chapter9_submitted')
    return render(request, 'arp_app/chapter9.html')

def chapter9_submitted_view(request):
    data = request.session.get('chapter9_data', {})
    return render(request, 'arp_app/chapter9_submitted.html', {'data': data})

def chapter10_view(request):
    if request.method == 'POST':
        request.session['chapter10_data'] = {
            'development_standards': request.POST.get('development_standards', ''),
            'notified_standards': request.POST.get('notified_standards', ''),
        }
        return redirect('chapter10_submitted')
    return render(request, 'arp_app/chapter10.html')

def chapter10_submitted_view(request):
    data = request.session.get('chapter10_data', {})
    return render(request, 'arp_app/chapter10_submitted.html', {'data': data})

def chapter11_view(request):
    if request.method == 'POST':
        request.session['chapter11_data'] = {
            'prosecutions': request.POST.get('prosecutions', ''),
        }
        return redirect('chapter11_submitted')
    return render(request, 'arp_app/chapter11.html')

def chapter11_submitted_view(request):
    data = request.session.get('chapter11_data', {})
    return render(request, 'arp_app/chapter11_submitted.html', {'data': data})

def chapter12_view(request):
    if request.method == 'POST':
        uploaded = request.FILES.get('financial_report')
        request.session['chapter12_data'] = {
            'financial_report_name': uploaded.name if uploaded else '',
        }
        return redirect('chapter12_submitted')
    return render(request, 'arp_app/chapter12.html')

def chapter12_submitted_view(request):
    data = request.session.get('chapter12_data', {})
    return render(request, 'arp_app/chapter12_submitted.html', {'data': data})

def home_view(request):
    return render(request, 'arp_app/home.html')

