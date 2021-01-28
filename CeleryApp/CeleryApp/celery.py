from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryApp.settings')

app = Celery('CeleryApp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'auto_update_every_5_minutes': {
        'task': 'StorageFiles.tasks.update_sensitivity',
        'schedule': crontab(minute='*/5'),
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
