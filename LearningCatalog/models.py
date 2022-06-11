from statistics import mode
from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import UserModel, Estudiante
# Creacion de modelos.

# Tipos de archivos para determinar cual icono utilizaremos en la interfaz
FILETYPES = [
    ('PDF', 'Archivo PDF'),
    ('IMG', 'Imagen'),
    ('DOC', 'Archivo Word'),
    ('PPX', 'PowerPoint'),
    ('XLX', 'Archivo Excel'),
    ('ANY', 'Archivo')
]

# Clase de modelos para crear las tablas en la base de datos

#Modelos de los quizzes
class Answer(models.Model):
	answer_text = models.CharField(max_length=900)
	is_correct = models.BooleanField(default=False)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.answer_text)

class Question(models.Model):
	question_text = models.CharField(max_length=900)
	answers = models.ManyToManyField(Answer)
	points = models.PositiveIntegerField()
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.question_text)

class Quizzes(models.Model):
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True)
	date = models.DateTimeField(auto_now_add=True)
	due = models.DateField(null=True)
	allowed_attempts = models.PositiveIntegerField()
	time_limit_mins = models.PositiveIntegerField()
	questions = models.ManyToManyField(Question)

	def __str__(self):
		return str(self.title)

class Attempter(models.Model):
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
	score = models.PositiveIntegerField()
	completed = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user.username)

class Attempt(models.Model):
	quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
	attempter = models.ForeignKey(Attempter, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.answer.answer_text)


class Categoria(models.Model):
    # Todos los atributos vienen de la importacion de models y son clases predefinidas de django para la creacion de tablas
    nombre = models.CharField("Nombre", max_length=30)
    descripcion = models.TextField("Descripción", max_length=100)
    imagen = models.ImageField("Imagen", upload_to='uploads/categories/img')
    fechaCreada = models.DateTimeField("Fecha de creación", auto_now_add=True)
    # Atributo que se refiere a la misma clase para poder tener nesting de categorias
    categoriaPadre = models.ForeignKey(
        'self', blank=True, null=True, on_delete=CASCADE, verbose_name="Categoria perteneciente")

    def __str__(self):
        return f"{self.nombre}"

 
#Modelos de los exercise
class AnswerExercise(models.Model):
	answer_text = models.CharField(max_length=900)
	is_correct = models.BooleanField(default=False)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.answer_text)
 
class QuestionExercise(models.Model):
	question_text = models.CharField(max_length=900)
	answers = models.ManyToManyField(AnswerExercise)
	points = models.PositiveIntegerField()
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.question_text)

class Exercises(models.Model):
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True)
	date = models.DateTimeField(auto_now_add=True)
	due = models.DateField(null=True)
	questions = models.ManyToManyField(QuestionExercise)

	def __str__(self):
		return str(self.title)

class AttempterExercise(models.Model):
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
	score = models.PositiveIntegerField()
	completed = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user.username)

class AttemptExercise(models.Model):
	exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
	question = models.ForeignKey(QuestionExercise, on_delete=models.CASCADE)
	answer = models.ForeignKey(AnswerExercise, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.answer.answer_text)

class Leccion(models.Model):

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    imagen = models.ImageField(upload_to='uploads/lessons/img')
    fecha = models.DateField(
        "Fecha de creación", auto_now=False, auto_now_add=True)
    aprobacion = models.BooleanField("Aprobación", default=False)
    category = models.ForeignKey(
        Categoria, on_delete=CASCADE, verbose_name="Categoria")
    quizzes = models.ManyToManyField(Quizzes)
    exercises = models.ManyToManyField(Exercises)
    # Verbose name y verbose name plural para cambiar el nombre de la seccion en el panel administrativo
    created_by = models.ForeignKey(UserModel, on_delete=CASCADE)
    # liked = models.ManyToManyField(Estudiante, related_name='liked', default=None, blank=True)

    class Meta:
        verbose_name = ("Lección")
        verbose_name_plural = ("Lecciones")
        
    def __str__(self):
        return f"{self.titulo}"

   
    # def num_likes(self):
    #    return self.liked.all().count()


""" LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike') 
)
class Like(models.Model):
    user = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=10)

    def __str__(self):
        return str(self.lesson) """


class Archivo(models.Model):
    orden = models.PositiveSmallIntegerField("Orden de aparición")
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    path = models.FileField("Archivo", upload_to='uploads/files')
    lipo = models.CharField("Tipo de archivo", choices=FILETYPES, max_length=3)
    leccion = models.ForeignKey(Leccion, on_delete=CASCADE)


class Video(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    link = models.CharField(max_length=500)
    leccion = models.ForeignKey(Leccion, on_delete=CASCADE)


class Estudiante_Leccione(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=CASCADE)
    leccion = models.ForeignKey(Leccion, on_delete=CASCADE)

""" class Comentario(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    leccion = models.ForeignKey(Leccion, related_name="comentarios", on_delete=models.CASCADE)
    contenido = models.TextField()


    def __str__(self):
        return '%s - %s' % (self.leccion.titulo, self.estudiante.nombre) """



#class Comentario (models.Model):
#    titulo = models.CharField(max_length=50)
 #   autor = models.ForeignKey (Perfil, null=True, blank=True, on_delete=models.CASCADE)
  #  archivo = models.FileField(upload_to='media/%Y/%m/%d', null=True, blank=True)
   # slug= models.SlugField(default=0)
   # likes = models.ManyToManyField(Perfil, related_name="likes")

    #def __str__(self):
     #   return (self.titulo)

    #@property

    #def total_likes(self):
     #   return self.likes.count()

    #def save(self, *args, **kwargs):
     #   self.slug=slugify(self.titulo)
      #  super(Comentario, self).save(*args, **kwargs)

class Encuesta(models.Model):
    title_leccion = models.TextField(null=True)
    pregunta1 = models.IntegerField()
    pregunta2 = models.IntegerField()
    pregunta3 = models.IntegerField()
    pregunta4 = models.IntegerField()
    pregunta5 = models.IntegerField()
    opinion = models.TextField("Opinion", max_length=500)



class Solicitar(models.Model):
    user = models.TextField(max_length=500)
    nombre_leccion = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return f"{self.user}"


