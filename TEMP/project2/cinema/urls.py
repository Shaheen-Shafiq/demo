from django.urls import path
from cinema import views
from .import views
app_name = "cinema"
urlpatterns = [
    # path('',views.base,name="base"),
    path('',views.Movielistview.as_view(),name="base"),
    # path('viewdetails/<int:p>',views.viewdetails,name="viewdetails"),
    path('Moviedetail/<int:pk>',views.MovieDetailView.as_view(),name="viewdetails"),
    # path('update/<int:p>', views.update, name="update"),
    path('Movieupdate/<int:pk>',views.Movieupdateview.as_view(),name="movieupdate"),
    # path('delete/<int:p>', views.delete, name="delete"),
    path('Moviedelete/<int:pk>',views.Deletemovieview.as_view(),name="moviedelete"),
    path('addmovie/', views.addmovie, name="addmovie")


]
