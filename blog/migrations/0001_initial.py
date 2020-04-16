# Generated by Django 3.0.3 on 2020-03-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TKcVrfcReptdcAdmn',
            fields=[
                ('mba_cd', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('reptdc_no', models.IntegerField()),
                ('reptdc_div', models.CharField(blank=True, max_length=10, null=True)),
                ('rept_dtm', models.DateField(blank=True, null=True)),
                ('strt_dt', models.CharField(blank=True, max_length=8, null=True)),
                ('end_dt', models.CharField(blank=True, max_length=8, null=True)),
                ('clos_dtm', models.DateField(blank=True, null=True)),
                ('reptdc_line', models.IntegerField(blank=True, null=True)),
                ('reptdc_stat', models.CharField(blank=True, max_length=10, null=True)),
                ('reg_user_id', models.CharField(blank=True, max_length=10, null=True)),
                ('reg_dtm', models.DateField(blank=True, null=True)),
                ('updt_user_id', models.CharField(blank=True, max_length=10, null=True)),
                ('last_updt_dtm', models.DateField(blank=True, null=True)),
                ('admn_no', models.CharField(blank=True, max_length=20, null=True)),
                ('apnd_no', models.CharField(blank=True, max_length=20, null=True)),
                ('sbmt_dtm', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 't_kc_vrfc_reptdc_admn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TKjIndiRcmmAdmin',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pswd', models.CharField(blank=True, max_length=32, null=True)),
                ('kor_nm', models.CharField(blank=True, max_length=20, null=True)),
                ('eng_nm', models.CharField(blank=True, max_length=40, null=True)),
                ('org_div', models.CharField(blank=True, max_length=40, null=True)),
                ('tel_offc', models.CharField(blank=True, max_length=16, null=True)),
                ('tel_home', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('posi', models.CharField(blank=True, max_length=50, null=True)),
                ('user_lv', models.CharField(blank=True, max_length=5, null=True)),
                ('user_ip', models.CharField(blank=True, max_length=32, null=True)),
                ('stat', models.CharField(blank=True, max_length=2, null=True)),
                ('login_chk', models.CharField(blank=True, max_length=2, null=True)),
                ('reg_user_id', models.CharField(blank=True, max_length=20, null=True)),
                ('reg_dtm', models.DateField(blank=True, null=True)),
                ('updt_user_id', models.CharField(blank=True, max_length=20, null=True)),
                ('last_updt_dtm', models.DateField(blank=True, null=True)),
                ('mba_cd', models.CharField(blank=True, max_length=200, null=True)),
                ('cert_key', models.CharField(blank=True, max_length=500, null=True)),
                ('accpt', models.CharField(blank=True, max_length=20, null=True)),
                ('facl_cd', models.CharField(blank=True, max_length=10, null=True)),
                ('facl_div', models.CharField(blank=True, max_length=20, null=True)),
                ('reg_div', models.CharField(blank=True, max_length=10, null=True)),
                ('depart', models.CharField(blank=True, max_length=100, null=True)),
                ('agree', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 't_kj_indi_rcmm_admin',
                'managed': False,
            },
        ),
    ]
