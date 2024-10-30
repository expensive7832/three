from rest_framework import serializers

from .models import purchase
from rest_framework.exceptions import ValidationError

class purchaseserializer(serializers.ModelSerializer):
    class Meta:
        model = purchase
        fields = '__all__'

    def validate(self, attrs):
        ref_code = attrs['ref_code']
        phone_number = attrs['phone_number']
        message = attrs['message']
        mobile_network = attrs['mobile_network']
        
        if ref_code == "" or phone_number == "" or message == "" or mobile_network == "":
            raise ValidationError("All Fields Are Required")
        elif len(ref_code) < 16:
            raise ValidationError("ref_code must be minimum pf 16 alphanumeric")

        else:
            return attrs