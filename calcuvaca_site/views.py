from django.http import HttpRequest
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
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
