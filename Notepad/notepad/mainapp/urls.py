from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.notes_page, name="notes"),
    path("reg", views.register_page, name="reg"),
    path("reg/", views.register_page, name="reg"),
    path("login", views.login_page, name="login"),
    path("login/", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("logout/", views.logout_page, name="logout"),
    path("notes", views.notes_page, name="notes"),
    path("notes/", views.notes_page, name="notes"),
    path("add_note", views.add_note_page, name="add_note"),
    path("add_note/", views.add_note_page, name="add_note"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)