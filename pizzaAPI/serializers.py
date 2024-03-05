from rest_framework.serializers import ModelSerializer

from pizzaAPI.models import Pizza, Order


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class OrderPizzaSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['pizza'] = instance.pizza.name

        return redata

