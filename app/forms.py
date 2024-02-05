from django import forms
g=[['FEMALE','Female'],['MALE','Male']]
c=[['python','python'],('DJANGO','DJANGO'),['sql','sql']]
class NameForm(forms.Form):
    sname=forms.CharField()
    sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    