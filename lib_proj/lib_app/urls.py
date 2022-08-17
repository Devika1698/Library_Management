from django.urls import include,path
from .views import *

urlpatterns = [
    path('', home,name='library'),
    path('admin1/', admin,name='library'),
    path('student/', student,name='library'),
    path('stusign/', stusign,name='library'),
    path('adsign/', adsign,name='library'),
    path('stulog/', stulog,name='library'),
    path('adlog/', adlog,name='library'),
    path('addbook/', addbook,name='library'),
    path('viewbook/', view_book,name='library'),
    path('edit/<int:id>', edit_book,name='library'),
    path('delete/<int:id>', delete_book,name='library'),
    path('issuebook/', issue_book,name='library'),
    path('viewissuedbook/', view_issuedbook,name='library'),
    path('viewissuedbookstud/', viewissuedbookstud,name='library'),
    path('viewstudent/', view_student,name='library'),
    path('contactus/', contactus,name='library'),
    path('aboutus/', aboutus,name='library'),
]
