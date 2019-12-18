from .forms import DSform
from question.models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import random


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
            quantity = g_form.cleaned_data['quantity']
            if_pow = g_form.cleaned_data['if_pow']
            if_fra = g_form.cleaned_data['if_fra']
            if_neg = g_form.cleaned_data['if_neg']
            potp = g_form.cleaned_data['pow_type']
            operator = g_form.cleaned_data['operators']
            quest = get_ls(operator=operator, if_pow=if_pow, if_neg=if_neg)
            i = 0
            print(quest)
            ot_ls = []
            while i < quantity:
                rand = random.randint(0, quest.__len__() - 1)
                quest[rand].question = string_change(quest[rand].question, potp)
                ot_ls.append(quest[rand])
                quest.pop(rand)
                i += 1
            context = {'output_list': ot_ls, 'if_fraction': if_fra, 'type': "POST"}
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


def get_ls(operator: list, if_pow, if_neg):
    i = 0
    rt_ls = []
    if if_neg == 'both':
        if if_pow == 'both':
            while i < operator.__len__():
                quest = Question.objects.filter(question_operators_num=operator[i])
                i += 1
                j = 0
                while j < quest.__len__():
                    rt_ls.append(quest[j])
                    j += 1
            return rt_ls
        else:
            while i < operator.__len__():
                quest = Question.objects.filter(question_operators_num=operator[i], question_if_pow=if_pow)
                i += 1
                j = 0
                while j < quest.__len__():
                    rt_ls.append(quest[j])
                    j += 1
            return rt_ls
    elif if_pow == 'both':
        if if_neg == 'both':
            while i < operator.__len__():
                quest = Question.objects.filter(question_operators_num=operator[i])
                i += 1
                j = 0
                while j < quest.__len__():
                    rt_ls.append(quest[j])
                    j += 1
            return rt_ls
        else:
            while i < operator.__len__():
                quest = Question.objects.filter(question_operators_num=operator[i], question_if_pow=if_pow)
                i += 1
                j = 0
                while j < quest.__len__():
                    rt_ls.append(quest[j])
                    j += 1
            return rt_ls
    else:
        while i < operator.__len__():
            quest = Question.objects.filter(question_if_negative=if_neg,
                                            question_operators_num=operator[i], question_if_pow=if_pow)
            i += 1
            j = 0
            while j < quest.__len__():
                rt_ls.append(quest[j])
                j += 1
        return rt_ls
