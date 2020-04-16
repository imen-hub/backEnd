from django.db import models
from teacher.models import Teacher , Class
from student.models import Student

"""class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    cin= models.IntegerField(default=00000000)
    classid=models.ForeignKey(Class, on_delete=models.CASCADE)
    
CREATE TABLE rattrapage ( numclasse varchar(20) NOT NULL  ,
 nomensign varchar(10) NOT NULL REFERENCES enseignant(nom) , 
 prenomensign varchar(20) NOT NULL REFERENCES enseignant(prenom) , 
 salle INT , date varchar(40)  NOT NULL , time varchar(10), matiere TEXT NOT NULL , 
   PRIMARY KEY (date,`numclasse`,`salle`,`time`) , 
CONSTRAINT PK7 FOREIGN KEY (numclasse) REFERENCES classe (idc) );"""

class CatchingUp(models.Model):
    numClass = models.ForeignKey(Class, on_delete=models.CASCADE )
    Teach =models.ForeignKey(Teacher, on_delete=models.CASCADE)
    roomNumber=models.IntegerField()
    date= models.DateField()
    time= models.TimeField()
    matiere= models.CharField(max_length=60)

"""  CREATE TABLE reunion( date varchar(40) NOT NULL , time varchar(10) , 
sujet TEXT NOT NULL , PRIMARY KEY (date,`heure`)); """

class Meeting(models.Model):
    date= models.DateField()
    time= models.TimeField()
    topic= models.CharField(max_length=60)


"""  CREATE TABLE resultat ( id etudiant INT NOT NULL REFERENCES etudiant (id) , 
nometud TEXT NOT NULL REFERENCES etudiant(nom) , 
prenometud TEXT NOT NULL REFERENCES etudiant (prenom) , 
moyenne FLOAT NOT NULL , 
observations TEXT , 
fiche notes TEXT NOT NULL  );"""

class Result(models.Model):
    idR=models.ForeignKey(Student, on_delete=models.CASCADE )
    Moyenne=models.FloatField(00.00) 
    Observations=models.CharField(max_length=100)
    listNotes=models.CharField(max_length=100)


"""  evenement ( date varchar(40) NOT NULL ,`time` varchar(10) 
 ,`sujet` TEXT NOT NULL , PRIMARY KEY (date,`time`) );"""

class Events(models.Model):
    date= models.DateField()
    time= models.TimeField()
    topic= models.CharField(max_length=60)