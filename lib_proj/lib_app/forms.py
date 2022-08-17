from django import forms
from .models import *

class StudentForm(forms.ModelForm):  #django modelform is a class that is used to directly convert a model into a django form
    class Meta:     #meta class is basically the inner class of your model class. model meta is used to change behaviour of ur model/form
        model=Student_signup
        fields="__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin_signup
        fields="__all__"

class Student_login(forms.ModelForm):
    class Meta:
        model=Student_signup
        fields=['uname','password']

class Admin_login(forms.ModelForm):
    class Meta:
        model=Admin_signup
        fields=['uname','password']

class BookForm(forms.ModelForm):
    class Meta:
        model=BookModel
        fields="__all__"

class IssuedBookForm(forms.Form):
     isbn2=forms.ModelChoiceField(queryset=BookModel.objects.all(),empty_label="Name and isbn",to_field_name="isbn",label="Name and Isbn")
     enrollment2=forms.ModelChoiceField(queryset=Student_signup.objects.all(),empty_label="Name and enrollment",to_field_name="enroll",label="Name and Enrollment")

class ContactusForm(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    message=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows':5,'cols':30}))

