from django.db import models

from teacher.models import Class

""" CREATE TABLE etudiant ( id INT NOT NULL UNIQUE ,
 nom TEXT NOT NULL , prenom TEXT NOT NULL , mail TEXT NOT NULL, 
 cin TEXT NOT NULL , class varchar(5) NOT NULL  , PRIMARY KEY (id) , 
 CONSTRAINT PK1 FOREIGN KEY (class) REFERENCES classe (idc) ); 
"""

class Student(models.Model):

    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    cin= models.IntegerField(default=00000000)
    photoStud=models.FileField(blank=True, upload_to='studentss/%Y/%m/%D')
    classid=models.ForeignKey(Class, on_delete=models.CASCADE)