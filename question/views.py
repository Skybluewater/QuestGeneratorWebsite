from django.shortcuts import render, HttpResponse
from login.models import User
from .forms import DSform, Form5
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
            g_form = Form5()
            context = {'output_list': ot_ls, 'form': g_form, 'answer_id': id}
            return render(request, 'question/Question_list.html', context)
    form = DSform()
    context = {'form': form}
    return render(request, 'question/Question.html', context)


def confirm(request, num, answer_id):
    if request.method == "POST":
        if num == 5:
            form = Form5(request.POST)
            print(request.POST)
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
                i = 0
                s = 5
                ot_ls = []
                while i < answer.__len__():
                    if history.if_fra == True:
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
                history.score = s
                history.save()
                context = {'output_list': ot_ls, 'score': s, 'time': time, 'if_fra': history.if_fra}
                return render(request, 'question/your_score.html', context)
            return HttpResponse('请重新填写表单')
    return HttpResponse('非法的提交操作')
