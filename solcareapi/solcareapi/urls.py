"""solcareapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from solcareapp import views

router=DefaultRouter()
router.register("jointables",views.jointablesAPI)
router.register("findadoctor",views.findadoctorAPI)
#router.register("time",views.timeAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/',views.patientApi),
    path('prescription/',views.prescriptionApi),
    path('person/',views.personApi),
    path('doctor/',views.docApi),
    path('doctoravail/', views.docavaliableApi),
    path('drug/', views.drugApi),
    path('drugbrandname/', views.drugbrandnameApi),
    path('appointment/', views.appointmentApi),
    path('',include(router.urls)),
    path('', include(router.urls)),
   # path('',include(router.urls))

]
