from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy
from .models import Bb 
from .models import Rubric
from .forms import BbForm



"""def index(request):       #Без шаблона вызов
	#return HttpResponse('<h1>Здесь будет выведен список обьявлений.</h1>')
	s = 'Список обьявлений\r\n\r\n\r\n'
	for bb in Bb.objects.order_by('-published'):
		s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
	return HttpResponse(s, content_type = 'text/plain; charset=utf-8')"""

"""def index(request):        #Без shortcuts

	template = loader.get_template('bboard/index.html') #принимаем шаблон
	bbs = Bb.objects.order_by('-published') #База
	context = {'bbs':bbs}  #контекст связка база с шаблоном
	return HttpResponse(template.render(context, request))"""

def index(request):          #Более новая версия

	bbs = Bb.objects.all()
	rubrics = Rubric.objects.all()
	context = {
		'bbs':bbs,
		'rubrics':rubrics
	}
	return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):

	rubrics = Rubric.objects.all()                 
	bbs = Bb.objects.filter(rubric=rubric_id)
	current_rubric = Rubric.objects.get(pk=rubric_id)
	context = {
		'bbs':bbs,
		'rubrics':rubrics,
		'current_rubric':current_rubric
	}
	return render(request, 'bboard/by_rubric.html', context)

class BbCreateView(CreateView):          #Реализуем поле
	
	template_name = 'bboard/create.html'
	form_class = BbForm 
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context

