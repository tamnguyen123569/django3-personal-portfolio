from django.shortcuts import render, get_object_or_404
from .models import Blog
#paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog(request):
    #blogs = Blog.objects.order_by('-date')
    blogs = Blog.objects.all()
    #Paginator
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page', 1)

    try:
        orders_paged = paginator.page(page)
    except PageNotAnInteger:
        orders_paged = paginator.page(1)
    except EmptyPage:
        orders_paged = paginator.page(paginator.num_pages)
    
    #context = {"orders": orders_paged}
    context = {"orders": orders_paged}
    return render(request, 'blog/blog.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})