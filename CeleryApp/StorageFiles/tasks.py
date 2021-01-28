from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .views import  auto_update_sensitivity
 

@shared_task
def update_sensitivity():
    auto_update_sensitivity()
    print("Ran auto updater!!!")