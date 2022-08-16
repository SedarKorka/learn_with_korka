from rest_framework import serializers

from .models import Course, Lesson,Comment, Category, Quiz

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title','slug') 

class CourseListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','title','short_description','slug','get_image') 

class CourseDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','title','short_description','long_description','slug') 

class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id','title','short_description','long_description','slug','lesson_type','youtube_id') 
class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','name','email','content','created_at') 

class QuizSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Quiz
        fields = ('id','lesson_id','question','answer','op1','op2','op3')


