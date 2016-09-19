from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post
from .models import User
from .models import Comment
from django.utils import timezone
from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def post_list(request):
    now = datetime.now()
    context = {'current_date': now}
    return render(request, 'project2/post_list.html', context)
    # template = loader.get_template('project2/post_list.html')
    # return HttpResponse(template.render(request))
    # posts = Post.objects.filter(published_date_lte=timezone.now()).order_by('published_date')
    # template = loader.get_template('project2/post_list.html', {posts: posts})
    # return HttpResponse(template.render(request))
    # return render(request, 'project2/post_list.html', {'posts': posts})]
def user_names(request):
    user = User.objects.all()
    context = {'first_name': user}
    return render(request, 'project2/post_list.html', context)

def post_detail(request, post_id):
    try:
        post = m.Post.objects.get(pk=post_id)
    except m.Post.DoesNotExist:
        # If no Post has id post_id, we raise an HTTP 404 error.
        raise Http404
    return render(request, 'project2/detail.html', {'post': post})

def post_upload(request):
    if request.method == 'GET':
        return render(request, 'project2/upload.html', {})
    elif request.method == 'POST':
        post = Post.objects.create(content=request.POST['content'],
                                          created_at=datetime.utcnow())
        #return HttpResponseRedirect(reverse('post_detail', kwargs{'post_id': post.id}))





