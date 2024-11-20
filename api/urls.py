from django.urls import path
from .views import ProcessAudioView

urlpatterns = [
    path('process/', ProcessAudioView.as_view(), name='process_audio'),
]
