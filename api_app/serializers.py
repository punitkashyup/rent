from rest_framework import serializers
from .models import rent
from .models import user
from rest_framework.validators import UniqueValidator

class rentSerializer(serializers.ModelSerializer):
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    rent_date = serializers.DateField(format="%d-%m-%Y", read_only=True)
    rentmonth = serializers.CharField()
    # rentmonth = serializers.CharField(source='get_rentmonth_display')
    rent_amount = serializers.FloatField()
    bijli_bill = serializers.FloatField()
    other_amount = serializers.FloatField()
    other_commnet = serializers.CharField(max_length=200)

    class Meta:
        model = rent
        fields = ('__all__')

class userSerializer(serializers.ModelSerializer):
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    user_name = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=user.objects.all())])
    user_email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    user_password = serializers.CharField(max_length=200, style={'input_type': 'password'})

    class Meta:
        model = user
        fields = ('__all__')