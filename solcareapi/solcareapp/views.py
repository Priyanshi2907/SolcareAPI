from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from solcareapp.models import patient,prescription,person,doctor,drug,drug_brand_names,doctor_availability,appointment,jointables,findadoctor,time
from solcareapp.serializer import patientSerializer,prescriptionSerializer,personSerializer,doctorserializer,drugserializer,drugbrandnameserializer,doctor_avalaibilityserializer,appointmentserializer,jointablesserializer,findadoctorserializer,timeserializer
from django.core.files.storage import default_storage
from.import pool
from django.http import HttpResponse
from rest_framework import viewsets
from itertools import chain

# Create your views here.
@csrf_exempt
def patientApi(request, id=0):

        if request.method=='GET':
         Registerpatient = patient.objects.all()
         db, cmd = pool.ConnectionPool()
         q = "select * from demo.solacareapp_patient where patient_id='hms0001pa'"

         cmd.execute(q)
         cmd.fetchall()
         db.close()
         Registerpatient_serializer=patientSerializer(Registerpatient,many=True)
         return JsonResponse(Registerpatient_serializer.data,safe=False)
        elif request.method == 'POST':
         registerpatient_data = JSONParser().parse(request)
         registerpatient_serializer = patientSerializer(data=registerpatient_data)
        if registerpatient_serializer.is_valid():
            registerpatient_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        else:
            return JsonResponse("Failed to Add", safe=False)


def prescriptionApi(request, id=0):
    if request.method == 'GET':
        Prescription = prescription.objects.all()
        prescription_serializer = prescriptionSerializer(Prescription, many=True)
        return JsonResponse(prescription_serializer.data, safe=False)
    elif request.method == 'POST':
        prescription_data = JSONParser().parse(request)
        prescription_serializer = prescriptionSerializer(data=prescription_data)
    if prescription_serializer.is_valid():
        prescription_serializer.save()
        return JsonResponse("Added Successfully", safe=False)
    else:
        return JsonResponse("Failed to Add", safe=False)

def personApi(request,id=0):
    if request.method=='GET':
        Person=person.objects.all()
        PersonSerializer=personSerializer(Person,many=True)
        return JsonResponse(PersonSerializer.data,safe=False)
    elif request.method=='POST':
        Person_data=JSONParser().parse(request)
        Person_serializer=personSerializer(data=Person_data)
    if Person_serializer.is_valid():
       Person_serializer.save()
       return JsonResponse("added successfully",safe=False)
    else:
        return JsonResponse("failed to add", safe=False)


def docApi(request,id=0):
    if request.method=='GET':
        Doc=doctor.objects.all()
        Docserializer=doctorserializer(Doc,many=True)
        return JsonResponse(Docserializer.data,safe=False)
    elif request.method=='POST':
        Doc_data=JSONParser().parse(request)
        Doc_serializer=doctorserializer(data=Doc_data)
    if Doc_serializer.is_valid():
       Doc_serializer.save()
       return JsonResponse("added successfully",safe=False)
    else:
        return JsonResponse("failed to add", safe=False)

def docavaliableApi(request,id=0):
    if request.method=='GET':
        docavaliability=doctor_availability.objects.all()
        docserializer=doctor_avalaibilityserializer(docavaliability,many=True)
        return JsonResponse(docserializer.data,safe=False)
    elif request.method=='POST':
        docavalaibility_data=JSONParser().parse(request)
        docavail_serializer=doctor_avalaibilityserializer(data=docavalaibility_data)
    if docavail_serializer.is_valid():
       docavail_serializer.save()
       return JsonResponse("added successfully",safe=False)
    else:
        return JsonResponse("failed to add", safe=False)

def drugApi(request,id=0):
    if request.method=='GET':
        Drug=drug.objects.all()
        Drugserializer=drugserializer(Drug,many=True)
        return JsonResponse(Drugserializer.data,safe=False)
    elif request.method=='POST':
        drug_data=JSONParser().parse(request)
        drug_serializer=drugserializer(data=drug_data)
    if drug_serializer.is_valid():
       drug_serializer.save()
       return JsonResponse("added successfully",safe=False)
    else:
        return JsonResponse("failed to add", safe=False)


