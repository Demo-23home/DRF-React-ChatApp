from django.shortcuts import render
from .serializers import ChatMessageSerializer, ChatMessage
from rest_framework import generics
from django.db.models import Subquery, OuterRef, Q
from api.models import User
# Create your views here.


class MyInbox(generics.ListAPIView):
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        messages = ChatMessage.objects.filter(
            id__in = Subquery(
                User.objects.filter(
                    Q(sender__reciever=user_id)|
                    Q(reciever__sender=user_id)
                ).distinct().annotate(
                    last_msg =Subquery(
                        ChatMessage.objects.filter(
                            Q(sender=OuterRef('id'), reciever=user_id)|
                            Q(reciever=OuterRef('id'), sender=user_id)
                        ).order_by('-id')[:1].values_list("id",flat=True)
                    )
                ).values_list("last_msg", flat=True).order_by("-id")
            )
        ).order_by("-id")
        return messages
    

    