import email
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class SobreNosotros(models.Model):
    descripcion = models.TextField("Descripción", max_length=1000)
    foto = models.ImageField("Foto", upload_to="uploads/sobreNosotros/img")

    def __str__(self):
        return f"Sección Sobre Nosotros"

    def save(self, *args, **kwargs):
        if not self.pk and SobreNosotros.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            ValidationError
            raise ValidationError(
                'Solo puede existir un objeto de este tipo.')
        return super(SobreNosotros, self).save(*args, **kwargs)

    def clean(self):
        if SobreNosotros.objects.exists() and not self.pk:
            raise ValidationError(
                "Solo puede existir un objeto de este tipo, por favor modifica el objeto en lugar de crear otro.")

    class Meta:
        verbose_name = ("Sección Sobre Nosotros")
        verbose_name_plural = ("Sección Sobre Nosotros")


class Persona(models.Model):

    nombre = models.CharField("Nombre", max_length=100)
    descripcion = models.TextField("Descripción", max_length=250)
    foto = models.ImageField("Foto", upload_to="uploads/people/img")

    def __str__(self):
        return f"{self.nombre}"

 