from django.shortcuts import render, get_object_or_404

# Create your views here.
from course_management.models import Course

from module_management.models import Module

from module_management.serializer import ModuleSerializer

from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from rest_framework import authentication,permissions



class ModuleCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ModuleSerializer

    def perform_create(self, serializer):

        course_id = self.kwargs.get("pk")

        course_object = get_object_or_404(Course,id = course_id)

        return serializer.save(course = course_object)


class ModuleRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ModuleSerializer

    queryset = Module.objects.all()

        