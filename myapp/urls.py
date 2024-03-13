from django.urls import path
from .views import ReminderCreateView

urlpatterns = [
    path('reminder/', ReminderCreateView.as_view(), name='reminder_create'),
    path('reminder/<int:pk>/', ReminderCreateView.as_view(), name='reminder_details'),

]