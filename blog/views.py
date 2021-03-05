from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.utils.decorators import method_decorator
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from user.models import User
from django.core.paginator import Paginator


def home(request, pg=1):
    if request.user.is_authenticated and request.user.is_team:
        posts = Post.objects.order_by('-date_published')
    else:
        posts = Post.objects.filter(
            is_published=True).order_by('-date_published')
    
    paginator = Paginator(posts, 5);

    context = {
        'posts': paginator.page(pg),
        'page': pg,
        'paginator': paginator
    }
    return render(request, 'blog/home.html', context)



def search(request, pg=1):
    query = request.GET['search']
    posts = Post.objects.filter(title__icontains = query)
    paginator = Paginator(posts, 20);

    context = {
        'posts': paginator.page(pg),
        'page': pg,
        'paginator': paginator
    }
    return render(request, 'blog/search.html', context)



# class PostDetailView(DetailView):
#     model = Post

def PostDetailView(request, pk, pg=1):

    post = Post.objects.filter(id=pk).first()
    
    context = {
        'post' : post,
    }

    return render(request, 'blog/post_detail.html', context)

def PostCreateView(request, pg=1):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your submission has been sent to our team for review. You will be notified via e-mail if it is published.')

            return HttpResponseRedirect(reverse('blog-home', args=[1]))

    else:
        form = PostCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/post_form.html', context)


def PostUpdateView(request, pk):
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES,
                              instance=Post.objects.filter(id=pk).first())
        if form.is_valid():
            if request.user.is_team:
                form.save()
                messages.success(request, 'Your blog has been published.')
                return HttpResponseRedirect(reverse('blog-home', args=[1]))
            else:
                messages.warning(
                    request, 'You do not have the perimission to update this blog.')

    else:
        form = PostUpdateForm(instance=Post.objects.filter(id=pk).first())

    context = {
        'form': form
    }

    return render(request, 'blog/post_form.html', context)


@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_team), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('blog-home', args=[1])


def magazine(request):
    return render(request, 'blog/bizfanatics.html')
