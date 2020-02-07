# Generated by Django 2.1 on 2018-08-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumoRateioHorasGns',
            fields=[
                ('id_tipo', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('id_atividade', models.IntegerField()),
                ('descricao', models.CharField(max_length=100)),
                ('des_item_contabil', models.CharField(max_length=100)),
                ('id_ic', models.CharField(max_length=10)),
                ('descricao_ic', models.CharField(max_length=100)),
                ('periodo', models.CharField(max_length=15)),
                ('qtd_horas', models.FloatField()),
            ],
            options={
                'db_table': 'painel_rateio_horas_gns_logstash',
                'managed': False,
            },
        ),
    ]
