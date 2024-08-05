from django.core.management.base import BaseCommand
from bookings.models import Table, MenuItem
from django.core.files import File
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        try:
            # Update or create tables
            for i in range(1, 11):
                capacity = 2 if i <= 5 else 4  # 5 tables for 2, 5 tables for 4
                Table.objects.update_or_create(
                    number=i,
                    defaults={'capacity': capacity}
                )
            self.stdout.write(self.style.SUCCESS('Successfully updated or created tables'))

            # Update or create menu items
            menu_items = [
                {'name': 'Jollof Rice', 'description': 'Spicy rice dish with assorted vegetables', 'price': 12.99, 'image': 'jollof_rice.jpg'},
                {'name': 'Fufu with Light Soup', 'description': 'Cassava dough with spicy vegetable soup', 'price': 14.99, 'image': 'fufu_light_soup.jpg'},
                {'name': 'Waakye', 'description': 'Rice and beans with spicy vegetable sauce', 'price': 11.99, 'image': 'waakye.jpg'},
                {'name': 'Kelewele', 'description': 'Spicy fried plantains', 'price': 8.99,  'image': 'kelewele.jpg'},
                {'name': 'Banku with Tilapia', 'description': 'Fermented corn dough with grilled fish', 'price': 16.99, 'image': 'banku_tilapia.jpg'},
            ]

            for item in menu_items:
                menu_item, created = MenuItem.objects.update_or_create(
                    name=item['name'],
                    defaults={
                        'description': item['description'],
                        'price': item['price']
                    }
                )
                
                image_path = os.path.join('static', 'images', item['image'])
                self.stdout.write(f"Checking for image: {image_path}")
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        menu_item.image.save(item['image'], File(f), save=True)
                    self.stdout.write(self.style.SUCCESS(f"Image found and saved: {item['image']}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Image not found: {image_path}"))
            
            self.stdout.write(self.style.SUCCESS('Successfully updated or created menu items'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {str(e)}'))