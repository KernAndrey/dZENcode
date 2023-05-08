from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import Comment, User
from .forms import NewComment


menu = [
    {'title': "Home", 'url_name': 'home'},
    {'title': "New comment", 'url_name': 'new_comment'},
]


class CommentListView(ListView):
    model = Comment
    template_name = 'home.html'
    context_object_name = 'comments'
    paginate_by = 25

    def get_queryset(self):
        sort_field = self.request.GET.get('sort', '-created_date')
        queryset = Comment.objects.filter(parent_comment=self.request.GET.get('parent'))
        queryset = queryset.order_by(sort_field)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_field'] = self.request.GET.get('sort', '-created_date')
        context['menu'] = menu
        print(context['comments'])
        return context


class NewCommentView(FormView):
    template_name = 'new_comment.html'
    form_class = NewComment
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        try:
            self.save(form.cleaned_data)
            return super().form_valid(form)
        except Exception as ex:
            form.add_error(None, ex)
            return self.render_to_response(self.get_context_data(form=form))

    def save(self, cleaned_data):
        # get_or_create User
        user_model, created = User.objects.get_or_create(
            user_name=cleaned_data['user_name'],
            email=cleaned_data['email'],
            home_page=cleaned_data['home_page']
        )

        # Validate and create new Comment
        new_comment = Comment()
        new_comment.user_name = user_model
        new_comment.text = cleaned_data['text']
        new_comment.html_validation()
        new_comment.save()



