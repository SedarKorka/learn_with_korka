from distutils.command.upload import upload
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length =255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:  
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Course(models.Model):
    Categories = models.ManyToManyField(Category)
    title = models.CharField(max_length =255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to = 'uploads', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url 
        else:
            return 'https://blogs.vmware.com/learning/files/2020/01/VMWQ419-1-VLZ-Icon-Refresh_R2__New-Courses.png'

class Lesson(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    ARTICLE = 'article'
    QUIZ = 'quiz'
    VIDEO = 'video'
    
    CHOICES_LESSON_TYPE = (
        (ARTICLE,'Article'),
        (QUIZ, 'Quiz'),
        (VIDEO,'Video'),
    )

    course = models.ForeignKey(Course, related_name='lessons',on_delete=models.CASCADE)
    title = models.CharField(max_length =255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices = CHOICES_STATUS, default = PUBLISHED)
    lesson_type = models.CharField(max_length=20,choices= CHOICES_LESSON_TYPE, default= ARTICLE)
    youtube_id = models.CharField(max_length=200, blank=True, null=True)

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments',on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

class Quiz(models.Model): 
    lesson = models.ForeignKey(Lesson, related_name='quizzes',on_delete=models.CASCADE)
    question = models.CharField(max_length=200,null=True)
    answer = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)

    class  Meta: 
        verbose_name_plural = 'Quizzes'


    
    
     

