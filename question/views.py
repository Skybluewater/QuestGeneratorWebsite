from django.shortcuts import render, HttpResponse
from login.models import User
from .forms import DSform, Form5, Form10, Form20
from SouSouSou.models import History
from SouSouSou.views import get_ls, string_change
import random
from .models import Answer, WrongAnswer


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
            if int(quantity) == 5:
                g_form = Form5
            elif int(quantity) == 10:
                g_form = Form10
            else:
                g_form = Form20
            context = {'output_list': ot_ls, 'form': g_form, 'answer_id': id, 'quantity': quantity}
            return render(request, 'question/Question_list.html', context)
    form = DSform()
    context = {'form': form}
    return render(request, 'question/Question.html', context)


def confirm(request, num, answer_id):
    if request.method == "POST":
        if num == 5:
            form = Form5(request.POST)
            if form.is_valid():
                answer = {}
                answer[0] = form.cleaned_data['Kt1']
                answer[1] = form.cleaned_data['Kt2']
                answer[2] = form.cleaned_data['Kt3']
                answer[3] = form.cleaned_data['Kt4']
                answer[4] = form.cleaned_data['Kt5']
                history = History.objects.get(id=answer_id)
                if history.end_time != None:
                    return HttpResponse('您已经提交过,请勿重复提交!')
                history.__set_end_time__()
                time = history.end_time - history.start_time
                as_list = Answer.objects.filter(answer_id=history)
                s, ot_ls = calculate(answer, as_list, num, if_fra=history.if_fra, history=history)
                if s == 'False':
                    return HttpResponse('input string must be a string could be converted to float')
                history.score = s
                history.save()
                context = {'output_list': ot_ls, 'score': s, 'time': time, 'if_fra': history.if_fra}
                return render(request, 'question/your_score.html', context)
            return HttpResponse('请重新填写表单')
        elif num == 10:
            form = Form10(request.POST)
            print(request.POST)
            if form.is_valid():
                answer = {}
                answer[0] = form.cleaned_data['Kt1']
                answer[1] = form.cleaned_data['Kt2']
                answer[2] = form.cleaned_data['Kt3']
                answer[3] = form.cleaned_data['Kt4']
                answer[4] = form.cleaned_data['Kt5']
                answer[5] = form.cleaned_data['Kt6']
                answer[6] = form.cleaned_data['Kt7']
                answer[7] = form.cleaned_data['Kt8']
                answer[8] = form.cleaned_data['Kt9']
                answer[9] = form.cleaned_data['Kt10']
                history = History.objects.get(id=answer_id)
                if history.end_time != None:
                    return HttpResponse('您已经提交过,请勿重复提交!')
                history.__set_end_time__()
                time = history.end_time - history.start_time
                as_list = Answer.objects.filter(answer_id=history)
                s, ot_ls = calculate(answer, as_list, num, if_fra=history.if_fra, history=history)
                if s == 'False':
                    return HttpResponse('input string must be a string could be converted to float')
                history.score = s
                history.save()
                context = {'output_list': ot_ls, 'score': s, 'time': time, 'if_fra': history.if_fra}
                return render(request, 'question/your_score.html', context)
            return HttpResponse('请重新填写表单')
        if request.method == "POST":
            if num == 20:
                form = Form5(request.POST)
                print(request.POST)
                if form.is_valid():
                    answer = {}
                    answer[0] = form.cleaned_data['Kt1']
                    answer[1] = form.cleaned_data['Kt2']
                    answer[2] = form.cleaned_data['Kt3']
                    answer[3] = form.cleaned_data['Kt4']
                    answer[4] = form.cleaned_data['Kt5']
                    answer[5] = form.cleaned_data['Kt6']
                    answer[6] = form.cleaned_data['Kt7']
                    answer[7] = form.cleaned_data['Kt8']
                    answer[8] = form.cleaned_data['Kt9']
                    answer[9] = form.cleaned_data['Kt10']
                    answer[10] = form.cleaned_data['Kt11']
                    answer[11] = form.cleaned_data['Kt12']
                    answer[12] = form.cleaned_data['Kt13']
                    answer[13] = form.cleaned_data['Kt14']
                    answer[14] = form.cleaned_data['Kt15']
                    answer[15] = form.cleaned_data['Kt16']
                    answer[16] = form.cleaned_data['Kt17']
                    answer[17] = form.cleaned_data['Kt18']
                    answer[18] = form.cleaned_data['Kt19']
                    answer[19] = form.cleaned_data['Kt20']
                    history = History.objects.get(id=answer_id)
                    if history.end_time != None:
                        return HttpResponse('您已经提交过,请勿重复提交!')
                    history.__set_end_time__()
                    time = history.end_time - history.start_time
                    as_list = Answer.objects.filter(answer_id=history)
                    s, ot_ls = calculate(answer, as_list, num, if_fra=history.if_fra, history=history)
                    if s == 'False':
                        return HttpResponse('input string must be a string could be converted to float')
                    history.score = s
                    history.save()
                    context = {'output_list': ot_ls, 'score': s, 'time': time, 'if_fra': history.if_fra}
                    return render(request, 'question/your_score.html', context)
                return HttpResponse('请重新填写表单')
    return HttpResponse('非法的提交操作')


def youtube(request):
    if not request.session.get('is_login', None):
        return HttpResponse('您尚未登录,无法操作')
    user = User.objects.get(id=request.session.get('user_id', None))
    history = History.objects.filter(user=user)
    i = 0
    ot_ls = []
    while i < history.__len__():
        wa = WrongAnswer.objects.filter(answer_id=history[i])
        k = 0
        while k < wa.__len__():
            ot_ls.append(wa[k].question)
            k = k + 1
        i = i + 1
    return render(request, 'question/history.html', context={'output_list': ot_ls})


def calculate(answer, as_list, num, if_fra, history):
    i = 0
    s = num
    ot_ls = []
    while i < answer.__len__():
        if if_fra == True:
            if not answer[i] == as_list[i].question.answer_Fraction:
                if WrongAnswer.objects.filter(question=as_list[i].question):
                    s = s - 1
                else:
                    wrong = WrongAnswer.objects.create()
                    wrong.question = as_list[i].question
                    wrong.answer_id = history
                    ot_ls.append(as_list[i].question)
                    wrong.save()
                    s = s - 1
        else:
            try:
                float(answer[i])
            except:
                s = 'False'
                return s, ot_ls
            if not float(answer[i]) == float(as_list[i].question.answer_float):
                if WrongAnswer.objects.filter(question=as_list[i].question):
                    s = s - 1
                else:
                    wrong = WrongAnswer.objects.create()
                    wrong.question = as_list[i].question
                    wrong.answer_id = history
                    wrong.save()
                    ot_ls.append(as_list[i].question)
                    s = s - 1
        i = i + 1
    return s, ot_ls
