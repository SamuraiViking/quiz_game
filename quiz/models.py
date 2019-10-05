from django.db import models


class Course(models.Model):
    # Time Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Associations 
    name = models.CharField(max_length=200)

class Quiz(models.Model):
    # Time Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Assocations
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    # Time Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Values
    question_text = models.CharField(max_length=200, default='')
    answer_text = models.CharField(max_length=200, default='')
    # Assocations
    quiz = models.ForeignKey(Course, on_delete=models.CASCADE)

class Choice(models.Model):
    # Time Stamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Values
    answer_text = models.CharField(max_length=200, default='')
    is_answer = models.BooleanField(default=False)
    # Associations
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
