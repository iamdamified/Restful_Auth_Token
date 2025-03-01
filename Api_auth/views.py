from django.shortcuts import render
from Authentication.models import Post
from .serializers import PostSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.

@api_view(["GET"])
def api_home(request):
    all_post = Post.objects.all()
    serialized_data = PostSerializers(all_post, many=True)
    return Response(serialized_data.data)


@api_view(["GET"])
def api_post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    serialized_detail = PostSerializers(post_detail)
    return Response(serialized_detail.data)

@api_view(["PUT"])
def api_post_update(request, id):
    post_detail = Post.objects.get(id=id)
    update_data = request.data
    serialized_update = PostSerializers(post_detail, data=update_data, partial=True)
    if serialized_update.is_valid():
        serialized_update.save()
        return Response(serialized_update.data)
    else:
        return Response({"Error": "You entered the wrong data"})
    

@api_view(["DELETE"])
def api_post_delete(request, id):
    post_detail = Post.objects.get(id=id) # A query set
    post_detail.delete() #delete
    return Response({"Success": "Post has been successfully deleted"})


@api_view(["POST"])
def api_post_create(request):
    new_data = PostSerializers(data=request.data)
    if new_data.is_valid():
        new_data.save()
        return Response({'message': 'Data created!'}, status=status.HTTP_201_CREATED)
        # return Response(new_data.data)