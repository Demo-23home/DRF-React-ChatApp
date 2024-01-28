from django.shortcuts import render
from .models import Profile, User
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from chat.serializers import ProfileSerializer
from django.db.models import Q

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dahsBoard(request):
    if request.method == "GET":
        context = f"hey {request.user} you're seeing a GET response"
        return Response({'response':context}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        text = request.POST.get("text")
        response = f"hey {request.user} this is an POST response , your text is {text}"
        return Response({' ':response}, status=status.HTTP_200_OK)
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    


#Get all Routes
# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)



class ProfileDetail(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]




class SerachUser(generics.ListAPIView):
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()

    def list(self, request, *args, **kwargs):
        username = self.kwargs['username']
        logged_in_user = self.request.user
        users = Profile.objects.filter(
            Q(user__username__icontains=username)|
            Q(full_name__icontains=username)|
            Q(user__email__icontains=username)         )

        if not users.exists():
            return Response({"details":"User donsn't exist!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(users, many=True)
        return Response({"data":serializer.data})