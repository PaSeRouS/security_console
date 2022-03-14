from django.shortcuts import render

from datacenter.generic_functions import format_duration, get_duration, is_visit_long
from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        duration = get_duration(visit)

        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(duration)
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
