from djongo import models
from bson import ObjectId  # Para manejar ObjectId en el modelo

class Cargo(models.Model):
    cargo_id = models.ObjectIdField()  # ID único para cada cargo
    concepto = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('%', 'Porcentaje'), ('fijo', 'Fijo')])
    mes = models.CharField(max_length=20)

    class Meta:
        abstract = True  # Necesario para `ArrayField`

class Estudiante(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # El identificador único de MongoDB
    cargos = models.ArrayField(
        model_container=Cargo,  # Define que los elementos son del tipo `Cargo`
    )

    def __str__(self):
        return str(self._id)  # Solo usamos el `_id` para identificar

