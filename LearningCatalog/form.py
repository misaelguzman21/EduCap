from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from accounts.models import *
from .models import *

class NewQuizForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	allowed_attempts = forms.IntegerField(max_value=100, min_value=1)
	time_limit_mins = forms.IntegerField(max_value=360, min_value=10)

	class Meta:
		model = Quizzes
		fields = ('title', 'description', 'allowed_attempts', 'time_limit_mins')


class NewQuestionForm(forms.ModelForm):
	question_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	points = forms.IntegerField(max_value=100, min_value=1)

	class Meta:
		model = Question
		fields = ('question_text', 'points')


class Search(forms.Form):
    search = forms.CharField(label='Your name', max_length=100)


class NewExerciseForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	
	class Meta:
		model = Exercises
		fields = ('title', 'description')
 

class NewQuestionExerciseForm(forms.ModelForm):
	question_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
	points = forms.IntegerField(max_value=100, min_value=1)

	class Meta:
		model = QuestionExercise
		fields = ('question_text', 'points')