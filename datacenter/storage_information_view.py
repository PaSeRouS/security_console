from django.shortcuts import render

from datacenter.generic_functions import format_duration, get_duration
from datacenter.models import Passcard, Visit

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
