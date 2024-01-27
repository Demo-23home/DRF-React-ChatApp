from rest_framework import serializers
from .models import ChatMessage
from api.models import Profile




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'full_name', 'image']
    








class ChatMessageSerializer(serializers.ModelSerializer):
    reciver_profile = ProfileSerializer(read_only=True)
    sender_profile = ProfileSerializer(read_only=True)

    
    class Meta:
        model = ChatMessage
        fields = ['id', 'user', 'sender', 'sender_profile','reciever', 'reciver_profile', 'message', 'is_read', 'date']