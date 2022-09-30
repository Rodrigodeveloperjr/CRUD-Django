from django.forms import model_to_dict
from rest_framework.views import APIView, Request, Response, status
from users.services.required_data import required_data
from users.services.required_keys import required_keys
from django.core.exceptions import ValidationError

from .models import Users

# Create your views here.
class UsersView(APIView):

    def get(self, request: Request) -> Response:

        users = Users.objects.all()

        users_dict = [model_to_dict(user) for user in users]

        return Response(users_dict)

    def post(self, request: Request) -> Response:

        try:
            required_keys(request.data)
            required_data(request.data)

            user = Users.objects.create(**request.data)
        
        except KeyError:
            return Response({
                "name": "missing key",
                "email": "missing key",
                "password": "missing key",
                "isAdm": "missing key"
            }, status.HTTP_404_NOT_FOUND)
        
        except ValidationError:
            return Response({
                "name": "must be a str",
                "email": "must be a str",
                "password": "must be a str",
                "isAdm": "must be a bool"
            }, status.HTTP_404_NOT_FOUND)

        user_dict = model_to_dict(user)

        return Response(user_dict, status.HTTP_201_CREATED)


class UsersViewId(APIView):

    def get(self, request: Request, user_id: int) -> Response:

        try:
            user = Users.objects.get(id=user_id)

        except Users.DoesNotExist:

            return Response({ "message": "User not found" }, status.HTTP_404_NOT_FOUND)

        user_dict = model_to_dict(user)

        return Response(user_dict)

    def patch(self, request: Request, user_id: int) -> Response:
        
        try:
            user = Users.objects.get(id=user_id)
        
        except Users.DoesNotExist:
            
            return Response({ "message": "User not found" }, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():

            setattr(user, key, value)
        
        user.save()
        user_dict = model_to_dict(user)

        return Response(user_dict)

    def delete(self, request: Request, user_id: int) -> Response:
        
        try:
            user = Users.objects.get(id=user_id)

        except Users.DoesNotExist:

            return Response({ "message": "User not found" }, status.HTTP_404_NOT_FOUND)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
