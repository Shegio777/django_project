from django.urls import path
from event.views import event, order_details, card_details

app_name = "event"

urlpatterns = [
    path('', event, name='index'),
    path('order/<int:event_id>/', order_details, name='confirm_order'),
    path('card_details/', card_details, name='card_details'),
]

