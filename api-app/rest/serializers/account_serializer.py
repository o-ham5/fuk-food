from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from ..models.account_model import Account, AccountManager


class AccountSerializer(serializers.ModelSerializer):
    # passwordについてoverrideしている
    password = serializers.CharField(write_only=True, required=False)
    # モデルからserializerが自動的に生成される

    class Meta:
        model = Account
        fields = ('account_id', 'username', 'email', 'inyou', 'oshare',
                  'shokuji', 'setsuyaku', 'bias', 'variance', 'password')

    def create(self, validated_data):
        return Account.objects.create_user(request_data=validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance
