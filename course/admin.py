from django.contrib import admin
from .models import Lesson, Category, Course, User

# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(User)
