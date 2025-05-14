from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from user_app.models import *
from .serializers import *

"""Only the admins can perform actions in the system (defined in the default permission classes in settings)"""

@api_view(['GET'])
def get_users(request):
    users = MyUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

"""
This can be used if the actions need to be performed by a logged in user: Permission class decorator(IsAuthenticated) will be added to the respective functions and the credentials from the logged in user will then be used to perform the actions
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user=authenticate(username=username, password=password, is_staff=True, is_superuser=True)

    if user:
        return Response({"Logged-in":"You have logged in successfully"})
    return Response({"error":"wrong credentials"},status=401)
"""

@api_view(['POST'])
def change_password(request,id):
    try:
        user=MyUser.objects.get(id=id)
    except MyUser.DoesNotExist:
        return Response({"Error":"User not found"},status=404)

    serializer=ChangePasswordSerializer(data=request.data, context={"user":user})
    if serializer.is_valid():
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"Success":"Password updated successfully"}, status=200)

    return Response(serializer.errors, status=400)

@api_view(['PATCH'])
def update_user_details(request,id):
    try:
        user=MyUser.objects.get(id=id)
    except MyUser.DoesNotExist:
        return Response({"User":"User does not exist"},status=404)

    serializer=UpdateUserDetails(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_user(request,id):
    try:
        user=MyUser.objects.get(id=id)
        user.delete()
        return Response({"Deletion": "User deleted successfully"}, status=204)
    except MyUser.DoesNotExist:
        return Response({"User":"User does not exist"},status=404)