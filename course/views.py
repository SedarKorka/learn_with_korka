from unicodedata import category
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from .models import Comment, Course, Lesson, Category
from .serializers import CourseListSerializers,CourseDetailSerializers, LessonListSerializers, CommentsSerializers, CategorySerializers, QuizSerializer

@api_view(['GET'])
def get_quiz(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    quiz = lesson.quizzes.first()
    serializer = QuizSerializer(quiz)
    return Response(serializer.data)






@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializers(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_courses(request):
    category_id = request.GET.get('category_id','')
    courses = Course.objects.all()

    if category_id:
        courses = courses.filter(Categories__in =[int(category_id)])
    serializer = CourseListSerializers(courses, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_frontpage_courses(request):
    courses = Course.objects.all()[0:9]
    serializer = CourseListSerializers(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializers(course)
    lesson_serializer = LessonListSerializers(course.lessons.all(), many=True)

    if request.user.is_authenticated:
        course_data = course_serializer.data
    else:
        course_data = {}

    data = {
        'course':course_data,
        'lessons': lesson_serializer.data
    }
    return Response(data)

@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentsSerializers(lesson.comments.all(),many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    #name = data.get('name')
    
    #email = data.get('email')
    #content = data.get('content')

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(course=course,lesson=lesson,name= request.user.username,email=request.user,content=data.get('content'),created_by=request.user)
    serializer = CommentsSerializers(comment)

    return Response(serializer.data)


