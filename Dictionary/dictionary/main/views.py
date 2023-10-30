from django.shortcuts import render, redirect


WORDS_LIST_PATH = "words_list.txt"


def add_to_file(word1: str, word2: str):
    with open(WORDS_LIST_PATH, "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


def read_from_file():
    file = open(WORDS_LIST_PATH, "r", encoding="utf-8").read().splitlines()
    words = []
    for line in file:
        word1, word2 = line.split("-")
        words.append([word1, word2])
    return words


def index_page(request):
    return render(request, "index.html", {"page": "index"})


def words_list_page(request):
    return render(
        request, "words_list.html",
        {"page": "words_list", "words_list": read_from_file()})


def add_word_page(request):
    if request.method == "GET":
        return render(request, "add_word.html", {"page": "add_word"})
    elif request.method == "POST":
        add_to_file(
            request.POST["word1"],
            request.POST["word2"],
        )
        return redirect(add_word_page)
    else:
        print("Unknown request!")
