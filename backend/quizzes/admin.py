from django.contrib import admin
from .models import Quiz, QuizAttempt, GeneratedImage

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'created_at')
    search_fields = ('question',)

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quiz', 'is_correct', 'attempted_at')
    list_filter = ('is_correct',)
    autocomplete_fields = ('user', 'quiz')

@admin.register(GeneratedImage)
class GeneratedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'attempt', 'url', 'created_at')
