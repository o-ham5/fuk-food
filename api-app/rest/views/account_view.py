from django.contrib.auth import authenticate
from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from django.db import transaction
from django.http import HttpResponse, Http404

from rest_framework import status, viewsets, filters
from rest_framework.views import APIView

from ..serializers.account_serializer import AccountSerializer
from ..models.account_model import Account, AccountManager

# ユーザ作成のView(POST)


class AuthRegister(generics.CreateAPIView):
    # 以下の3つはcreateAPIViewに必ず指定する必要のある変数。
    permission_classes = (permissions.AllowAny,)
    # このクエリセットをベースとして何かを行う
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ユーザ情報取得のView(GET)


class AuthInfoGetView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, format=None):
        return Response(data={
            'account_id': request.user.account_id,
            'username': request.user.username,
            'email': request.user.email,
        },
            status=status.HTTP_200_OK)

# ユーザ情報更新のView(PUT)


class AuthInfoUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    lookup_field = 'email'
    queryset = Account.objects.all()

    def get_object(self):
        try:
            # クエリセットから特定のオブジェクトを抽出する。
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Account.DoesNotExist:
            raise Http404

# ユーザ削除のView(DELETE)


class AuthInfoDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    lookup_field = 'email'
    queryset = Account.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Account.DoesNotExist:
            raise Http404