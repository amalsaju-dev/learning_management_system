from django.shortcuts import render,get_object_or_404

# Create your views here.

from accounts.models import TrainerProfile,StudentProfile

from accounts.serializer import TrainerProfileSerializer

from accounts.serializer import TrainerSerializer 

from accounts.serializer import StudentSerializer

from accounts.serializer import StudentProfileSerializer


from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView

from rest_framework import authentication,permissions

class TrainerSignUpView(CreateAPIView):

    serializer_class = TrainerSerializer


class TrainerProfileRetrieveUpdateView(RetrieveUpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TrainerProfileSerializer

    def get_object(self):
        
        return get_object_or_404(TrainerProfile,user = self.request.user)



class StudentSignUpView(CreateAPIView):

    serializer_class = StudentSerializer


class StudentProfileRetrieveUpdateView(RetrieveUpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = StudentProfileSerializer

    def get_object(self):

        return get_object_or_404(StudentProfile,user=self.request.user)
