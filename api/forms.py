from django import forms

class TodoForm(forms.Form):

    title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'id' : 'title','name':'title'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'id' : 'date'}))
    status = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id' : 'status'}))

