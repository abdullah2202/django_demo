from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
   model = Choice
   extra = 3

class QuestionAdmin(admin.ModelAdmin):
   # Form to show when adding a question
   fieldsets = [
      (None,               {'fields': ['question_text']}),
      ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
   ]
   # Shows the choices inline with the question
   inlines = [ChoiceInline]

   # Displays all questions
   list_display = ('question_text', 'pub_date', 'was_published_recently')
   
   # Filter for pub_date
   list_filter = ['pub_date']

   # Search function
   search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

