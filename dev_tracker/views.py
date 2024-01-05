from django.http import HttpResponse
from .models import Developed
from django.template import loader

from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Developed.objects.order_by("-created_at")[:10]
    context = {"latest_question_list": latest_question_list}
    return render(request, "dev_tracker/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Developed, pk=question_id)
    return render(request, "dev_tracker/detail.html", {"question": question})