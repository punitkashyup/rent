from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import rentSerializer
from .models import rent
from .serializers import userSerializer
from .models import user
from django.shortcuts import get_object_or_404

################################RentAPI######################################
class rentViews(APIView):
    def post(self, request):
        serializer = rentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = rent.objects.get(id=id)
            serializer = rentSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = rent.objects.all()
        serializer = rentSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = rent.objects.get(id=id)
        serializer = rentSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(rent, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
###############################UserAPI#######################################
class userViews(APIView):
    def post(self, request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = user.objects.get(id=id)
            serializer = userSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = user.objects.all()
        serializer = userSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = user.objects.get(id=id)
        serializer = userSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(user, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})