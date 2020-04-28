from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the celery app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smithworks_frontend.settings")

app = Celery("smithworks_frontend")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
