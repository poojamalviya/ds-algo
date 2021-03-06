def carPooling(trip, cap):
    last = []
    for n, s, e in trip:
        last.append((s, n))
        last.append((e, -n))
    
    last.sort()
    curcapa =0 
    for cur in last:
        curcapa += cur[1]
        if curcapa> cap:
            return False
    return True

def carPooling1(trip, cap):
    lst = []
    for n, start, end in trips:
        lst.append((start, n))
        lst.append((end, -n))
    lst.sort()
    pas = 0
    for loc in lst:
        pas += loc[1]
        if pas > capacity:
            return False
    return True


# trips = [[2,1,5],[3,3,7]] 
# capacity = 4
trips = [[2,1,5],[3,3,7]] 
capacity = 5
# trips = [[2,1,5],[3,5,7]]
# capacity = 3

# trips = [[3,2,7],[3,7,9],[8,3,9]]
# capacity = 11

print carPooling(trips, capacity)
print carPooling1(trips, capacity)
def f(n):
    return (n<3) if n-1 else f(n-1) +f(n-2)
print f(5)

            if req_data.get("enable_bill_fetch", False):
                if type(req_data["enable_bill_fetch"]) != type(True):
                    self.response["res_str"] = "enable_bill_fetch is a Boolean field"
                    return send_400(self.response)  
                register_data["enable_bill_fetch"] = req_data["enable_bill_fetch"]
            if req_data.get("enable_recurring_pay", False):
                if type(req_data["enable_recurring_pay"]) != type(True):
                    self.response["res_str"] = "enable_recurring_pay is a Boolean field"
                    return send_400(self.response)
                register_data["enable_recurring_pay"] = req_data["enable_recurring_pay"]


                0042_auto_20200512_1353
                0045_auto_20201029_0405


# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2020-11-08 11:30
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TransactionEngine', '0042_auto_20200512_1353'),
        ('AccessControl', '0045_auto_20201029_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillPaymentTxn',
            fields=[
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('status', models.PositiveSmallIntegerField(choices=[(2, 'Initiated'), (1, 'Success'), (0, 'Failed')], default=2)),
                ('req_id', models.CharField(max_length=255)),
                ('bbps_payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('npci_payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_date', models.DateTimeField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('response_body', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
                ('is_reinitiated', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('bill_ref_id', models.CharField(db_index=True, max_length=255)),
                ('billing_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('due_date', models.DateTimeField()),
                ('billing_date', models.DateTimeField()),
                ('bill_number', models.CharField(max_length=255)),
                ('billing_period', models.CharField(max_length=255)),
                ('customer_name', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'INACTIVE'), (0, 'ACTIVE')], default=0)),
                ('additional_info', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegisteredBiller',
            fields=[
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('biller_id', models.CharField(db_index=True, max_length=255)),
                ('biller_name', models.CharField(db_index=True, max_length=255)),
                ('biller_nick_name', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('registration_id', models.CharField(max_length=255)),
                ('customer_params', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('category', models.CharField(db_index=True, max_length=255)),
                ('enable_bill_fetch', models.BooleanField(default=False)),
                ('enable_recurring_pay', models.BooleanField(default=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'INACTIVE'), (0, 'ACTIVE')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AccessControl.HappayUser')),
            ],
            options={
                'verbose_name_plural': 'Registered Billers',
            },
        ),
        migrations.AddField(
            model_name='bills',
            name='registered_biller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BbpsBill.RegisteredBiller'),
        ),
        migrations.AddField(
            model_name='billpaymenttxn',
            name='bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BbpsBill.Bills'),
        ),
        migrations.AddField(
            model_name='billpaymenttxn',
            name='initiated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AccessControl.HappayUser'),
        ),
        migrations.AddField(
            model_name='billpaymenttxn',
            name='payment_txn',
            field=models.ManyToManyField(blank=True, null=True, to='TransactionEngine.Transaction'),
        ),
    ]
