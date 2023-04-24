from django.urls import path
from . import views
url_patterns = [
    path('', view=views.home, name="Contributions_home")
]