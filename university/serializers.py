from rest_framework import serializers
from .models import University, BenefitsBoolean, StateAndPaidInfo, Hostel

class StateAndPaidInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateAndPaidInfo
        fields = ["state_price", "state_point", "state_place", "paid_price", "paid_point", "paid_place"]

class BenefitsBooleanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitsBoolean
        fields = ["state_univers", "arm_univers", "tech_univers", "humanitarian_univers", "hostel_univers"]

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ["name", "date", "address", "link_address"]

class UniversitySerializer(serializers.ModelSerializer):
    info_stateandpaid = StateAndPaidInfoSerializer(many=False, read_only=True)
    benefits_univers = BenefitsBooleanSerializer(many=False, read_only=True)

    class Meta:
        model = University
        fields = '__all__'
        depth = 1

class UniversityOneSerializer(serializers.ModelSerializer):
    info_stateandpaid = StateAndPaidInfoSerializer(many=False, read_only=True)
    benefits_univers = BenefitsBooleanSerializer(many=False, read_only=True)
    hostel_univers = HostelSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = '__all__'
        depth = 1
