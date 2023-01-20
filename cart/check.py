from django.http import HttpResponse
from rest_framework.response import Response


def Home(request):
    data = request.data
    print(data)
    return HttpResponse("hannan")
