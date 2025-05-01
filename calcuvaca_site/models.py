from django.db import models

class Employ(models.Model):
    name = models.CharField('Nombre del Empleado', max_length=255)
    entry_date = models.DateField('Fecha de Ingreso')
    created_at = models.DateField('Fecha de Creación del registro')
    modified_at = models.DateField('Fecha de Ultima Modificación')

    def __str__(self):
        return f"{self.name}"

class VacationTaken(models.Model):
    employ = models.ForeignKey(Employ, on_delete=models.CASCADE)
    vacation_days = models.IntegerField("Cantidad de días tomados")
    vacation_date = models.DateField("Fecha de solicitud de vacaciones")
