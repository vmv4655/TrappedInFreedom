from django.shortcuts import render
from django.http import HttpResponse
from .models import WelcomeMessage

import random

# Create your views here.
def welcome(request):
	welcome_message_total = WelcomeMessage.objects.all().count()
	welcome_message       = WelcomeMessage.objects.all()
	random_index          = random.randint(0, welcome_message_total-1)
	#return HttpResponse('just testing here')
	return render(request, 'inprogress.html', context={'welcome_message':welcome_message[random_index]},)