def drugbrandnameApi(request,id=0):
    if request.method=='GET':
        drugbrandname=drug_brand_names.objects.all()
        DrugbrandnameSerializer=drugbrandnameserializer(drugbrandname,many=True)
        return JsonResponse(DrugbrandnameSerializer.data,safe=False)
    elif request.method=='POST':
        drugbrandname_data=JSONParser().parse(request)
        Drugbrandname_Serializer=drugbrandnameserializer(data=drugbrandname_data)
    if Drugbrandname_Serializer.is_valid():
       Drugbrandname_Serializer.save()
       return JsonResponse("added successfully",safe=False)
    else:
        return JsonResponse("failed to add", safe=False)

def appointmentApi(request,id=0):
    if request.method=='GET':
        Appointment=appointment.objects.all()
        AppointmentSerializer=appointmentserializer(Appointment,many=True)
        return JsonResponse(AppointmentSerializer.data,safe=False)

    elif request.method=='POST':
        appointment_data=JSONParser().parse(request)
        appointment_Serializer=appointmentserializer(data=appointment_data)
    if appointment_Serializer.is_valid():
       appointment_Serializer.save()
       return JsonResponse("added successfully",safe=False)
    else:
        return JsonResponse("failed to add", safe=False)

class jointablesAPI(viewsets.ModelViewSet):

    queryset = jointables.objects.raw("select solcareapp_doctor_availability.slmc_reg_no,solcareapp_doctor_availability.day,"
                                      "solcareapp_doctor.* from solcareapp_doctor_availability inner join solcareapp_doctor on"
                                      " solcareapp_doctor_availability.slmc_reg_no=solcareapp_doctor.slmc_reg_no")
    serializer_class=jointablesserializer

class findadoctorAPI(viewsets.ModelViewSet):
    #result_list=[]
    #time = findadoctor.objects.raw("SET @testTime2 = CAST('15:34' AS TIME)")
    #solcareapp_doctor_availability.time_slot_id,
    #"CAST('15:34' AS TIME) BETWEEN CAST(Left(time_slot,5) as TIME) AND"
                                       #" CAST(Right(time_slot,5) as TIME"
                                        

    queryset = findadoctor.objects.raw("select solcareapp_doctor_availability.slmc_reg_no,solcareapp_doctor_availability.day,solcareapp_doctor_availability.time_slot_id,"
                                       "solcareapp_doctor.user_id,solcareapp_doctor.experienced_areas from solcareapp_doctor_availability inner join solcareapp_doctor on "
                                       "solcareapp_doctor_availability.slmc_reg_no=solcareapp_doctor.slmc_reg_no "
                                       "where solcareapp_doctor_availability.day=2 and solcareapp_doctor.experienced_areas='risk managment' and CAST('17:00' AS TIME) BETWEEN CAST(Left(time_slot,5) as TIME) AND"
                                       " CAST(Right(time_slot,5) as TIME)" )
    #and solcareapp_doctor.experienced_areas='risk managment'

    #result_list=list(chain(time,join))
    serializer_class = findadoctorserializer

class timeAPI(viewsets.ModelViewSet):

    queryset =time.objects.raw (
                                 "SELECT time_slot_id FROM demo.solcareapp_doctor_availability"
                                " WHERE  CAST('15:34' AS TIME) BETWEEN CAST(Left(solcareapp_doctor_availability.time_slot,5) as TIME) AND CAST(Right(solcareapp_doctor_availability.time_slot,5) as TIME) ")

    serializer_class = timeserializer
#def finddoctorapi(request):'
 #   try:
  #      doctor_id=request.GET('slmc_reg_no')
   #     timeslotid=request.GET('time_slot_id')
    #    day=request.GET('day')
     #   time=request.GET('time_slot')
      #  db,cmd=pool.ConnectionPool()
       # starttime="select time_slot from solcare_doctor_availibility where timeslot like'%-
        #dict={doctor_id,timeslotid,day,}







