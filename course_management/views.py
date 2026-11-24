from django.shortcuts import render

# Create your views here.

from course_management.models import Course

from course_management.serializer import CourseSerializer

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from rest_framework import authentication,permissions

class CourseListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CourseSerializer

    def get_queryset(self):

        return Course.objects.filter(trainer=self.request.user)

    def perform_create(self,serializer):

        serializer.save(trainer=self.request.user)

   

class CourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_classs = CourseSerializer

    def get_queryset(self):
        
        return Course.objects.filter(trainer=self.request.user)



