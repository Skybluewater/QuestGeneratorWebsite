from django import forms


class DSform(forms.ModelForm):
    quantity = forms.IntegerField(label="要几个")

    optr = (
        ('2', "简单难度2"),
        ('3', "简单难度3"),
        ('4', "4"),
        ('5', "5"),
        ('6', "6"),
        ('7', "7"),
    )
    operators = forms.ChoiceField(label="客官来几个符号", choices=optr)
    if_pw = (
        ('True', "是"),
        ('False', "否"),
    )
    if_ng = (
        ('True', "是"),
        ('False', "否"),
    )
    if_fa = (
        ('True', "是"),
        ('False', "否"),
    )
    potyp = (
        ('True', "^"),
        ('False', "**"),
    )
    if_pow = forms.ChoiceField(label="乘方", choices=if_pw)
    if_neg = forms.ChoiceField(label="负数", choices=if_ng)
    if_fra = forms.ChoiceField(label="分数", choices=if_fa)
    pow_type = forms.ChoiceField(label="类型", choices=potyp)
