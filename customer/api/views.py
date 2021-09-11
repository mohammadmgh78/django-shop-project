from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
User = get_user_model()
# from customer.models import Customer
#
#
from customer.api.serializers import CustomerSerializer, UserSerializer
from customer.models import Customer


class CreateCustomer(APIView):

    def get(self, request, format=None):
        print('here')
        print(Customer.objects.all())
        serializer = CustomerSerializer(Customer.objects.all(), many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        # print(request.data['select_student'])
        # print('successsss')
        # student = Customer.objects.get(pk=request.data['select_student'])
        # for lesson_id in request.data['lessons']:
        #     lesson = Lesson.objects.get(pk=lesson_id)
        #     lesson.students.add(student)
        #     student.lessons.add(lesson)
        #     lesson.save()
        #     student.save()

        # serializer = StudentSerializer(Student.objects.all(), many=True)
        return Response({})

class CreateUser(APIView):

    def get(self, request, format=None):
        print('here')
        print(User.objects.all())
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        # print(request.data['select_student'])
        # print('successsss')
        # student = Customer.objects.get(pk=request.data['select_student'])
        # for lesson_id in request.data['lessons']:
        #     lesson = Lesson.objects.get(pk=lesson_id)
        #     lesson.students.add(student)
        #     student.lessons.add(lesson)
        #     lesson.save()
        #     student.save()

        # serializer = StudentSerializer(Student.objects.all(), many=True)
        return Response({})