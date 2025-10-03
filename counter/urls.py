from django.urls import path
from . import views
from .chatbot_views import chatbot
from .chatbot_views import chathome

urlpatterns = [
    path('', views.home, name='home'),
    path("chatbot/", chatbot, name="chatbot"),
    path("chathome/", chathome, name="chathome"),
    
]