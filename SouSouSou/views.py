from django.shortcuts import render
from .forms import DSform
from question.models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import random


# Create your views here.

def class_list(request):
    return render(request, 'SouSouSou/main.html')


def test(request):
    if not request.session.get('is_login', None):
        return HttpResponse('您尚未登陆,没有操作权限')


def quest_generator(request):
    if not request.session.get('is_login', None):
        return HttpResponse('您尚未登陆')
    if request.method == 'POST':
        g_form = DSform(request.POST)
        if g_form.is_valid():
            quantity = g_form.quantity
            if_pow = g_form.if_pow
            if_fra = g_form.if_fra
            if_neg = g_form.if_neg
            potp = g_form.potyp
            operator = g_form.operators
            quest: list
            quest = Question.objects.filter(quantity=quantity, question_if_negative=if_neg,
                                            question_operators_num=operator, question_if_pow=if_pow)
            i = 0
            output_list: list
            while i < quantity:
                rand = random.randint(0, quest.__len__() - 1)
                quest[rand].question = string_change(quest[rand].question, potp)
                output_list.append(quest[rand])
                quest.pop(rand)
                i += 1
            context = {'output_list': output_list, 'if_fraction': if_fra, 'type': "POST"}
            return render(request, 'SouSouSou/Generator.html', context)
        else:
            HttpResponse('form contents err')
    g_form = DSform()
    context = {'form': g_form, 'type': "GET"}
    return render(request, 'SouSouSou/Generator.html', context)


def string_change(string: str, potp):
    if potp:
        return string.replace('^', '**')
    return string
