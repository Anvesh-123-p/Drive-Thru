from django.contrib import admin

from product.models import Doctor, User, Appointment, Task, Quiz, Question, Answer, Result, SubmittedTask

class Answer_admin(admin.TabularInline):
    model = Answer

class Question_admin(admin.ModelAdmin):
    inlines = [Answer_admin]

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Task)
admin.site.register(Quiz)
admin.site.register(Question,Question_admin)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(SubmittedTask)