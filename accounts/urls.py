from django.urls import path
from  .views import *

urlpatterns = [
    path("", AccountView.as_view()),
]
