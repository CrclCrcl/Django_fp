from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField("Imię",max_length=25)
    surname = models.CharField("Nazwisko",max_length=25)
    mail_address = models.CharField("E-mail",max_length=30)
    message = models.TextField("Wiadomość",max_length=240)

    class Meta:
        db_table = "Student"