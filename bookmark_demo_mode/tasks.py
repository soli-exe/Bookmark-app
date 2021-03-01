import datetime
from django.utils import timezone
from .models import DemoBookMark


def delete_expired_objects():
    time = timezone.now() - datetime.timedelta(minutes=5)
    objs = DemoBookMark.objects.filter(publication_date__lte=time)
    return objs.delete()
