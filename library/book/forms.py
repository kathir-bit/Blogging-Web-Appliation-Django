
from django import forms
from book.models import Book
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'