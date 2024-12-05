from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Estudiante
import json
from bson import ObjectId
from django.utils.decorators import method_decorator

#@method_decorator(csrf_exempt, name='dispatch')
class CargosListView(View):
    def get(self, request):
        # Listar todos los estudiantes y sus cargos
        estudiantes = Estudiante.objects.all()
        print(estudiantes)
        data = [{"id": str(estudiante._id), "nombre": estudiante.nombre,
                 "codigo": estudiante.codigo, "cargos": estudiante.cargos} for estudiante in estudiantes]
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        try:
            estudiante = Estudiante.objects.get(codigo=data['codigo_estudiante'])  # Buscar el estudiante por código
            # Crear un nuevo cargo con un nuevo cargo_id
            nuevo_cargo = {
                "cargo_id": ObjectId(),  # Generar un nuevo ObjectId para el cargo
                "concepto": data['concepto'],
                "valor": data['valor'],
                "tipo": data['tipo'],
                "mes": data['mes']
            }
            estudiante.cargos.append(nuevo_cargo)  # Agregar el cargo al arreglo de cargos
            estudiante.save()  # Guardar el estudiante con el nuevo cargo
            return JsonResponse({"message": "Cargo agregado exitosamente"}, status=201)
        except Estudiante.DoesNotExist:
            return JsonResponse({"message": "Estudiante no encontrado"}, status=404)


#@method_decorator(csrf_exempt, name='dispatch')
class CargosDetailView(View):
    def get(self, request, id):
        try:
            estudiante = Estudiante.objects.get(_id=id)
            data = {
                "id": str(estudiante._id),
                "nombre": estudiante.nombre,
                "codigo": estudiante.codigo,
                "edad": estudiante.edad,
                "id_curso": str(estudiante.id_curso),
                "cargos": estudiante.cargos
            }
            return JsonResponse(data)
        except Estudiante.DoesNotExist:
            return JsonResponse({"message": "Estudiante no encontrado"}, status=404)

    def put(self, request, id):
        data = json.loads(request.body)
        try:
            estudiante = Estudiante.objects.get(_id=id)
            cargo_id = ObjectId(data['cargo_id'])  # Convertir cargo_id a ObjectId
            for cargo in estudiante.cargos:
                if cargo['cargo_id'] == cargo_id:
                    cargo['concepto'] = data.get('concepto', cargo['concepto'])
                    cargo['valor'] = data.get('valor', cargo['valor'])
                    cargo['tipo'] = data.get('tipo', cargo['tipo'])
                    cargo['mes'] = data.get('mes', cargo['mes'])
                    break
            estudiante.save()  # Guardar el estudiante con el cargo actualizado
            return JsonResponse({"message": "Cargo actualizado exitosamente"})
        except Estudiante.DoesNotExist:
            return JsonResponse({"message": "Estudiante no encontrado"}, status=404)

    @csrf_exempt
    def delete(self, request, id):
        data = json.loads(request.body)
        try:
            estudiante = Estudiante.objects.get(_id=id)
            cargo_id = ObjectId(data['cargo_id'])  # Convertir cargo_id a ObjectId
            estudiante.cargos = [cargo for cargo in estudiante.cargos if cargo['cargo_id'] != cargo_id]
            estudiante.save()  # Guardar los cambios
            return JsonResponse({"message": "Cargo eliminado exitosamente"})
        except Estudiante.DoesNotExist:
            return JsonResponse({"message": "Estudiante no encontrado"}, status=404)
