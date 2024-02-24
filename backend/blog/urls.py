# blog.urls.py

from django.urls import path, include

from blog import views

app_name = 'blog'
urlpatterns = [
    path("post/",
        include([
            path(route='', view=views.post_list_view, name='post_list'),
            path(route='detail/<slug>/', view=views.post_detail_view, name='post_detail'),
        ]),
    ),
    path("categorie/",
        include([
            path(route='', view=views.category_detail_view, name='category_detail'),
        ]),
    ),
]
