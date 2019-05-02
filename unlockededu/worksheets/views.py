from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import FreeResponseQuestion, MultipleChoiceQuestion


def get_free_responses():
    fr_questions = list(FreeResponseQuestion.objects.all())

    frqs = []
    for frq in fr_questions:
        frqs.append(
            {
                'question': frq.text,
                'answer': frq.answer,
                'subject': frq.subject.name,
                'tags': [tag.name for tag in list(frq.tags.all())],
            }
        )
    return frqs


def get_multiple_choices():
    mc_questions = list(MultipleChoiceQuestion.objects.all())

    mcqs = []
    for mcq in mc_questions:
        mcqs.append(
            {
                'question': mcq.text,
                'answer_choices': [ans.answer for ans in
                                   mcq.mcanswer_set.all()],
                'answers': [ans.answer for ans in
                            mcq.mcanswer_set.all() if ans.correct is True],
                'subject': mcq.subject.name,
                'tags': [tag.name for tag in list(mcq.tags.all())]
            }
        )

    return mcqs


def multiple_choice_questions(request):
    data = {
        'multiple_choice_questions': get_multiple_choices(),
    }
    return render(request, 'mcq.html', data)


def free_response_questions(request):
    data = {
        'free_response_questions': get_free_responses(),
    }
    return render(request, 'frq.html', data)


@login_required
def raw_dump(request):
    data = {
        'multiple_choice_questions': get_multiple_choices(),
        'free_response_questions': get_free_responses()
    }
    return JsonResponse(data)
