from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET', 'POST'])

def create_order_api(request, ids):
    if request.method == "GET":
        print(ids)

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