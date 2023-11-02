from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import User, Note


# Create your views here.
@csrf_exempt
def register_page(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        data = request.POST
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password1, password2 = data.get("password1"), data.get("password2")

        if not all([username, first_name, last_name, email, password1, password2]):
            return HttpResponse("<h3>All fields must be filled!</h3>")
        elif password1 != password2:
            return HttpResponse("<h3>Passwords must match!</h3>")
        else:
            new_user = User()
            new_user.create_user(username, first_name, last_name, email, password1)
            return HttpResponse("<h3>You have successfully registered!")
    else:
        return HttpResponse(f"Unpredicted method: {request.method}")


@csrf_exempt
def login_page(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        data = request.POST
        try:
            user = authenticate(request, username=data["username"], password=data["password"])
            if user is None:
                return HttpResponse("<h3>No such user!</h3>")
            login(request, user)
            return redirect(notes_page)
        except KeyError:
            return HttpResponse("<h3>Fill in all fields!</h3>")
    else:
        return HttpResponse(f"Unpredicted method: {request.method}")


def logout_page(request):
    logout(request)
    return redirect(login_page)


@login_required(login_url="login")
def notes_page(request):
    notes = Note.objects.filter(username=request.user).all()
    return render(request, "notes.html", {"notes": notes})


@csrf_exempt
@login_required(login_url="login")
def add_note_page(request):
    if request.method == "GET":
        return render(request, "add_note.html")
    elif request.method == "POST":
        data = request.POST
        print(data)
        note = Note()
        note.add_note(data["note-text"], request.user)
        return redirect(notes_page)
    else:
        return HttpResponse(f"Unpredicted method: {request.method}")
