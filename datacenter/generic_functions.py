import datetime

from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    else:
        return localtime() - visit.entered_at


def format_duration(duration):
    return datetime.timedelta(seconds=int(duration.total_seconds()))


def is_visit_long(duration, minutes=60):
    return int(duration.total_seconds() / 60) > minutes
