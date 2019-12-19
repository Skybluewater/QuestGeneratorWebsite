from django.shortcuts import render, HttpResponse
from login.models import User
from .forms import DSform, Form5
from SouSouSou.models import History
from SouSouSou.views import get_ls, string_change
import random
from .models import Answer, WrongAnswer
from django.utils import timezone


# Create your views here.


def generator(request):
    if not request.session.get('is_login', None):
        return HttpResponse('您尚未登陆,无法操作')
    if request.method == "POST":
        form = DSform(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if_pow = form.cleaned_data['if_pow']
            if_fra = form.cleaned_data['if_fra']
            if_neg = form.cleaned_data['if_neg']
            potp = form.cleaned_data['pow_type']
            operator = form.cleaned_data['operators']
            quest = get_ls(operator=operator, if_pow=if_pow, if_neg=if_neg)
            user = User.objects.get(id=request.session.get('user_id', None))
            i = 0
            ot_ls = []
            history = History.objects.create()
            history.user = user
            history.quantity = quantity
            history.if_fra = if_fra
            history.save()
            id = history.id
            while i < int(quantity):
                rand = random.randint(0, quest.__len__() - 1)
                quest[rand].question = string_change(quest[rand].question, potp)
                ot_ls.append(quest[rand])
                quest.pop(rand)
                i += 1
            i = 0
            while i < int(quantity):
                answer = Answer.objects.create()
                answer.answer_id = history
                answer.question = ot_ls[i]
                answer.save()
                i = i + 1
            dic = {'answer_id': id}
            g_form = Form5(dic)
            context = {'output_list': ot_ls, 'form': g_form}
            return render(request, 'question/Question_list.html', context)
    form = DSform()
    context = {'form': form}
    return render(request, 'question/Question.html', context)
