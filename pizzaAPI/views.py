from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from time import sleep

from .serializers import PizzaSerializer, OrderPizzaSerializer
from .models import Pizza, Order


class PizzaAPI(APIView):

    def get(self, request):
        pizza_list = Pizza.objects.all()
        serializer = PizzaSerializer(instance=pizza_list, many=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pizza_id = request.data.get('id')
        Pizza.objects.get(id=int(pizza_id)).delete()

        return Response('Deleted!', status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        pizza_id = request.data.get('id')

        if Pizza.objects.filter(id=pizza_id).exists():
            instance = Pizza.objects.get(id=pizza_id)
        else:
            return Response("Object does not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(instance, serializer.validated_data)

            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderPizzaAPIView(APIView):
    def get(self, request):
        phone_number = request.data.get('phone_number')
        orders = Order.objects.filter(phone_number=phone_number)
        serializer = OrderPizzaSerializer(instance=orders, many=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        serializer = OrderPizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
