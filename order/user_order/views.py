from rest_framework import viewsets, status
from .models import Shop, Order
from .serializers import ShopSerializer, OrderSerializer
from rest_framework.response import Response

from .producer import publish

class ShopViewSet(viewsets.ViewSet):
    def list(self, request):  #/api/shop
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def create(self, request):  #/api/shop
        serializer = ShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('shop_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  #/api/shop/<str:idx>
        shop = Shop.objects.get(id=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def update(self, request, pk=None):  #/api/shop/<str:idx>
        shop = Shop.objects.get(id=pk)
        serializer = ShopSerializer(instance = shop, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('shop_updated',serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  #/api/shop/<str:idx>
        shop = Shop.objects.get(id=pk)
        shop.delete()
        publish('shop_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):  #/api/order
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):  #/api/order
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('order_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  #/api/order/<str:idx>
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk=None):  #/api/order/<str:idx>
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(instance = order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('order_updated',serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  #/api/order/<str:idx>
        order = Order.objects.get(id=pk)
        order.delete()
        publish('order_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)