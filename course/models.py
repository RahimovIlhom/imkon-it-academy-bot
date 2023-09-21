from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} - {self.name}"


class Lesson(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.category} - {self.desc[:8]}"


class User(models.Model):
    user_id = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
