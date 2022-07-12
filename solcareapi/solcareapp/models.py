from django.db import models

# Create your models here.
class patient(models.Model):
    patient_id=models.CharField(max_length=10,primary_key=True)
    person_id=models.CharField(max_length=15)
    drug_allergies_and_reactions=models.CharField(max_length=500)

class prescription(models.Model):
     prescription_id=models.CharField(max_length=10,primary_key=True)
     patient_id=models.CharField(max_length=10)
     consultant_id=models.CharField(max_length=20)
     date=models.DateField()
     drugs_dose=models.CharField(max_length=300)
     tests=models.CharField(max_length=100)


class person(models.Model):
    person_id=models.CharField(max_length=15,primary_key=True)
    user_id=models.CharField(max_length=10)
    nic=models.CharField(max_length=10)
    gender=models.CharField(max_length=1)
    date_of_birth=models.DateField()
    address=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    nationality=models.CharField(max_length=20)
    religion=models.CharField(max_length=20)

class drug(models.Model):
    drug_id=models.CharField(max_length=20,primary_key=True)
    drug_name=models.CharField(max_length=20)
    dangerous_drug=models.IntegerField()

class doctor(models.Model):
    slmc_reg_no=models.CharField(max_length=20,primary_key=True)
    user_id=models.CharField(max_length=10)
    education=models.CharField(max_length=100)
    training=models.CharField(max_length=100)
    experienced_areas=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    achievements=models.CharField(max_length=100)
    channelling_fee=models.IntegerField(11)

class doctor_availability(models.Model):
     time_slot_id=models.CharField(max_length=20,primary_key=True)
     slmc_reg_no=models.CharField(max_length=20)
     day=models.IntegerField()
     time_slot=models.CharField(max_length=40)
     current_week_appointments=models.IntegerField()
     next_week_appointments=models.IntegerField()


class drug_brand_names(models.Model):
    brand_id=models.CharField(max_length=20,primary_key=True)
    brand_name=models.CharField(max_length=20)
    generic_name=models.CharField(max_length=20)
    drug_type=models.CharField(max_length=20)
    drug_unit=models.CharField(max_length=20)
    unit_price=models.IntegerField()

class appointment(models.Model):
    appointment_id=models.CharField(max_length=15,primary_key=True)
    date=models.DateTimeField()
    info=models.CharField(max_length=100)
    patient_id=models.CharField(max_length=10)
    bill_id=models.CharField(max_length=20)
    slmc_reg_no=models.CharField(max_length=20)
    cancelled=models.IntegerField()

class jointables(models.Model):
    slmc_reg_no=models.CharField(max_length=20)
    day=models.IntegerField(primary_key=True)
    experienced_areas=models.CharField(max_length=20)
    user_id = models.CharField(max_length=10)
    education = models.CharField(max_length=100)
    training = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    achievements = models.CharField(max_length=100)
    channelling_fee = models.IntegerField()



class findadoctor(models.Model):
    slmc_reg_no = models.CharField(max_length=20)
    day = models.IntegerField(primary_key=True)
    experienced_areas = models.CharField(max_length=20)
    user_id = models.CharField(max_length=10)
    time_slot_id=models.CharField(max_length=20)
    time_slot = models.CharField(max_length=40)


class time(models.Model):

    time_slot_id=models.CharField(max_length=20,primary_key=True)
    time_slot=models.CharField(max_length=40)





