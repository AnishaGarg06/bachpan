from django import forms

from .models import Post
from .models import SurvivorStories

class PostForm(forms.ModelForm):

	class Meta:
		model=Post
		fields = ('title', 'text',)

class PostStory(forms.ModelForm):

	class Meta:
		model=SurvivorStories
		fields = ('text', 'published_date',)