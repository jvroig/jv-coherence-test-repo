# Generated by Django 3.2.14 on 2022-07-27 17:55

from django.db import migrations, models
from django.utils import timezone
import django.db.models.deletion

def load_first_poll(apps, schema_editor):
    Question = apps.get_model('polls', 'Question')
    q = Question(question_text="Default poll", pub_date=timezone.now())
    q.save()

    Choice = apps.get_model('polls', 'Choice')
    c = Choice(question_id=q.id, choice_text='Option 1', votes=0)
    c.save()
    c = Choice(question_id=q.id, choice_text='Option 2', votes=0)
    c.save()
    c = Choice(question_id=q.id, choice_text='Option 3', votes=0)
    c.save()

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_first_poll),
    ]
