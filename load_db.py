import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogproject.settings")
django.setup()

from django.core.management import call_command

call_command("loaddata", "db.json")
