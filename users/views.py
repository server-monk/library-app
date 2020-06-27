from django.contrib.auth import authenticate, get_user_model, hashers

from rest_framework import generics, status, permissions
from rest_framework.response import Response

import users.serializers as serializers

CustomUser = get_user_model()

class RegisterView(generics.CreateAPIView):
    '''View to create a new `user` or `admin`.'''
    queryset = CustomUser.objects.all()
    serializer_class = serializers.RegistrationSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        if request.data['password'] == request.data['confirm_password']:
            serializer = serializers.RegistrationSerializer(data=request.data)
        else:
            return Response({'error': 'Password mismatch'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveAPIView):
    '''Returns currently logged in user info.'''
    serializer_class = serializers.UserSerializer

    def get(self, request):
        try:
            queryset = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserSerializer(queryset, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    '''Allows password change for currently looged in user.'''
    serializer_class = serializers.ChangePasswordSerializer

    def post(self, request):
        queryset = CustomUser.objects.get(id=request.user.id)
        
        if hashers.check_password(request.data['password'], queryset.password):
            if request.data['new_password'] == request.data['confirm_password']:
                serializer = serializers.ChangePasswordSerializer(data=request.data)

                if serializer.is_valid(raise_exception=True):
                    serializer.update(queryset, request.data)
                    return Response({'message': 'Password changed successfully!'}, status=status.HTTP_202_ACCEPTED)

            return Response(data={'error': 'Password mismatch!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(data={'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
