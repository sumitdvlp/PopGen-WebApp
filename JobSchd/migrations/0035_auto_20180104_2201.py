# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-04 22:01
from __future__ import unicode_literals

import JobSchd.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0034_auto_20180104_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfinal',
            name='Job_Pushed',
            field=models.BooleanField(default=False, help_text='If the Job is configured, Your updates will not be reflected , Make another Job', verbose_name='Submit'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='desc',
            field=models.CharField(default='Connecticut TAZ Scenario', help_text='For Eg. Connecticut TAZ Scenario', max_length=50, verbose_name='Scenario Description'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='entities',
            field=models.CharField(default='[household, groupquarter, person]', help_text='Eg. [household, groupquarter, person]', max_length=500, verbose_name='Entities'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='entity_one',
            field=models.CharField(default='household', help_text='Eg. household or person', max_length=50, verbose_name='Entity'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='entity_two',
            field=models.CharField(default='person', help_text='For Eg. household or person', max_length=50, verbose_name='Entity'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='filename_one',
            field=models.CharField(default='hhsize_income.csv', help_text='Eg. hhsize_income.csv', max_length=50, verbose_name='Filename'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='filename_two',
            field=models.CharField(default='hhsize_income.csv', help_text='For Eg. hhsize_income.csv', max_length=50, verbose_name='Filename'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='filetype_one',
            field=models.CharField(default='csv', help_text='Eg. csv', max_length=50, verbose_name='Filetype'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='filetype_two',
            field=models.CharField(default='csv', help_text='For Eg. csv', max_length=50, verbose_name='Filetype'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo',
            field=models.CharField(default='geo', help_text='For TAZ Eg. geo', max_length=50, verbose_name='Groupquarter Entity Name'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_groupquarter',
            field=models.CharField(default='', help_text='For eg. [gqtotals, gqtype]', max_length=50, verbose_name='Geo Groupquarter'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_groupquarter_files',
            field=models.FileField(blank=True, help_text='groupquarters_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Geo Groupquarter File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_household',
            field=models.CharField(default='', help_text='For eg. [hhtotals, hinc, hsize]', max_length=50, verbose_name='Geo Household'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_household_files',
            field=models.FileField(blank=True, help_text='household_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Geo Household File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_ids',
            field=models.CharField(default='[1,2,3]', help_text='For Eg. [1,2,3,4,5,6,7,8,9,10,11,12,13,14]', max_length=3000, verbose_name='Geo Ids'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_person',
            field=models.CharField(default='', help_text='For eg. [pworker, ptotals] ', max_length=50, verbose_name='Geo Person'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_person_files',
            field=models.FileField(blank=True, help_text='person_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Geo Person File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_to_sample',
            field=models.FileField(blank=True, help_text='geo_sample_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='geo to Sample File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='hid',
            field=models.CharField(default='hid', help_text='Eg. hhld', max_length=50, verbose_name='Household Entity Name'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='housing_entities',
            field=models.CharField(default='[household, groupquarter]', help_text='Eg. [household, groupquarter]', max_length=500, verbose_name='Housing Entities'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='job_name',
            field=models.CharField(help_text='Eg. Connecticut_Run', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='multiway_variables_one',
            field=models.CharField(default='[hsize, hinc]', help_text='For Eg. [hsize, hinc]', max_length=50, verbose_name='Multiway Variables'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='multiway_variables_two',
            field=models.CharField(default='[hsize, hinc]', help_text='For Eg. [hsize, hinc]', max_length=50, verbose_name='Multiway Variables'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='performance',
            field=models.CharField(default='[ipf, reweighting, drawing]', help_text='For Eg.[ipf, reweighting, drawing]', max_length=50, verbose_name='Performance'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='person_entities',
            field=models.CharField(default='[person]', help_text='Eg. [person]', max_length=500, verbose_name='Person Entities'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='pid',
            field=models.CharField(default='pid', help_text='Eg. person', max_length=50, verbose_name='Person Entity Name'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='project_name',
            field=models.CharField(help_text='Eg. Connecticut_Synthetic_Population', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region',
            field=models.CharField(default='region', help_text='For County Eg. region', max_length=50, verbose_name='Aggregate Spatial Unit'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_groupquarter',
            field=models.CharField(default='', help_text='For eg. [gqrtotals]', max_length=50, verbose_name='Region Groupquarter'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_groupquarter_files',
            field=models.FileField(blank=True, help_text='region_groupquarters_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Region Groupquarter File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_household',
            field=models.CharField(default='', help_text='For eg. [hhrtotals]', max_length=50, verbose_name='Region Household'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_household_files',
            field=models.FileField(blank=True, help_text='region_household_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Region Household File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_ids',
            field=models.CharField(default='[1,2,3]', help_text='For Eg. [1,2,3,4,5,6,7,8,9,10,11,12,13,14]', max_length=50, verbose_name='Region Ids'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_person',
            field=models.CharField(default='', help_text='For eg. [rpsex, rpage, rpworker, prtotals]', max_length=50, verbose_name='Region Person'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_person_files',
            field=models.FileField(blank=True, help_text='region_person_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Region Person File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_to_geo',
            field=models.FileField(blank=True, help_text='region_geo_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='region to Geo File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_to_sample',
            field=models.FileField(blank=True, help_text='region_sample_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='region to Sample File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='rp',
            field=models.CharField(choices=[('bucket', 'Bucket')], default='bucket', max_length=50, verbose_name='Rounding Procedure'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='sample_geo',
            field=models.CharField(default='sample_geo', help_text='For TAZ Eg. sample_geo', max_length=50, verbose_name='Disaggregate Spatial Unit'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='sample_groupquarter',
            field=models.FileField(blank=True, help_text='groupquarters_sample.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Sample Groupquarter File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='sample_household',
            field=models.FileField(blank=True, help_text='household_sample.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Sample Household File'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='sample_person',
            field=models.FileField(blank=True, help_text='person_sample.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Sample Person File'),
        ),
    ]