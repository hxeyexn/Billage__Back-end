# Generated by Django 4.0.6 on 2022-07-09 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board_comments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField()),
                ('board_id', models.ForeignKey(db_column='board_id', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='board.board')),
                ('comment_id', models.ForeignKey(db_column='comment_id', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='board.board_comments')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
