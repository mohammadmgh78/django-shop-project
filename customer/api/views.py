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


class CreateCustomerAPI(APIView):

    def get(self, request, format=None):
        print('here')
        print(Customer.objects.all())
        serializer = CustomerSerializer(Customer.objects.all(), many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        print(request.data)
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
        customer_data = dict(list(request.data.items())[1:6])
        user_data = dict(list(request.data.items())[6:8])
        customer_serializer = CustomerSerializer(data=customer_data)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            print('user_serializer is valid!')
            user_created = User.objects.create_user(username=user_data['username'], password=user_data['password'])
            print(user_created)

        if customer_serializer.is_valid():
            print('customer_serializer is valid!')
            customer_created = customer_serializer.save()
            customer_created.owner = user_created
            customer_created.save()
        print(customer_data)
        print(user_data)
        # print(list(request.data.items()))
        return Response({})

