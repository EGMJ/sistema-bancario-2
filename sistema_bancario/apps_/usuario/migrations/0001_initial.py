# Generated by Django 2.1.7 on 2019-04-05 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('cod_credito', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Debito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCredito',
            fields=[
                ('cod_estado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('cod_transferencia', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cod_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('num_cuenta', models.BigIntegerField(unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=12, unique=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('monto', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Rol')),
            ],
        ),
        migrations.AddField(
            model_name='transferencia',
            name='destino_cod_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencia_destino', to='usuario.Usuario'),
        ),
        migrations.AddField(
            model_name='transferencia',
            name='origen_cod_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencia_origen', to='usuario.Usuario'),
        ),
        migrations.AddField(
            model_name='debito',
            name='cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario'),
        ),
        migrations.AddField(
            model_name='credito',
            name='cod_estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.EstadoCredito'),
        ),
        migrations.AddField(
            model_name='credito',
            name='cod_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario'),
        ),
    ]
