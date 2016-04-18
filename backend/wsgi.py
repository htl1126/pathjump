"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# ref: http://stackoverflow.com/questions/32577998/wsgi-script-cannot-
#             be-loaded-as-python-module-500-internal-server-error
sys.path.append('/home/ubuntu/pathjump/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()
