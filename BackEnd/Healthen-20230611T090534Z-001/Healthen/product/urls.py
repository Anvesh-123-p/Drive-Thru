from django.urls import path

from .views import UserView, DoctorView, AppointmentView, TaskView, QuizView, QuestionView, AnswerView, ResultView, SubmittedTaskView, GameScoreView

urlpatterns = [
    path("api/users/", UserView.as_view()),
    path("api/doctors/", DoctorView.as_view()),
    path("api/appointments/", AppointmentView.as_view()),
    path("api/tasks/", TaskView.as_view()),
    path("api/quiz/", QuizView.as_view()),
    path("api/question/", QuestionView.as_view()),
    path("api/answer/", AnswerView.as_view()),
    path("api/result/", ResultView.as_view()),
    path("api/submitted_task/", SubmittedTaskView.as_view()),
    path("api/gameScore/", GameScoreView.as_view()),
]

