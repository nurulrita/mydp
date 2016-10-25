from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
	# waktu = forms.DateTimeField(input_formats=('%Y-%m-%dT%H:%M:%S+0000',))
	class Meta:
		model = Todo
		fields = (
			'activity',
			'time',
		)
