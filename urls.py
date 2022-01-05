from rest_framework import routers
from.views import  StudentCurd
from django.urls import include,path



# app_name='itemapp'


router=routers.DefaultRouter()
router.register(r'students',StudentCurd,basename="students")
urlpatterns=[

    path("",include(router.urls))
]
