from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404,HttpResponse

def home(request):
    return render(request, 'home.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form=CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, "post_detail.html", {
    'post': post,
    'comments': comments,
    'comment_form': comment_form})