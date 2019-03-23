from django.urls import path
from produtos.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

app_name = 'produtos'

urlpatterns = [
    path('', ProdutoListView.as_view(), name='lista'),
    path('salvar/', ProdutoCreateView.as_view(), name='novo'),
    path('atualizar/<int:pk>', ProdutoUpdateView.as_view(), name='atualiza'),
    path('exclir/<int:pk>', ProdutoDeleteView.as_view(), name='exclui'),
]
