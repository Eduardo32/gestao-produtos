from django import forms
from gestao_produtos.models import Produto


class SalvaProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto

        fields = '__all__'
