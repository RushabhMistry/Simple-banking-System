# from django import forms
# # from .models import Txnn

# class transferMoneyForm(forms.Form):
#     amount = forms.FloatField()
#     balance = forms.FloatField()
    
#     def clean_amount(self):
#         data1 = self.cleaned_data.get('amount')
#         data2 = self.cleaned_data.get('amount')
        
#         if data1 > data2:
#             raise forms.ValidationError('Amount must not be greater than available balance.')