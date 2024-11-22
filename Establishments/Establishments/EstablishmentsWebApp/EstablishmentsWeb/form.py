from .models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 11)],  
        widget=forms.RadioSelect,
        label='Рейтинг (из 10)'
    )
        fields = ['username', 'title', 'feedback', 'rating']
        labels={
            'username': 'Имя пользователя',
            'title': 'Наименование заведения'
        }

        widgets = {  # Добавление атрибута disabled для поля 'name'
            'name': forms.TextInput(attrs={'readonly': 'readonly'}) 
        }