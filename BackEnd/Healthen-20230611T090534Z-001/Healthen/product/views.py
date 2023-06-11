from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment, Doctor, User, Task, Quiz, Question, Answer, Result, SubmittedTask, GameScore
from .serializers import AppointmentSerializer, DoctorSerializer, UserSerializer, TaskSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, ResultSerializer, SubmittedTaskSerializer, GameScoreSerializer


class UserView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(User, id=param.get('id'))
            serializer = UserSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('name')):
            item = User.objects.filter(name=param.get('name'))
            serializer = UserSerializer(item,many=True)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('email')):
            item = User.objects.filter(email=param.get('email'))
            serializer = UserSerializer(item,many=True)
            return Response({"status": "success", "data": serializer.data}, status=200)
        services = User.objects.all()
        response = UserSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def patch(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(User, id=param.get('id'))
            serializer = UserSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data},status=200)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(User, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

class DoctorView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(Doctor, id=param.get('id'))
            serializer = DoctorSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('name')):
            item = Doctor.objects.filter(name=param.get('name'))
            serializer = DoctorSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        elif bool(param.get('email')):
            item = Doctor.objects.filter(email=param.get('email'))
            serializer = DoctorSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        services = Doctor.objects.all()
        response = DoctorSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = DoctorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def patch(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(Doctor, id=param.get('id'))
            serializer = DoctorSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data},status=200)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(Doctor, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

class AppointmentView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(Appointment, id=param.get('id'))
            serializer = AppointmentSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('name')):
            item = Appointment.objects.filter(name=param.get('name'))
            serializer = AppointmentSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        services = Appointment.objects.all()
        response = AppointmentSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = AppointmentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def patch(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(Appointment, id=param.get('id'))
            serializer = AppointmentSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data},status=200)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(Appointment, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

class TaskView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(Task, id=param.get('id'))
            serializer = TaskSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('name')):
            item = Task.objects.filter(name=param.get('name'))
            serializer = TaskSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        elif bool(param.get('user_email')):
            item = Task.objects.filter(user_email=param.get('user_email'))
            serializer = TaskSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        # elif bool(param.get('user_email','submission')):
        #     item = Task.objects.filter(user_email=param.get('user_email')).filter(submission=param.get("submission"))
        #     serializer = TaskSerializer(item,many=True)
        #     return Response({"data": serializer.data},status=200)
        services = Task.objects.all()
        response = TaskSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def patch(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(Task, id=param.get('id'))
            serializer = TaskSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data},status=200)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(Task, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

class QuizView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(Quiz, id=param.get('id'))
            serializer = QuizSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('type_quiz')):
            item = Quiz.objects.filter(type_quiz=param.get('type_quiz'))
            serializer = QuizSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        services = Quiz.objects.all()
        response = QuizSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = QuizSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(Quiz, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

class QuestionView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(Question, id=param.get('id'))
            serializer = QuestionsSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('type_quiz')):
            item = Question.objects.filter(type_quiz=param.get('type_quiz'))
            serializer = QuestionSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        services = Question.objects.all()
        response = QuestionSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(Question, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

class AnswerView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('q_id')):
            item = Answer.objects.filter(q_id=param.get('q_id'))
            serializer = AnswerSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        services = Answer.objects.all()
        response = AnswerSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = AnswerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(Answer, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

class ResultView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('type')):
            item = get_object_or_404(Result, type_quiz=param.get('type'))
            serializer = ResultSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('id')):
            item = Result.objects.filter(user_id=param.get('id'))
            serializer = ResultSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        services = Result.objects.all()
        response = ResultSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = ResultSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(Result, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

class SubmittedTaskView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('doctor_id')):
            item = get_object_or_404(SubmittedTask, doctor_id=param.get('doctor_id'))
            serializer = SubmittedTaskSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('user_id')):
            item = SubmittedTask.objects.filter(user_id=param.get('user_id'))
            serializer = SubmittedTaskSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        services = SubmittedTask.objects.all()
        response = SubmittedTaskSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = SubmittedTaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(SubmittedTask, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

    def patch(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(SubmittedTask, id=param.get('id'))
            serializer = SubmittedTaskSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data},status=200)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)

class GameScoreView(APIView):
    def get(self, request):
        param = request.GET
        if bool(param.get('type_game')):
            item = get_object_or_404(GameScore, type_game=param.get('type_game'))
            serializer = GameScoreSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=200)
        elif bool(param.get('user_id')):
            item = GameScore.objects.filter(user_id=param.get('user_id'))
            serializer = GameScoreSerializer(item,many=True)
            return Response({"data": serializer.data},status=200)
        services = GameScore.objects.all()
        response = GameScoreSerializer(services, many=True)
        return Response({"data": response.data},status=200)

    def post(self, request):
        data = request.data
        serializer = GameScoreSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request):
        param = request.GET
        item = None
        if bool(param.get('id')):
            item = get_object_or_404(GameScore, id=param.get('id'))
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"},status=200)

    def patch(self, request):
        param = request.GET
        if bool(param.get('id')):
            item = get_object_or_404(GameScore, id=param.get('id'))
            serializer = GameScoreSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data},status=200)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
