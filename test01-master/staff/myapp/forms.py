from .models import Task
from django.forms import ModelForm, TextInput
from django.forms import ModelForm, TextInput, FileField, ClearableFileInput
from django.forms import FileInput
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "place", "price", "square", "img"]
        widgets ={
            "name": TextInput(attrs={
                'class': 'form-control w-75',
                'placeholder': 'Название'
            }),
            "price": TextInput(attrs={
                'class': 'form-control w-75',
                'placeholder': 'Цена'
            }),
            "place": TextInput(attrs={
                'class': 'form-control w-75',
                'placeholder': 'Количество'
            }),
            "square": TextInput(attrs={
                'class': 'form-control w-75',
                'placeholder': 'Адрес заказа'
            }),
            "img": FileInput(attrs={
                'class': 'p_files w-75',
                'placeholder': 'Файлы'
            }),
        }
