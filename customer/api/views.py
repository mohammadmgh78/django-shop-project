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


from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)