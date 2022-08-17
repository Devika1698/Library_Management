from django.db import models
from datetime import datetime,timedelta

class Student_signup(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    enroll=models.CharField(max_length=30)
    branch=models.CharField(max_length=50)
    #used in issue book
    def __str__(self):
        return self.fname+'['+str(self.enroll)+']'
    @property
    def get_name(self):
        return self.fname
    @property
    def getuserid(self):
        return self.id


class Admin_signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class BookModel(models.Model):
    catchoice=[
        ('education','Education'),
        ('entertainment','Entertainment'),
        ('comics','Comics'),
        ('biography','Biography'),
        ('history','History'),
    ]
    bookname=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    def __str__(self):
        return str(self.bookname)+"["+str(self.isbn)+"]"


def get_expiry():
    return datetime.today()+timedelta(days=15)
class IssueBook(models.Model):
    enroll=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.enroll
