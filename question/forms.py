from django import forms


class DSform(forms.Form):
    qunt = (
        ('5', "给爷先来5个"),
        ('10', "少废话再来5个"),
        ('20', "20个让爷做到爽"),
    )
    quantity = forms.ChoiceField(label="想来几个题爽", choices=qunt)
    optr = (
        ('2', "简单难度2"),
        ('3', "简单难度3"),
        ('4', "简单难度4"),
        ('5', "中等难度5"),
        ('6', "中等难度6"),
        ('7', "中等难度7"),
        ('8', "小学生都哭了的难度8"),
        ('9', "小学生都哭了的难度9"),
    )
    operators = forms.MultipleChoiceField(label="爷来几个符号", choices=optr)
    if_pw = (
        ('True', "要"),
        ('False', "不要"),
        ('Both', "爷都要"),
    )
    if_ng = (
        ('True', "要"),
        ('False', "不要"),
        ('Both', "爷都要"),
    )
    if_fa = (
        ('True', "要"),
        ('False', "不要"),
    )
    potyp = (
        ('True', "^"),
        ('False', "**"),
    )
    if_pow = forms.ChoiceField(label="乘方", choices=if_pw)
    if_neg = forms.ChoiceField(label="负数", choices=if_ng)
    if_fra = forms.ChoiceField(label="分数", choices=if_fa)
    pow_type = forms.ChoiceField(label="类型", choices=potyp)


class Form5(forms.Form):
    Kt1 = forms.CharField(max_length=128)
    Kt2 = forms.CharField(max_length=128)
    Kt3 = forms.CharField(max_length=128)
    Kt4 = forms.CharField(max_length=128)
    Kt5 = forms.CharField(max_length=128)


class Form10(forms.Form):
    Kt1 = forms.CharField(max_length=128)
    Kt2 = forms.CharField(max_length=128)
    Kt3 = forms.CharField(max_length=128)
    Kt4 = forms.CharField(max_length=128)
    Kt5 = forms.CharField(max_length=128)
    Kt6 = forms.CharField(max_length=128)
    Kt7 = forms.CharField(max_length=128)
    Kt8 = forms.CharField(max_length=128)
    Kt9 = forms.CharField(max_length=128)
    Kt10 = forms.CharField(max_length=128)


class Form20(forms.Form):
    Kt1 = forms.CharField(max_length=128)
    Kt2 = forms.CharField(max_length=128)
    Kt3 = forms.CharField(max_length=128)
    Kt4 = forms.CharField(max_length=128)
    Kt5 = forms.CharField(max_length=128)
    Kt6 = forms.CharField(max_length=128)
    Kt7 = forms.CharField(max_length=128)
    Kt8 = forms.CharField(max_length=128)
    Kt9 = forms.CharField(max_length=128)
    Kt10 = forms.CharField(max_length=128)
    Kt11 = forms.CharField(max_length=128)
    Kt12 = forms.CharField(max_length=128)
    Kt13 = forms.CharField(max_length=128)
    Kt14 = forms.CharField(max_length=128)
    Kt15 = forms.CharField(max_length=128)
    Kt16 = forms.CharField(max_length=128)
    Kt17 = forms.CharField(max_length=128)
    Kt18 = forms.CharField(max_length=128)
    Kt19 = forms.CharField(max_length=128)
    Kt20 = forms.CharField(max_length=128)
