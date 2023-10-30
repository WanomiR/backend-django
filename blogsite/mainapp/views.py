from django.shortcuts import render, redirect

# Create your views here.

posts = [
    {
        "Title": "fjfjjf",
        "Description": "gjgj",
        "Author": "gjjg",
        "Date": "gjgjjg"
     }
]


def indexpage(request):
    return render(request, "index.html", {"articles": posts, "page": "index"})


def aboutpage(request):
    return render(request, "about.html", {"page": "about"})


def contactpage(request):
    if request.method == "GET":
        return render(request, "contact.html", {"page": "contact"})

    else:
        print(request.POST)
        with open("/Users/vladbax6/Codding/code_works/Sites/Django/CourseBlog/Backend/blogsite/mainapp/contact_resuls.txt", "a") as file:
            file.writelines(f"Name: {request.POST['name']}, Email: {request.POST['email']}, Subject: {request.POST['subject']}")
        return redirect(contactpage)
