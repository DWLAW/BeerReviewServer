
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from beerreviewapi.models import BeerType

class BeerTypeView(ViewSet):
    def list(self, request):
        beertypes = BeerType.objects.all()

        serializer = BeerTypeSerializer(
            beertypes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            beertype = BeerType.objects.get(pk=pk)
            serializer = BeerTypeSerializer(beertype)
            return Response(serializer.data)
        except BeerType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        beertype = BeerType.objects.create(
          name = request.data["name"],
          )

        serializer = BeerTypeSerializer(
            beertype, context={'request': request}
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        beertype = BeerType.objects.get(pk=pk)
        beertype.name = request.data["name"]

        beertype.save()
        serializer = BeerTypeSerializer(beertype)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            beertype = BeerType.objects.get(pk=pk)
            beertype.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except BeerType.DoesNotExist as ex:
            return Response(
                {'message': ex.args[0]},
                status=status.HTTP_404_NOT_FOUND
            )
class BeerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerType
        fields = ('id', 'name')           
