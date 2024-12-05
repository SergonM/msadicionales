from djongo import models

class Cargo(models.Model):
    cargo_id = models.ObjectIdField()  # El identificador único del cargo
    concepto = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('%', 'Porcentaje'), ('fijo', 'Fijo')])
    mes = models.CharField(max_length=20)

    class Meta:
        abstract = True

class Estudiante(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # El identificador único de MongoDB
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20)  # Clave única, pero no primaria
    id_curso = models.CharField(max_length=20)
    edad = models.IntegerField()
    cargos = models.ArrayField(
        model_container=Cargo,  # Aquí estamos diciendo que cada elemento en 'cargos' es un objeto Cargo
        default=list,  # Lista vacía por defecto si no se proporcionan datos
    )

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

    class Meta:
        db_table = 'estudiantes_estudiante'
