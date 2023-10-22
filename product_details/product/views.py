from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from product.models import User, Product
from product.serializer import UserSerializer, ProductSerializer

class UserAPI(APIView):
    def post(self, request):
        try:
            serialized = UserSerializer(data = request.data)
            if serialized.is_valid():
                user_obj = serialized.save()
                return Response({'error': '', 'error_code': '', 'data': {'user_id':user_obj.id}}, status=200)
            else:
                error = ', '.join(['{0}:{1}'.format(k, str(v[0])) for k, v in serialized.errors.items()])
                return Response({'error': error, 'error_code': 'HS002', 'data': {}}, status=200)
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)

class ProductDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            serialized = ProductSerializer(Product.objects.all(),many=True)
            return Response({'error': '', 'error_code': '', 'data': {'user_email':request.user.email,'product_details':serialized.data}}, status=200)
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)


    def post(self, request):
        try:
            serialized = ProductSerializer(data = request.data)
            if serialized.is_valid():
                product_details = serialized.save()
                return Response({'error': '', 'error_code': '', 'data': {'product_details':serialized.data}}, status=200)
            else:
                error = ', '.join(['{0}:{1}'.format(k, str(v[0])) for k, v in serialized.errors.items()])
                return Response({'error': error, 'error_code': 'HS002', 'data': {}}, status=200)
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)

