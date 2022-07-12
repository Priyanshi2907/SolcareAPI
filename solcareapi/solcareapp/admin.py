from django.contrib import admin
from.models import patient,prescription,person,doctor,drug,drug_brand_names,doctor_availability
admin.site.register(patient)
admin.site.register(prescription)
admin.site.register(person)
admin.site.register(doctor)
admin.site.register(drug)
admin.site.register(drug_brand_names)
admin.site.register(doctor_availability)

# Register your models here.
