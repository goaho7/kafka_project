from django.urls import path
from api.views import ProducerView

urlpatterns = [
    path('produce/', ProducerView.as_view(), name='produce')
]
