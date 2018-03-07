import os
from celery import Celery
print(os.environ.get('CELERY_BROKER_URL'))
app = Celery('tapp_a', broker='redis://broker:6379')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
