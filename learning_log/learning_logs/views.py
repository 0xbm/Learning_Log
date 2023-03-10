from django.shortcuts import render

# Create your views here.
from .models import Topic


def index(request):
    return render(request, "learning_logs/index.html")


def topics(request):
    """Wyswietlenie wszytskich tematow"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    "wyswietla pojedynczy temat i wszystkie powaizane z nim wpisy"
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
