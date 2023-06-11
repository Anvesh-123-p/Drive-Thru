from distutils.command.upload import upload
from django.db import models


class User(models.Model):
    profile = models.TextField(blank=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32,blank=True)
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    )  
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    mobile_number = models.BigIntegerField()
    password = models.CharField(max_length=256)
    about = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.email + " (" +  self.first_name + " )"


class Doctor(models.Model):
    profile = models.TextField(blank=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32,blank=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    )  
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    experience = models.IntegerField()
    mobile_number = models.BigIntegerField()
    password = models.CharField(max_length=256)
    about =  models.TextField(blank=True)
    registeration_id = models.BigIntegerField(blank=True,null=True)
    language = models.CharField(max_length=256,blank=True)
    qualification = models.CharField(max_length=64)
    specialization = models.CharField(max_length=256)
    available_between = models.CharField(max_length=32,blank=True)
    def __str__(self):
        return self.email + " (" +  self.first_name + " )"

class Appointment(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32,blank=True)
    description = models.CharField(max_length=256,blank=True)
    mobile_number = models.BigIntegerField()
    date = models.DateField()
    time = models.TimeField(auto_now=False)
    upload = models.FileField(blank=True)
    statuses = (
    ('OH', 'On Hold'),
    ('SH', 'Scheduled'),
    ('RJ', 'Rejected'),
    )
    status = models.CharField(choices=statuses, default="OH",max_length=2)

class Task(models.Model):
    doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    user_email = models.ForeignKey(User, to_field="email", db_column="email",on_delete=models.CASCADE)
    tasks = (
    ('DW', 'Draw'),
    ('IM', 'Image'),
    )
    task = models.CharField(choices=tasks, default="OH",max_length=2)
    date = models.DateField()
    description = models.CharField(max_length=256,blank=True)
    image = models.TextField(blank=True,null=True)
    submission = models.CharField(max_length=5,blank=True,default="False")
   
    def __str__(self):
        return str(self.id)

class Quiz(models.Model):
    type_quiz = models.CharField(max_length=100)

    def __str__(self):
        return self.type_quiz

class Question(models.Model):
    type_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text

    def get_question():
        return self.question_set.all

class Answer(models.Model):
    q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    score = models.IntegerField()

    def __str__(self):
        return self.text

    def get_answers():
        return self.anwer.all

class Result(models.Model):
    type_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField()

class SubmittedTask(models.Model):
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    submitted_image = models.TextField(blank=True,null=True)
    submitted_answer = models.CharField(max_length=255,blank=True,null=True)
    task_type = models.CharField(max_length=25)
    doctor_comment = models.CharField(max_length=100,blank=True)
    task_score = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return str(self.id)

class GameScore(models.Model):
    type_game = models.CharField(max_length=20)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField()