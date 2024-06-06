from django.forms import ModelForm
from .models import *

class AdminShowcaseForm(ModelForm):
    class Meta:
        model = AdminShowcase
        fields ='__all__'

class AdminsLastMoviesForm(ModelForm):
    class Meta:
        model = AdminLastMovies
        fields ='__all__'
class AmdminsMoviesForm(ModelForm):
    class Meta:
        model = AdminMovies
        fields ='__all__'