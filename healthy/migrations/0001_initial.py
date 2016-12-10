# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 08:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Date')),
                ('ref_number', models.IntegerField(verbose_name='Reference Number')),
                ('doctor', models.CharField(blank=True, max_length=300, null=True, verbose_name='Doctor')),
                ('collection_point', models.CharField(blank=True, max_length=500, null=True, verbose_name='Collection point')),
                ('patient_code', models.IntegerField(null=True, verbose_name='Patient Code')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='LabNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('lab_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lab_LabNote_ref', to='healthy.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, default=0, max_digits=10, null=True, verbose_name='Value')),
                ('lab_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lab_ref', to='healthy.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Leucocite(WBC)', 'Leucocite(WBC)'), ('Hematii(RBC)', 'Hematii(RBC)'), ('Hemoglobina(HGB)', 'Hemoglobina(HGB)'), ('VEM(volum eritocitar mediu)', 'VEM(volum eritocitar mediu'), ('HEM(hemoglobina eritocitara medie)', 'HEM(hemoglobina eritocitara medie)'), ('CHEM(conc HB eritocitara medie)', 'CHEM(conc HB eritocitara medie)'), ('RDW', 'RDW'), ('Trombocite(PLT)', 'Trombocite'), ('MPW', 'MPW'), ('PDW', 'PDW'), ('Neutro', 'Neutro'), ('Lym', 'Lym'), ('Monocite', 'Monocite'), ('Eozinofile', 'Eozinofile'), ('Bazofile', 'Bazofile'), ('Creatinina serica', 'Creatinina serica'), ('Magneziu seric', 'Magneziu seric'), ('Sideremie', 'Sideremie'), ('Glicemie', 'Glicemie'), ('TGP', 'TGP'), ('TSH', 'TSH'), ('FT4', 'FT4')], default='Leucocite(WBC)', max_length=100, verbose_name='Name')),
                ('abbr', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abbreviation')),
                ('category', models.CharField(choices=[('Hematologie', 'Hematologie'), ('Biochimie', 'Biochimie'), ('Dozari hormonale, Imunologie si markeri tumorali (Chemiluminiscenta)', 'Dozari hormonale, Imunologie si markeri tumorali (Chemiluminiscenta)')], default='Hematologie', max_length=100, verbose_name='Category')),
                ('um', models.CharField(choices=[('10^3/mm3', '10^3/mm3'), ('10^6/mm3', '10^6/mm3'), ('g/dl', 'g/dl'), ('%', '%'), ('fL', 'fL'), ('mg/dl', 'mg/dl'), ('U\\L', 'U\\L'), ('μUI\\ml', 'μUI\\ml'), ('ng/dl', 'ng/dl')], default='10^3/mm3', max_length=10, verbose_name='Unit')),
            ],
        ),
        migrations.CreateModel(
            name='MarkerPredefined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold_min', models.DecimalField(decimal_places=3, default=0, max_digits=10, null=True, verbose_name='Min Value')),
                ('threshold_max', models.DecimalField(decimal_places=3, default=0, max_digits=10, null=True, verbose_name='Max Value')),
                ('marker_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Marker_MarkerPredefined_ref', to='healthy.Marker')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('F', 'F'), ('M', 'M')], default='F', max_length=5)),
                ('dob', models.DateField(null=True, verbose_name='Date of birth')),
                ('blood_type', models.CharField(choices=[('Group A', 'Group A'), ('Group B', 'Group B'), ('Group AB', 'Group AB'), ('Group 0', 'Group 0'), ('N', 'N')], default='N', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='labresult',
            name='marker_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Marker_LabResults_ref', to='healthy.Marker', verbose_name='Marker'),
        ),
        migrations.AddField(
            model_name='labresult',
            name='predefined_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MarkerPredefined_LabResults_ref', to='healthy.MarkerPredefined'),
        ),
        migrations.AddField(
            model_name='labresult',
            name='user_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='marker_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Marker_Dictionary_ref', to='healthy.Marker'),
        ),
    ]