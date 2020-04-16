'''
Created on 2020. 3. 5.

@author: user
'''
from django import forms

from .models import TKjIndiRcmmAdmin, TKcVrfcReptdcAdmn

class TKjIndiRcmmAdminForm(forms.ModelForm):

    class Meta:
        model = TKjIndiRcmmAdmin
        fields = ('user_id', 'pswd','kor_nm', 'eng_nm','org_div', 
                  'tel_offc','tel_home', 'email', 'posi','user_lv', 'user_ip',
                  'stat','login_chk', 'reg_user_id', 'reg_dtm','updt_user_id', 'last_updt_dtm',
                  'mba_cd','accpt', 'facl_cd', 'facl_div','reg_div', 'depart','agree',)
        


class TKcVrfcReptdcAdmnForm(forms.ModelForm):

    mba_cd = forms.CharField(label='', widget=forms.TextInput(attrs={'size': '100px'}))
    reptdc_no = forms.CharField(label='', widget=forms.TextInput(attrs={'size': '50px', 'placeholder':'MBA코드'}))
    reptdc_div = forms.CharField(label='', widget=forms.TextInput(attrs={'size': '30px', 'placeholder':'MBA코드'}))
    
    class Meta:
        model = TKcVrfcReptdcAdmn
        fields = ['mba_cd', 'reptdc_no','reptdc_div', 'rept_dtm', 'reg_dtm',
                  'last_updt_dtm']
