from django.urls import path
from . import views

# URL patterns for the chat application. These routes handle viewing the chat index
# and individual chat rooms identified by their slugs.
urlpatterns = [
   # path("", views.chat, name="chat"),  # Root path for the chat index view.
    path('<str:room_slug>/', views.room, name="room"),  # Path for individual chat rooms.
    path('send-message/<str:room_slug>/', views.send_message, name="send_message"),
]
