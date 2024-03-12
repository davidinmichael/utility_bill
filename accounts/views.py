from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class AccountView(APIView):

    def get(self, request):
        context = {
            "name": "David",
            "stack": "Backend",
        }
        return render(request, "accounts/welcome.html", context)