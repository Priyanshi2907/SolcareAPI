from rest_framework import serializers
from solcareapp.models import patient,prescription,person,doctor,drug,drug_brand_names,doctor_availability,appointment,jointables,findadoctor,time
class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model=patient
        fields=("patient_id","person_id","drug_allergies_and_reactions")

class prescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=prescription
        fields=("prescription_id","patient_id","consultant_id","date","drugs_dose","tests")


class personSerializer(serializers.ModelSerializer):
    class Meta:
        model=person
        fields='__all__'


class doctorserializer(serializers.ModelSerializer):
    class Meta:
        model=doctor
        fields='__all__'

class drugserializer(serializers.ModelSerializer):
    class Meta:
        model=drug
        fields='__all__'

class doctor_avalaibilityserializer(serializers.ModelSerializer):
    class Meta:
        model=doctor_availability
        fields='__all__'

class drugbrandnameserializer(serializers.ModelSerializer):
    class Meta:
        model=drug_brand_names
        fields='__all__'

class appointmentserializer(serializers.ModelSerializer):
    class Meta:
        model=appointment
        fields='__all__'
class jointablesserializer(serializers.ModelSerializer):
     class Meta:
         model=jointables
         fields=("day","slmc_reg_no", "user_id", "education", "training", "experienced_areas", "experience", "achievements", "channelling_fee")

class findadoctorserializer(serializers.ModelSerializer):
    class Meta:
        model=findadoctor
        fields=('slmc_reg_no','day','experienced_areas' ,'user_id','time_slot_id','time_slot')

class timeserializer(serializers.ModelSerializer):
    class Meta:
        model=time
        fields=('__all__')


