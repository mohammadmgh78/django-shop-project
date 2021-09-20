from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from customer.models import Customer
from order.models import Order
from product.models import Product


@api_view(['GET', 'POST'])

def create_order_api(request, ids):
    if request.method == "GET":
        print(ids)
        print(request.user.username)
        print(request.user, type(request.user))
        product = Product.objects.filter(pk=ids).first()
        customer = Customer.objects.filter(owner=request.user).first()
        print(customer)


        # order = Order.objects.update_or_create(order_status='Not Selected', user=customer)
        # order = order.products.add(product)
        # print(order)
        # order.save()
        # print(order)
        #
        if Order.objects.filter(user=customer, order_status='Not Selected'):
            print('came here')
            order = Order.objects.filter(user=customer).first()

            # print(order.products.all())
            # order.products.add(product)
            # order.save()
            if product in order.products.all():
                order.products.remove(product)
                order.save()
            else:
                order.products.add(product)
                order.save()
        else:
            order = Order(order_status='Not Selected', user=customer)
            order.save()
            order.products.add(product)
            order.save()
    print(order.id)

    return Response({})
        # for post in Post.objects(id=post_id):
        #     if post.status == STATUS['ACTIVE']:
        #         # print('THIS IS ACTIVE')
        #         Post.objects(id=post_id).update(
        #             status=STATUS['DEACTIVE']
        #         )
        #     elif post.status == STATUS['DEACTIVE']:
        #         # print('THIS IS DEACTIVE')
        #         Post.objects(id=post_id).update(
        #             status=STATUS['ACTIVE']
        #         )
        # return render_template('posts_list.html')