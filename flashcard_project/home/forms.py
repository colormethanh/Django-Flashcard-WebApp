from django import forms
from .models import Set, Card 
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class SetForm(forms.ModelForm):

    class Meta:
        model = Set
        fields = ["name","owner"]

    def __init__(self, *args, **kwargs):
        super(SetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'post'
        self.helper.form_action = 'set_create'
        self.helper.add_input(Submit('submit','Submit'))

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ["front", "back"]

    def __init__(self, *args, **kwargs):
        super(CardForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'post'
        self.helper.form_action = 'card_create'
        self.helper.add_input(Submit('submit','Submit'))