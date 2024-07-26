from django.core.management.base import BaseCommand
from bookings.models import Table, MenuItem

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        try:
            # Create tables if they don't already exist
            if Table.objects.exists():
                self.stdout.write(self.style.WARNING('Tables already exist. Skipping table creation.'))
            else:
                for i in range(1, 11):  # Create 10 tables
                    capacity = 2 if i <= 5 else 4  # 5 tables for 2, 5 tables for 4
                    Table.objects.create(number=i, capacity=capacity)
                self.stdout.write(self.style.SUCCESS('Successfully created tables'))

            # Create menu items if they don't already exist
            if MenuItem.objects.exists():
                self.stdout.write(self.style.WARNING('Menu items already exist. Skipping menu item creation.'))
            else:
                menu_items = [
                    {'name': 'Jollof Rice', 'description': 'Spicy rice dish with vegetables', 'price': 12.99},
                    {'name': 'Fufu with Light Soup', 'description': 'Cassava dough with spicy soup', 'price': 14.99},
                    {'name': 'Waakye', 'description': 'Rice and beans with spicy sauce', 'price': 11.99},
                    {'name': 'Kelewele', 'description': 'Spicy fried plantains', 'price': 8.99},
                    {'name': 'Banku with Tilapia', 'description': 'Fermented corn dough with grilled fish', 'price': 16.99},
                ]

                for item in menu_items:
                    MenuItem.objects.create(**item)
                
                self.stdout.write(self.style.SUCCESS('Successfully created menu items'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {str(e)}'))
