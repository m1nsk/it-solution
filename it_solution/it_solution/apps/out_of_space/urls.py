from django.conf.urls import url
from .views import get_messages, mark_message

urlpatterns = [
    url(r'^get_messages', get_messages),
    url(r'^mark_read', mark_message),
]