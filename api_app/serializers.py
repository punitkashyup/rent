from rest_framework import serializers
from .models import rent
from django.contrib.auth.models import User

class rentSerializer(serializers.ModelSerializer):
    # id=serializers.PrimaryKeyRelatedField(read_only=True)
    rent_date = serializers.DateField(format="%d-%m-%Y", read_only=True)
    rentmonth = serializers.CharField()
    rent_amount = serializers.FloatField()
    bijli_bill = serializers.FloatField()
    other_amount = serializers.FloatField()
    other_commnet = serializers.CharField(max_length=200)

    class Meta:
        model = rent
        fields = ('__all__')

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user