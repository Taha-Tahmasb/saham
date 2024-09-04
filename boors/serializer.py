from rest_framework.serializers import ModelSerializer
from .models import Investment



class InvestSerializer(ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'