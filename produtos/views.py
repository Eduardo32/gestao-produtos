from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from gestao_produtos.models import Produto
from produtos.forms import SalvaProdutoForm


class ProdutoListView(ListView):
    #usuario = 1

    #queryset = Produto.objetos.filter(usuario=usuario)
    template_name = 'produtos/lista.html'
    model = Produto
    context_object_name = 'Produtos'


class ProdutoCreateView(CreateView):
    template_name = 'produtos/salva.html'
    model = Produto
    form_class = SalvaProdutoForm
    success_url = reverse_lazy('produtos:lista')


class ProdutoUpdateView(UpdateView):
    template_name = 'produtos/atualiza.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('produtos:lista')


class ProdutoDeleteView(DeleteView):
    template_name = 'produtos/exclui.html'
    model = Produto
    context_object_name = 'Produto'
    success_url = reverse_lazy('produtos:lista')
