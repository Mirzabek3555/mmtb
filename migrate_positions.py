from staff_app.models import Staff, Position
for staff in Staff.objects.all():
    display_name = staff.get_position_display()
    if display_name:
        position, _ = Position.objects.get_or_create(name=display_name)
        staff.new_position = position
        staff.save()
print("Data migrated successfully!")
