from typing import Any, Dict, Optional
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.views.generic import ListView
from .models import Article
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin,
UserPassesTestMixin)
from .forms import CommentForm,ArticleForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

# 1:classbaseview
# class ArticleListVuew(ListView):
#     model = Article
#     template_name = "articles/article_list.html"

# 2:function
def articlelist(request): 
    article = Article.objects.all()
    context = {
        "article":article
    }
    return render(request,"articles/article_list.html",context)




# 1:classbaseview
# class BlogDetailview(FormMixin,DetailView):
#     model = Article
#     template_name = "articles/detailview.html"
#     form_class = CommentForm

#   1:classbaseview (detail)     
    # def get_success_url(self):
    #    return reverse("articles:detail",kwargs={"pk":self.object.id})
    # def get_context_data(self, **kwargs):
    #     context = super(BlogDetailview,self).get_context_data(**kwargs)
    #     context['form'] = CommentForm(initial={"article":self.object ,"writer":self.request.user})
    #     return context 
    # def post(self,*args,**kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         pass
    # def form_valid(self, form):
    #     form.save() 
    #     return super(BlogDetailview,self).form_valid(form)
      




# 2:function
def article_detail(request,pk):
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article,id=pk)
    form = CommentForm()
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.writer  = request.user   
                obj.article = article
                obj.save()
                return HttpResponseRedirect(request.path_info)
        else:
            form = CommentForm()
    else:
        article = get_object_or_404(Article,id=pk)
        return render(request,"articles/detailview.html",{"article":article})
    
    return render(request,"articles/detailview.html",{"article":article ,"form":form})
 




# 1:classbaseview
# class ArticlesUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    # model = Article
    # fields = ('title',"body")
    # template_name = "articles/update.html"

    # def test_func(self):
    #     object = self.get_object()
    #     return object.author == self.request.user




# 2:function
@login_required
def ArticleUpdate(request,pk):
    article =get_object_or_404(Article,id=pk)
    if request.user == article.author:
        form = ArticleForm(request.POST or None , instance=article)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return 
        
        form = ArticleForm
        return render(request,"articles/update.html",{"form":form})
    else:
        return HttpResponseForbidden()






# 1:classbaseview
# class ArticlesDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    # model = Article
    # template_name = "articles/delete.html"
    # success_url = reverse_lazy('articles:articles')

    # def test_func(self):
        # object = self.get_object()
        # return object.author == self.request.user



# 2:function
@login_required
def articledelet(request,pk):
    article = get_object_or_404(Article,id=pk)
    if request.user == article.author:
        if request.method == "POST":
            article.delete()
            return HttpResponseRedirect("/"+"articles/")
        return render(request,"articles/delete.html",{"article":article})
    else:
        return HttpResponseForbidden()


# 1:classbaseview
# class CreatViews(LoginRequiredMixin,CreateView):
    # model = Article
    # template_name = "articles/creatview.html"
    # fields = ("title","body")
    # def form_valid(self,form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    




# 2:function
@login_required
def articlecreate(request):
    # if request.user.is_authenticated:
        form = ArticleForm()
        if request.method == "POST":
            form = ArticleForm(request.POST)
            if form.is_valid():
                post_title = form.cleaned_data["title"]
                post_body = form.cleaned_data["body"]
                post_author =request.user
                object = Article(title=post_title,body=post_body,author=post_author)
                object.save()
                return HttpResponseRedirect("/"+"articles/")
        else:
            form= ArticleForm()  
    # else:
    #     return HttpResponseRedirect("/"+"accounts/login/")

        return render(request,"articles/creatview.html",{"form":form})
    