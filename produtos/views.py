from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from gestao_produtos.models import Produto
from produtos.forms import SalvaProdutoForm


class ProdutoListView(ListView):

    template_name = 'produtos/lista.html'
    model = Produto
    context_object_name = 'Produtos'

    def get_queryset(self):
        usuario = self.request.user.id
        queryset = Produto.objetos.filter(usuario=usuario)
        return queryset


class ProdutoCreateView(CreateView):
    template_name = 'produtos/salva.html'
    model = Produto
    form_class = SalvaProdutoForm
    success_url = reverse_lazy('produtos:lista')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(ProdutoCreateView, self).form_valid(form)


class ProdutoUpdateView(UpdateView):
    template_name = 'produtos/atualiza.html'
    model = Produto
    fields = [
        'nome',
        'descricao',
        'qtd',
        'preco',
    ]
    success_url = reverse_lazy('produtos:lista')


class ProdutoDeleteView(DeleteView):
    template_name = 'produtos/exclui.html'
    model = Produto
    context_object_name = 'Produto'
    success_url = reverse_lazy('produtos:lista')
