from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from wonderwords import RandomSentence


@require_GET
@login_required
def ai_tool(request: HttpRequest) -> HttpResponse:
    return render(request, 'gpt.html')


@require_POST
@login_required
def send_message(request: HttpRequest) -> HttpResponse:
    # TODO save in database and return real response
    r: RandomSentence = RandomSentence()
    data = {
        'reply': r.simple_sentence()
    }
    return JsonResponse(data)


@require_GET
def poll_bot(request: HttpRequest) -> HttpResponse:
    # TODO read from database
    r: RandomSentence = RandomSentence()
    data = {
        'newMessages': [
            r.simple_sentence(),
            r.sentence(),
            r.bare_bone_sentence()
        ],
        'lastMessageId': 444,

    }
    return JsonResponse(data)
