from django.db import models

# Modelo Bautizo
class Bautizo(models.Model):
    # Información personal del bautizado
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_bautizo = models.DateField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    lugar_nacimiento = models.CharField(max_length=100, blank=True, null=True)

    # Información de los padres
    padre = models.CharField(max_length=100, blank=True, null=True)
    madre = models.CharField(max_length=100, blank=True, null=True)

    # Información de los padrinos y celebrante
    padrinos = models.CharField(max_length=100, blank=True, null=True)
    celebrante = models.CharField(max_length=100, blank=True, null=True)

    # Registro eclesiástico
    ano_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    tomo_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    pagina_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    acta_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)

    # Registro civil
    ano_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    tomo_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    pagina_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    acta_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    cedula_registro_civil = models.CharField(max_length=100, blank=True, null=True)

    # Nota adicional
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Bautizo de {self.nombre or 'Desconocido'}"


# Modelo Comunion
class Comunion(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    padre = models.CharField(max_length=100, blank=True, null=True)
    madre = models.CharField(max_length=100, blank=True, null=True)
    celebrante = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateField(null=True, blank=True)
    ano_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    tomo = models.CharField(max_length=100, blank=True, null=True)
    pagina = models.CharField(max_length=100, blank=True, null=True)
    acta = models.CharField(max_length=100, blank=True, null=True)
    ano_registro_civil = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo
    datos_registro_civil_acta = models.CharField(max_length=100, blank=True, null=True)
    datos_registro_civil_tomo = models.CharField(max_length=100, blank=True, null=True)
    datos_registro_civil_pagina = models.CharField(max_length=100, blank=True, null=True)
    fecha_emision = models.DateField(null=True, blank=True)
    parroco = models.CharField(max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Comunión de {self.nombre or 'Desconocido'}"


# Modelo Confirmación
class Confirmacion(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    fecha_confirmacion = models.DateField(null=True, blank=True)
    padre = models.CharField(max_length=255, blank=True, null=True)
    madre = models.CharField(max_length=255, blank=True, null=True)
    celebrante = models.CharField(max_length=255, blank=True, null=True)

    # Registro eclesiástico
    ano_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    tomo_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    pagina_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    acta_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)

    # Registro civil
    ano_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    tomo_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    pagina_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    acta_registro_civil = models.CharField(max_length=100, blank=True, null=True)

    # Nota adicional
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Confirmación de {self.nombre or 'Desconocido'}"


# Modelo Matrimonio
class Matrimonio(models.Model):
    conyuges = models.CharField(max_length=511, blank=True, null=True)
    fecha_matrimonio = models.DateField(null=True, blank=True)
    testigos = models.CharField(max_length=255, blank=True, null=True)
    padrinos = models.CharField(max_length=255, blank=True, null=True)
    celebrante = models.CharField(max_length=255, blank=True, null=True)

    # Registro eclesiástico
    ano_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    tomo_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    pagina_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    acta_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)

    # Registro civil
    ano_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    tomo_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    pagina_registro_civil = models.CharField(max_length=100, blank=True, null=True)
    acta_registro_civil = models.CharField(max_length=100, blank=True, null=True)

    # Nota adicional
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Matrimonio de {self.conyuges or 'Desconocido'}"


# Modelo Defuncion
class Defuncion(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(default=0)
    lugar_fallecimiento = models.CharField(max_length=255, blank=True, null=True)
    causa_fallecimiento = models.CharField(max_length=255, blank=True, null=True)
    parroco = models.CharField(max_length=255, blank=True, null=True)
    ano_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    tomo = models.CharField(max_length=255, blank=True, null=True)
    pagina = models.CharField(max_length=255, blank=True, null=True)
    acta = models.CharField(max_length=100, blank=True, null=True)
    datos_registro_civil_ano = models.IntegerField(default=2024)
    datos_registro_civil_tomo = models.CharField(max_length=255, blank=True, null=True)
    datos_registro_civil_pagina = models.CharField(max_length=255, blank=True, null=True)
    datos_registro_civil_acta = models.CharField(max_length=255, blank=True, null=True)
    fecha_emision_certificado_defuncion = models.DateField(null=True, blank=True)
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Defunción registrada en {self.ano_registro_eclesiastico or 'Desconocido'}"


# Modelo Sepultura
class Sepultura(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(default=0)
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    motivo_fallecimiento = models.CharField(max_length=255, blank=True, null=True)
    parroco = models.CharField(max_length=255, blank=True, null=True)
    fecha_sepultura = models.DateField(null=True, blank=True)
    ano_registro_eclesiastico = models.CharField(max_length=100, blank=True, null=True)
    tomo = models.CharField(max_length=255, blank=True, null=True)
    pagina = models.CharField(max_length=255, blank=True, null=True)
    acta = models.CharField(max_length=100, blank=True, null=True)
    datos_registro_civil_ano = models.IntegerField(default=2024)
    datos_registro_civil_tomo = models.CharField(max_length=255, blank=True, null=True)
    datos_registro_civil_pagina = models.CharField(max_length=255, blank=True, null=True)
    datos_registro_civil_acta = models.CharField(max_length=255, blank=True, null=True)
    fecha_emision_certificado_sepultura = models.DateField(null=True, blank=True)
    parroco_certificado = models.CharField(max_length=255, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sepultura de {self.estado_civil or 'Desconocido'}"
