from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import login, preceptor_CR, preceptor_RUD 

urlpatterns = [
    path('login/', login)
]

urlpatterns = format_suffix_patterns(urlpatterns)