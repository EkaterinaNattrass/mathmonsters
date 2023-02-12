
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mathmonsters.settings")

from django.core.wsgi import get_wsgi_application
print("wsgi.py")
application = get_wsgi_application()
