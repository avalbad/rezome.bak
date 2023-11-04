from django.urls import path
from .import views

app_name ="articles"
urlpatterns = [
    # 1:classbaseview
    # path("",views.ArticleListVuew.as_view(),name="articles"),
    # path('<int:pk>/',views.BlogDetailview.as_view(),name = "detail"),
    # path('edite/<int:pk>/',views.ArticlesUpdateView.as_view(),name= "update"),
    # path('delete/<int:pk>/',views.ArticlesDeleteView.as_view(),name= "delete"),
    # path('new/',views.CreatViews.as_view(),name ='newpost'),
  

    # 2:function
    path('delete/<int:pk>/',views.articledelet,name= "delete"),
    path('<int:pk>/edit/',views.ArticleUpdate,name= "update"),
    path('<int:pk>/',views.article_detail,name = "detail"),
    path('new/',views.articlecreate,name ='newpost'),
    path("",views.articlelist,name="articles"),

]