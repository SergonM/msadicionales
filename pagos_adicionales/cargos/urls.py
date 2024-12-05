from django.urls import path
from .views import CargosListView, CargosDetailView

urlpatterns = [
    path('cargos/', CargosListView.as_view(), name='cargos_list_create'),
    path('cargos/<str:id>/', CargosDetailView.as_view(), name='cargos_detail'),
]
