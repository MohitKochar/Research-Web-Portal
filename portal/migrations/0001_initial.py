# Generated by Django 2.0.6 on 2018-06-24 12:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_no', models.CharField(default='00XX0000', max_length=8)),
                ('applicant_name', models.CharField(max_length=250, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('caste', models.CharField(max_length=100, null=True)),
                ('residence_address', models.TextField(null=True)),
                ('college_name', models.CharField(max_length=500, null=True)),
                ('college_address', models.TextField(null=True)),
                ('mobile_no', models.IntegerField(null=True)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('applicant_photo', models.FileField(help_text='upload jpg, jpeg, png files only', null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])])),
                ('noc', models.FileField(help_text='upload pdf,jpg,jpeg,png files only with size less than 2mb', null=True, upload_to='')),
                ('caste_certificate', models.FileField(help_text='upload pdf,jpg,jpeg,png files only with size less than 2mb', null=True, upload_to='')),
                ('internship_type', models.CharField(default='Training', max_length=50, null=True)),
                ('duration', models.IntegerField(default=7, null=True)),
                ('slot', models.CharField(default='', max_length=250, null=True)),
                ('course', models.CharField(default='', max_length=250, null=True)),
                ('year_of_study', models.CharField(default='Third', max_length=10, null=True)),
                ('department', models.CharField(default='', max_length=250, null=True)),
                ('is_application_filled', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('remarks', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_no', models.CharField(max_length=8, null=True)),
                ('fee_receipt', models.FileField(help_text='upload pdf,jpg,jpeg,png files only with size less than 2mb', null=True, upload_to='')),
                ('fee_type', models.CharField(choices=[('O', 'Online'), ('C', 'Challan')], default='O', max_length=1)),
                ('transaction_no', models.CharField(max_length=20, null=True)),
                ('fees', models.FloatField(null=True)),
                ('paid_on', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('is_fees_paid', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('end_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('duration', models.IntegerField(default=7, null=True)),
                ('max_strength', models.IntegerField(default=10, null=True)),
                ('present_strength', models.IntegerField(default=0, null=True)),
                ('is_filled', models.BooleanField(default=False)),
            ],
        ),
    ]
