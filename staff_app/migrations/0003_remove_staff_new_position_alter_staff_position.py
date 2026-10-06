from django.db import migrations, models
import django.db.models.deletion

OLD_LABELS = [
    ('rahbar', "Bo'lim boshlig'i"),
    ('bosh_mutaxassis', 'Bosh mutaxassis'),
    ('mutaxassis', 'Mutaxassis'),
    ('inspektor', 'Inspektor'),
    ('metodist', 'Metodist'),
    ('boshqa', 'Boshqa'),
]


def copy_positions(apps, schema_editor):
    Staff = apps.get_model('staff_app', 'Staff')
    Position = apps.get_model('staff_app', 'Position')
    positions = {}
    for i, (key, label) in enumerate(OLD_LABELS):
        positions[key], _ = Position.objects.get_or_create(
            name=label, defaults={'order': i}
        )
    for staff in Staff.objects.all():
        pos = positions.get(staff.position)
        if pos:
            staff.new_position = pos
            staff.save(update_fields=['new_position'])


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0002_position_staff_new_position'),
    ]

    operations = [
        migrations.RunPython(copy_positions, migrations.RunPython.noop),
        migrations.RemoveField(model_name='staff', name='position'),
        migrations.RenameField(model_name='staff', old_name='new_position', new_name='position'),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='staff_app.position', verbose_name='Lavozim',
            ),
        ),
    ]