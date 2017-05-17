import os, sys


sys.path.append('/usr/share/palamar/palamar')

sys.path.append('/usr/share/palamar/venv/lib/python2.7/site-packages')


from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "palamar.settings")

application = get_wsgi_application()
