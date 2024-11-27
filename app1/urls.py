from django.urls import path
from . import views

urlpatterns = [

    # URLs para Bautizo
    path('bautizos/', views.BautizoList.as_view(), name='bautizo-list'),  # Lista y creación de bautizos
    path('bautizos/<int:pk>/', views.BautizoDetail.as_view(), name='bautizo-detail'),  # Detalle, actualización y eliminación de un bautizo

    # URLs para Comunion
    path('comuniones/', views.ComunionList.as_view(), name='comunion-list'),  # Lista y creación de comuniones
    path('comuniones/<int:pk>/', views.ComunionDetail.as_view(), name='comunion-detail'),  # Detalle, actualización y eliminación de una comunion

    # URLs para Confirmacion
    path('confirmaciones/', views.ConfirmacionList.as_view(), name='confirmacion-list'),  # Lista y creación de confirmaciones
    path('confirmaciones/<int:pk>/', views.ConfirmacionDetail.as_view(), name='confirmacion-detail'),  # Detalle, actualización y eliminación de una confirmacion

    # URLs para Matrimonio
    path('matrimonios/', views.MatrimonioList.as_view(), name='matrimonio-list'),  # Lista y creación de matrimonios
    path('matrimonios/<int:pk>/', views.MatrimonioDetail.as_view(), name='matrimonio-detail'),  # Detalle, actualización y eliminación de un matrimonio

    # URLs para Sepultura
    path('sepulturas/', views.SepulturaList.as_view(), name='sepultura-list'),  # Lista y creación de sepulturas
    path('sepulturas/<int:pk>/', views.SepulturaDetail.as_view(), name='sepultura-detail'),  # Detalle, actualización y eliminación de una sepultura

    # URLs para Defuncion
    path('defunciones/', views.DefuncionList.as_view(), name='defuncion-list'),  # Lista y creación de defunciones
    path('defunciones/<int:pk>/', views.DefuncionDetail.as_view(), name='defuncion-detail'),  # Detalle, actualización y eliminación de una defuncion
]
