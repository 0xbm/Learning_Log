from django.shortcuts import render, redirect

# Create your views here.
from .models import Topic
from .forms import TopicForm


def index(request):
    return render(request, "learning_logs/index.html")


def topics(request):
    """Wyswietlenie wszytskich tematow"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """wyswietla pojedynczy temat i wszystkie powaizane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


def new_topic(request):
    """dodaj nowy temat"""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)
