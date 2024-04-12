"""
WSGI config for OpPrint project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OpPrint.settings")

application = get_wsgi_application()

app = application  #i added this bcus im hosting my website with vercel bcus our allow host is set to .vercel in the settings.py



