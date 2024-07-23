import requests
from django.core.management.base import BaseCommand
from Filter.models import UnsplashImage
from django.conf import settings
import environ

env = environ.Env()
environ.Env.read_env()


class Command(BaseCommand):
    help = 'Fetch hotel-related images from Unsplash API and store them in the database'

    def handle(self, *args, **kwargs):
        access_key = 'IB78nN-9bvvedpmw0axHxEj3q7GHBKPmlGnd1zwV0Go'
        url = 'https://api.unsplash.com/search/photos'
        headers = {'Authorization': f'Client-ID {access_key}'}
        query = 'hotel'
        page = 1
        total_images = 0

        # Ensure we start fresh
        UnsplashImage.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Old image data removed'))

        while total_images < 800:
            response = requests.get(url, headers=headers, params={'query': query, 'page': page, 'per_page': 30})
            data = response.json()

            if 'results' not in data:
                self.stdout.write(self.style.ERROR(f'Error fetching images: {data}'))
                break

            for item in data['results']:
                unsplash_image_id = item['id']
                image_url = item['urls']['full']

                if not UnsplashImage.objects.filter(unsplash_image_id=unsplash_image_id).exists():
                    UnsplashImage.objects.create(unsplash_image_id=unsplash_image_id, image_url=image_url)
                    total_images += 1

                if total_images >= 800:
                    break

            page += 1
            self.stdout.write(self.style.SUCCESS(f'Fetched {total_images} images'))

        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored 800 hotel-related images'))
