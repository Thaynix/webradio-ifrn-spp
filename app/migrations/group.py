from django.db import migrations


def make_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    groups = ["Orientador", "Bolsista"]

    for group in groups:
        Group.objects.get_or_create(name=group)

class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(make_groups)
    ]