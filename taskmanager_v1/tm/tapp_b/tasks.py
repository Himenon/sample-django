from celery import shared_task
from . import models as app_models
from tapp_a import models as app_a_models


@shared_task
def hello_from_b(*args, **kwargs):
    print("Hello! From B")
    print("args = {}".format(args))
    print("kwargs = {}".format(kwargs))


@shared_task
def counter_upper(counter_id, *args, **kwargs):
    m = app_models.Counter.objects.get(pk=counter_id)
    m.count += 1
    m.save()
    print(m)
    return m


@shared_task
def counter_upper_task_a_from_b(counter_id, *args, **kwargs):
    m = app_a_models.Counter.objects.get(pk=counter_id)
    m.count += 1
    m.save()
    print(m)
    return m
