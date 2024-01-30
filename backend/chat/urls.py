from django.urls import path
from .views import *
urlpatterns = [
    path("my-messages/<user_id>/", MyInbox.as_view()),
    path("get-messages/<sender_id>/<reciever_id>/", GetMessages.as_view()),
    path("send-messages/", SendMessages.as_view()),
    path("",getRoutes)
]
