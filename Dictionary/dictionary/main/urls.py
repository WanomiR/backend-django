from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index_page, name="index"),
    path("home", views.index_page, name="index"),
    path("home/", views.index_page, name="index"),
    path("words_list", views.words_list_page, name="words_list"),
    path("words_list/", views.words_list_page, name="words_list"),
    path("add_word", views.add_word_page, name="add_word"),
    path("add_word/", views.add_word_page, name="add_word"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # STATIC_DIR ???
