import os
import sys
from myproject.wsgi import application

sys.path.insert(0, os.path.dirname("C:\Users\Phillip Williams\DUKE\kenan\mysite\mysite\wsgi.py"))

environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")