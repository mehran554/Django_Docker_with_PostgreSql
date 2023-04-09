from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartForm


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/list_view.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail_view.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartForm()
        return context


# def comment_view(request):
#     # comment = Comment.objects.get(pk=pk)
#     # if request.user == book.user:
#     # comments_book = comment.comments.all()
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         # if comment_form.is_valid():
#         #     new_comment_form = comment_form.save()
#         # new_comment_form.user = request.user
#         # new_comment_form.book = book
#         # new_comment_form.save()
#         # comment_form = CommentForm()
#
#     else:
#         comment_form = CommentForm()
#
#     return render(request, 'products/detail_view.html', {'comment_form': comment_form})
#

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm()

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        messages.success(self.request, 'پست شما با موفقیت ارسال شد ')
        return super().form_valid(form)
