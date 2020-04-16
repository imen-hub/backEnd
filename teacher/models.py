from django.db import models

"""CREATE TABLE classes ( idc varchar(40) NOT NULL  ,
 emploi TEXT NOT NULL , PRIMARY KEY (idc) );
 CREATE TABLE enseignant ( nom TEXT NOT NULL  REFERENCES classe (idc) , 
prenom TEXT NOT NULL ,
 cin int(12) NOT NULL PRIMARY KEY ,
  mail TEXT NOT NULL, tel int(8) NOT NULL , 
  classid varchar(40) );
"""
class Class (models.Model):
    idc= models.CharField(max_length=60,primary_key=True)
    emploi=models.FileField(blank=True, upload_to='emplois/%Y/%m/%D')


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    cin= models.IntegerField(default=00000000)
    photoTeach=models.FileField(blank=True, upload_to='teachers/%Y/%m/%D')
    classid=models.ForeignKey(Class, on_delete=models.CASCADE)
