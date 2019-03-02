import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from home.models import ChatBots

logger = logging.getLogger('app')


def home_view(request):
    #  View: /
    if request.user.is_authenticated:
        bot, created = ChatBots.objects.get_or_create(user=request.user)
        return render(request, 'home.html', {'bot': bot})
    return render(request, 'home.html')


@login_required
@require_http_methods(['POST'])
def add_bot(request):
    #  View: /add
    bot, created = ChatBots.objects.get_or_create(user=request.user)
    if bot.active:
        message(request, 'warning', 'Sorry, the MultiChat bot is already active in your channel.')
    else:
        started = start_bot(request.user.username)
        if started:
            bot.active = True
            bot.save()
            message(request, 'success', 'Success! You have added the MultiChat bot to your channel.')
        else:
            message(request, 'warning', 'Error! Unable to add the MultiChat bot to your channel at this time.')
    return redirect('home:index')


def start_bot(channel):
    try:
        return True
    except Exception:
        return False


def message(request, level, message):
    """
    Easily add a success or error message
    """
    if level == 'success':
        messages.add_message(request, messages.SUCCESS, message, extra_tags='success')
    else:
        messages.add_message(request, messages.WARNING, message, extra_tags=level)
