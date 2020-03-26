import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abstract_anticafe.settings')

app = Celery('abstract_anticafe')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.s
app.autodiscover_tasks()
