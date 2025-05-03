from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime

from calcuvaca_site.forms import InsertEmploy
from calcuvaca_site.models import Employ, VacationTaken
from calcuvaca_site.services import get_vacation_days

def home(request: HttpRequest):
    employs = Employ.objects.all()
    context = {'employs': employs}

    return render(request, 'home.html', context)

def employ_details(request: HttpRequest, id: str):
    try:
        employ = Employ.objects.get(pk=int(id))
        vacations_taken = VacationTaken.objects.filter(employ=int(id))
        days_taken = 0

        for data in vacations_taken:
            days_taken += data.vacation_days

        vacation_days = get_vacation_days(employ.entry_date, days_taken)

        context = {'employ': employ, 'days_taken': days_taken, 'vacation_days': vacation_days}
    except ObjectDoesNotExist:
        context = {'employ': None, 'vacations_taken': None}

    return render(request, 'details.html', context)

def employ_insert(request: HttpRequest):
    message = ''
    form = InsertEmploy(request.POST or None)

    if request.method == 'POST':
        name = request.POST["name"]
        entry_date = request.POST["entry_date"]

        employ = Employ(name=name, entry_date=entry_date, created_at=datetime.now().strftime("%Y-%m-%d"), modified_at=datetime.now().strftime("%Y-%m-%d"))
        employ.save()

        return redirect("home")

    context = {'form': form, 'message': message}
    
    return render(request, 'employ_insert.html', context)
