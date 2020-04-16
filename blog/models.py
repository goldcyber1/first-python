from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse



#########################################################################
# 사용자 TB
#########################################################################
class TKjIndiRcmmAdmin(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    pswd = models.CharField(max_length=32, blank=True, null=True)
    kor_nm = models.CharField(max_length=20, blank=True, null=True)
    eng_nm = models.CharField(max_length=40, blank=True, null=True)
    org_div = models.CharField(max_length=40, blank=True, null=True)
    tel_offc = models.CharField(max_length=16, blank=True, null=True)
    tel_home = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    posi = models.CharField(max_length=50, blank=True, null=True)
    user_lv = models.CharField(max_length=5, blank=True, null=True)
    user_ip = models.CharField(max_length=32, blank=True, null=True)
    stat = models.CharField(max_length=2, blank=True, null=True)
    login_chk = models.CharField(max_length=2, blank=True, null=True)
    reg_user_id = models.CharField(max_length=20, blank=True, null=True)
    reg_dtm = models.DateField(blank=True, null=True)
    updt_user_id = models.CharField(max_length=20, blank=True, null=True)
    last_updt_dtm = models.DateField(blank=True, null=True)
    mba_cd = models.CharField(max_length=200, blank=True, null=True)
    cert_key = models.CharField(max_length=500, blank=True, null=True)
    accpt = models.CharField(max_length=20, blank=True, null=True)
    facl_cd = models.CharField(max_length=10, blank=True, null=True)
    facl_div = models.CharField(max_length=20, blank=True, null=True)
    reg_div = models.CharField(max_length=10, blank=True, null=True)
    depart = models.CharField(max_length=100, blank=True, null=True)
    agree = models.CharField(max_length=2, blank=True, null=True)

    def admn_save(self):
        self.save()
    
    def get_detail(self):
        return reverse('admin_detail', args=[self.user_id])
    
    def get_list(self):
        return reverse('admin_list')
        
    class Meta:
        managed = False
        db_table = 't_kj_indi_rcmm_admin'  

#########################################################################
# 계량관리 TB
#########################################################################   
class TKcVrfcReptdcAdmn(models.Model):
    mba_cd = models.CharField(primary_key=True, max_length=4)
    reptdc_no = models.IntegerField()
    reptdc_div = models.CharField(max_length=10, blank=True, null=True)
    rept_dtm = models.DateField(blank=True, null=True)
    strt_dt = models.CharField(max_length=8, blank=True, null=True)
    end_dt = models.CharField(max_length=8, blank=True, null=True)
    clos_dtm = models.DateField(blank=True, null=True)
    reptdc_line = models.IntegerField(blank=True, null=True)
    reptdc_stat = models.CharField(max_length=10, blank=True, null=True)
    reg_user_id = models.CharField(max_length=10, blank=True, null=True)
    reg_dtm = models.DateField(blank=True, null=True)
    updt_user_id = models.CharField(max_length=10, blank=True, null=True)
    last_updt_dtm = models.DateField(blank=True, null=True)
    admn_no = models.CharField(max_length=20, blank=True, null=True)
    apnd_no = models.CharField(max_length=20, blank=True, null=True)
    sbmt_dtm = models.CharField(max_length=8, blank=True, null=True)

    def reptdc_save(self):
        self.save()
    
    def get_detail(self):
        return reverse('insp_detail', args=[self.mba_cd, self.reptdc_no])
    
    def get_list(self):
        return reverse('insp_list')
        
    class Meta:
        managed = False
        db_table = 't_kc_vrfc_reptdc_admn'
        unique_together = (('mba_cd', 'reptdc_no'),)    
        