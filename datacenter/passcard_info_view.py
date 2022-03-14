import datetime

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit


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

def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    else:
        return localtime() - visit.entered_at


def format_duration(duration):
    return datetime.timedelta(seconds=int(duration.total_seconds()))


def is_visit_long(duration, minutes=60):
    return int(duration.total_seconds() / 60) > minutes