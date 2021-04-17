from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth import get_user_model
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets, status
from accounts.serializers import UserSerializer
from accounts.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        print(self.request.user)
        data = UserSerializer(self.request.user).data

        return Response(data=data, status=status.HTTP_200_OK)



@csrf_exempt
def register_view(request):
    if (request.method == 'POST'):
        body = json.loads(request.body)
        email = body["email"]
        password = body["password"]
        first_name = body["firstName"]
        last_name = body["lastName"]
        get_user_model().objects.create_user(email, first_name, last_name, password)
    return JsonResponse({"email": email, "first_name": first_name, "last_name": last_name, "password": password})
