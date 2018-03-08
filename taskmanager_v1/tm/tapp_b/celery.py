from os import environ
from celery import Celery
app = Celery('tapp_b', broker=environ.get('BROKER_URL'))
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
