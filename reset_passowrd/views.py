import datetime
import pytz
from django.shortcuts import render, redirect
from .forms import UserForm, UserPass, UserCode
from login.models import User
from .models import ConfirmString
from django.conf import settings
import hashlib


def make_confirm_string(user):
    from uuid import uuid4
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = str(uuid4())
    ConfirmString.objects.create(code=code, user=user)
    return code


def post(request):
    if request.session.get('user_id', None):
        user_id = request.session.get('user_id', None)
        user = User.objects.get(id=user_id)
        message = ''
        if ConfirmString.objects.filter(user=user):
            confirm = ConfirmString.objects.get(user=user)
            confirm.delete()
            code = make_confirm_string(user)
            send_email(user.email, code)
            message = '邮件已发送,请前往您预留的邮箱地址确认'
            usercode_form = UserForm()
            return render(request, 'reset_passowrd/reset.html', locals())
        else:
            code = make_confirm_string(user)
            send_email(user.email, code)
            message = '邮件已发送,请前往您预留的邮箱地址确认'
            usercode_form = UserForm()
            return render(request, 'reset_passowrd/reset.html', locals())
    else:
        message = '请输入您的用户名'
        username_form = UserForm()
        return render(request, 'reset_passowrd/confirm.html', locals())


def user_confirm(request):
    if request.session.get('is_login', None):
        return redirect('SouSouSou:main')
    if request.method == "POST":
        message = ''
        username_form = UserForm(request.POST)
        if username_form.is_valid():
            username = username_form.cleaned_data['username']
            if User.objects.filter(name=username):
                user = User.objects.get(name=username)
                request.session['user_id'] = user.id
                if ConfirmString.objects.filter(user=user):
                    return render(request, 'reset_passowrd/_message.html', locals())
                code = make_confirm_string(user)
                send_email(user.email, code)
                message = '邮件已发送,请前往您预留的邮箱地址确认'
                usercode_form = UserCode()
                return render(request, 'reset_passowrd/reset.html', locals())
            else:
                message = '用户不存在,请确认您输入的用户名'
        return render(request, 'reset_passowrd/confirm.html', locals())
    username_form = UserForm()
    return render(request, 'reset_passowrd/confirm.html', locals())


def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives
    subject = '来自猿题库的密码确认邮件'
    text_content = '''如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员!'''
    html_content = '''
                        <p>感谢使用</p>
                        <p>请返回站点链接完成修改密码确认！</p>
                        <p>您的验证id为{}</p>
                        <p>此链接有效期为{}天！</p>
                        '''.format(code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def user_reset(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect('SouSouSou:main')
    if request.method == "POST":
        if request.session.get('user_id', None):
            usercode_form = UserCode(request.POST)
            if usercode_form.is_valid():
                code = usercode_form.cleaned_data['usercode']
                if ConfirmString.objects.filter(code=code):
                    confirm = ConfirmString.objects.get(code=code)
                    c_time = confirm.c_time
                    now = datetime.datetime.now()
                    now = now.replace(tzinfo=pytz.timezone('UTC'))
                    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
                        confirm.user.delete()
                        username_form = UserForm()
                        message = '您的邮件已经过期！请重新提申请!'
                        return render(request, 'reset_passowrd/confirm.html', locals())
                    else:
                        if confirm.user.id == request.session.get('user_id', None):
                            request.session['allowance'] = 'allowed'
                            userpass_form = UserPass()
                            return render(request, 'reset_passowrd/pass.html', locals())
                        else:
                            message = '用户名不匹配,危险'
                            username_form = UserForm()
                            return render(request, 'reset_passowrd/confirm.html', locals())
                else:
                    message = '无效的确认请求!'
                    usercode_form = UserCode()
                    return render(request, 'reset_passowrd/reset.html', locals())
        else:
            message = '你是谁?!?!'
            return render(request, 'reset_passowrd/confirm.html', locals())
    usercode_form = UserCode()
    return render(request, 'reset_passowrd/reset.html', locals())


def user_changepass(request):
    if request.session.get('allowance', None) == 'allowed':
        if request.method == 'POST':
            userpass_form = UserPass(request.POST)
            if userpass_form.is_valid():
                password1 = userpass_form.cleaned_data['password1']
                password2 = userpass_form.cleaned_data['password2']
                if password1 != password2:  # 判断两次密码是否相同
                    message = "两次输入的密码不同！"
                    return render(request, 'reset_passowrd/pass.html', locals())
                else:
                    user = User.objects.get(id=request.session.get('user_id', None))
                    user.password = hash_code(password1)
                    user.save()
                    confirm = ConfirmString.objects.get(user=user)
                    confirm.delete()
                    message = '修改密码成功,请登录'
                    return redirect('/login', locals())
        else:
            userpass_form = UserPass()
            return render(request, 'reset_passowrd/pass.html', locals())
    else:
        return render(request, 'reset_passowrd/confirm.html', locals())


def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()
