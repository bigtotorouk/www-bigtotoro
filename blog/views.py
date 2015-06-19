from blog.models import Entry, Comment, Category
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
# Create your views here.
def list(request, template='web/blog/list.html'):
    categories, dates = blog_base()
    print 'list'
    if 'category_id' in request.GET:

        category_id = request.GET['category_id']
        print 'category_id',category_id
        category = categories.filter(id=category_id);
        queryset = Entry.objects.filter(category=category)
    else:
        queryset = Entry.objects.all()
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render_to_response('web/blog/list.html', {"posts": posts,"categories":categories,"dates":dates }, context_instance=RequestContext(request))

def blog_base():
    dates = []
    entryies = Entry.objects.all()
    for entry in entryies:
        #if entry.post_date.year not in years:
        #    years.append(entry.post_date.year)
        blog_date = date(entry.post_date.year, entry.post_date.month, 1)
        if blog_date not in dates:
            dates.append(blog_date)
    categories = Category.objects.all()
    #
    for category in categories:
        category.article_num = 0
        for entry in entryies:
            if entry.category == category:
                category.article_num += 1
        category.save()
    return categories, dates;

def list_category(request, category_id):
    categories = Category.objects.all()
    if category_id:
        category = categories.filter(id=category_id);
        queryset = Entry.objects.filter(category=category)
    else:
        queryset = Entry.objects.all()
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render_to_response('web/blog/list.html', {"posts": posts,"categories":categories,"request":request,}, context_instance=RequestContext(request))

def comment_list(id):
    entry = Entry.objects.get(id=id)
    comments = entry.comment_set.all()
    return comments

def entry(request, id):
    print 'entry'
    categories, dates = blog_base()
    post = Entry.objects.get(pk=id)
    post.hits += 1
    post.save()
    comments = comment_list(id)
    return render_to_response("web/blog/entry.html", {'post':post, "categories":categories, 'comments':comments, "dates": dates}, context_instance=RequestContext(request))

import json
def comment_insert(request, id):
    print 'comment_insert'
    entry = Entry.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['message']
        comment = Comment(name=name, content=content, email=email, entry=entry)
        comment.save()
        return HttpResponse(json.dumps({"status": "1", "msg": "insert message success"}), content_type= 'Application/json')
    else:
        return HttpResponse(json.dumps({"status": "0", "msg": "insert message failed"}), content_type= 'Application/json')

from django_ajax.decorators import ajax
@ajax
def ajax_comment_insert(request, id):
    print 'ajax_comment_insert'
    entry = Entry.objects.get(id=id)
    if request.method == 'POST':
        print 'post'
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['message']
        comment = Comment(name=name, content=content, email=email, entry=entry)
        comment.save()
        return {"status": "1", "msg": "insert message success"}
    else:
        return {"status": "0", "msg": "insert message failed"}

