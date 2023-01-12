from django import forms
from .models import UserProgress


class UserProgressForm(forms.ModelForm):
    class Meta:
        model = UserProgress
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'height': 'Height',
            'weight': 'Weight',
            'waist': 'measurements',
            'chest': 'measurements',
            'weight_goal': 'Goal Weight',
        }

        self.fields['height'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False