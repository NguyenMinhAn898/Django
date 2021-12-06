from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Place, Blog
from django.utils.dateparse import parse_datetime
# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    context = {'listBlog': blogs}
    return render(request, 'blog/home/index.html', context)


def newsBlog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        description = request.POST.get('description')
        imageUrl = request.POST.get('imageUrl')
        status = request.POST.get('status')
        categoryId = request.POST.get('category')
        publicDate = request.POST.get('publicDate')
        Blog.objects.create(
            title=title,
            detail=detail,
            description=description,
            imgUrl=imageUrl,
            status=strToBool(status),
            category=Category.objects.get(id=categoryId),
            # publicDate = datetime.fromtimestamp(publicDate)
        )
        return redirect('home')
    elif request.method == 'GET':
        categories = Category.objects.all()
        places = Place.objects.all()
        context = {'listCategory': categories, 'listPlace': places}
        return render(request, 'blog/news/index.html', context)


def searchBlog(request):
    context = {'listBlog': None, 'searchStr': 'Search'}
    return render(request, 'blog/search/index.html', context)


def detailBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    categories = Category.objects.all()
    places = Place.objects.all()
    context = {'blog': blog, 'listCategory': categories, 'listPlace': places}
    return render(request, 'blog/detailBlog.html', context)


def updateBlog(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        description = request.POST.get('description')
        imageUrl = request.POST.get('imageUrl')
        status = request.POST.get('status')
        categoryId = request.POST.get('category')
        if id != None:
            blog = Blog.objects.get(id=id)
            blog.title = title
            blog.detail = detail
            blog.description = description
            blog.imageUrl = imageUrl
            blog.status = strToBool(status)
            blog.category = Category.objects.get(id=categoryId)
            blog.save()
            return redirect('home')
    else:
        return redirect('home')


def delete_Blog(request, pk):
    blog = Blog.objects.get(id=pk)
    if(blog != None):
        blog.delete()

    return redirect('home')


def strToBool(v):
    return v.lower() in ("yes", "true", "True", "t", "1")
