from djongo import models
from bson import ObjectId  # Para manejar ObjectId en el modelo

class Estudiante(models.Model):
    # Campos del estudiante
    _id = models.ObjectIdField()  # Identificador único de MongoDB
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=100, unique=True)
    edad = models.IntegerField()
    id_curso = models.ObjectIdField()  # Referencia al curso
    cargos = models.ArrayField(
        model_fields=[
            ('cargo_id', models.ObjectIdField()),  # ID único para cada cargo
            ('concepto', models.CharField(max_length=255)),
            ('valor', models.DecimalField(max_digits=10, decimal_places=2)),
            ('tipo', models.CharField(max_length=10, choices=[('%', 'Porcentaje'), ('fijo', 'Fijo')])),
            ('mes', models.CharField(max_length=20))
        ]
    )

    def __str__(self):
        return self.nombre
