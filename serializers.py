from rest_framework.serializers import ModelSerializer
from.models import test
class testSerializers(ModelSerializer):
    class Meta:
        model=test
        fields=['name','costperitem','stockquantity','volume']