from django.db import models
from django.conf import settings

class Quiz(models.Model):
    question   = models.TextField()
    answer     = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QuizAttempt(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz         = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    user_answer  = models.CharField(max_length=255)
    is_correct   = models.BooleanField(editable=False)
    attempted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.is_correct = (self.user_answer.strip().lower() == self.quiz.answer.strip().lower())
        super().save(*args, **kwargs)

class GeneratedImage(models.Model):
    attempt    = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='generated_images')
    url        = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for attempt {self.attempt.id}"
