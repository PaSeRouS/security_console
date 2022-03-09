import datetime

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for visit in visits:
        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    
    return render(request, 'storage_information.html', context)

def get_duration(visit):
    return localtime() - visit.entered_at

def format_duration(duration):
    return datetime.timedelta(seconds=int(duration.total_seconds()))
