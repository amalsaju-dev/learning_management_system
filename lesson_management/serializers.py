from rest_framework import serializers

from lesson_management.models import Lesson

class LessonSerialiizer(serializers.ModelSerializer):

    class Meta:

        model = Lesson

        fields = "__all__"

        read_only_fields = ["id","module","order","slug","created_at","updated_at"]


        





