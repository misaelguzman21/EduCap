from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Carrousel(models.Model):
    imagen1 = models.ImageField(
        upload_to='uploads/carrousel/img', verbose_name='Imagen 1')
    imagen2 = models.ImageField(
        upload_to='uploads/carrousel/img', verbose_name='Imagen 2')
    imagen3 = models.ImageField(
        upload_to='uploads/carrousel/img', verbose_name='Imagen 3')

    class Meta:
        verbose_name = ("Carrousel")
        verbose_name_plural = ("Carrouseles")

    def __str__(self):
        return "Carrousel"

    def save(self, *args, **kwargs):
        if not self.pk and Carrousel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            ValidationError
            raise ValidationError(
                'Solo puede existir un objeto de este tipo.')
        return super(Carrousel, self).save(*args, **kwargs)

    def clean(self):
        if Carrousel.objects.exists() and not self.pk:
            raise ValidationError(
                "Solo puede existir un objeto de este tipo, por favor modifica el objeto en lugar de crear otro.")


class HomeSections(models.Model):
    # Card de lecciones
    imagenLecciones = models.ImageField(
        upload_to='uploads/homeSection/img', verbose_name='Imagen de lecciones')
    textoLecciones = models.TextField(
        max_length=250, verbose_name='Texto de lecciones')
    # Card de categorias
    imagenCategorias = models.ImageField(
        upload_to='uploads/homeSection/img', verbose_name='Imagen de categorías')
    textoCategorias = models.TextField(
        max_length=250, verbose_name='Texto de categorías')
    # Card de crear cuenta
    imagenCrearCuenta = models.ImageField(
        upload_to='uploads/homeSection/img', verbose_name='Imagen de crear cuenta')
    textoCrearCuenta = models.TextField(
        max_length=250, verbose_name='Texto de crear cuenta')

    class Meta:
        verbose_name = ("Tarjetas de secciones")
        verbose_name_plural = ("Tarjetas de secciones")

    def __str__(self):
        return "Tarjetas de secciones"

    def save(self, *args, **kwargs):
        if not self.pk and HomeSections.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            ValidationError
            raise ValidationError(
                'Solo puede existir un objeto de este tipo.')
        return super(HomeSections, self).save(*args, **kwargs)

    def clean(self):
        if HomeSections.objects.exists() and not self.pk:
            raise ValidationError(
                "Solo puede existir un objeto de este tipo, por favor modifica el objeto en lugar de crear otro.")


class JumboTronHome(models.Model):

    titulo = models.TextField(
        max_length=250, verbose_name='Título')

    subtitulo = models.TextField(
        max_length=250, verbose_name='Subtítulo')

    subtituloPequeno = models.TextField(
        max_length=250, verbose_name='Subtítulo pequeño')

    class Meta:
        verbose_name = ("Jumbotron")
        verbose_name_plural = ("Jumbotron")

    def __str__(self):
        return "Jumbotron"

    def save(self, *args, **kwargs):
        if not self.pk and JumboTronHome.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            ValidationError
            raise ValidationError(
                'Solo puede existir un objeto de este tipo.')
        return super(JumboTronHome, self).save(*args, **kwargs)

    def clean(self):
        if JumboTronHome.objects.exists() and not self.pk:
            raise ValidationError(
                "Solo puede existir un objeto de este tipo, por favor modifica el objeto en lugar de crear otro.")
