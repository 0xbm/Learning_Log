from django.shortcuts import render, redirect

# Create your views here.
from .models import Topic
from .forms import TopicForm, EntryForm


def index(request):
    return render(request, "learning_logs/index.html")


def topics(request):
    """Wyswietlenie wszytskich tematow"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """Wyswietla pojedynczy temat i wszystkie powaizane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


def new_topic(request):
    """Dodaj nowy temat"""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


def new_entry(request, topic_id):
    """Dodanie nowego wpisu dla okreslonego tematu"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    # Wyswietlanie pustego formularza
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)
