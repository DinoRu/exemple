from django import forms
from app.blog.models import SubscribeUsers


class SubscribeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({'class': 'input email', 'placeholder': 'Enter your email...'})

	class Meta:
		model = SubscribeUsers
		fields = ['email']