from itertools import count
import json
from .models import Token
from .serializers import TokenSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .libs.hash_generator.generator import genHash
from .libs.tx_handler.tx_handler import tx_create, tx_total_supply

class TokenList(APIView):
    def get(self, request, format=None):
        tokens = Token.objects.all()
        serializer = TokenSerializer(tokens, many=True)
        return Response(serializer.data)

class TotalSupply(APIView):
    def get(self, request, format=None):
        count = tx_total_supply()
        return Response(json.dumps({'result': count}))

class TokenCreate(APIView):

    def post(self, request, format=None):
        request.data['unique_hash'] = genHash()
        request.data['tx_hash'] = tx_create(request.data).hex()
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.save()
            return Response(TokenSerializer(token).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    