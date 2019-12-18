from django import forms


class DSform(forms.Form):
    quantity = forms.IntegerField(label="客官要几个题", min_value=0, max_value=50)
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
    operators = forms.MultipleChoiceField(label="客官来几个符号", choices=optr)
    if_pw = (
        ('True', "是"),
        ('False', "否"),
        ('Both', "我都要"),
    )
    if_ng = (
        ('True', "是"),
        ('False', "否"),
        ('Both', "我都要"),
    )
    if_fa = (
        ('True', "是"),
        ('False', "否"),
        ('Both', "我都要"),
    )
    potyp = (
        ('True', "^"),
        ('False', "**"),
    )
    if_pow = forms.ChoiceField(label="乘方", choices=if_pw)
    if_neg = forms.ChoiceField(label="负数", choices=if_ng)
    if_fra = forms.ChoiceField(label="分数", choices=if_fa)
    pow_type = forms.ChoiceField(label="类型", choices=potyp)
