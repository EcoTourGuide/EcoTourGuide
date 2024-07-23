from django.core.management.base import BaseCommand
from home.models import TravelDestination
from Filter.models import UnsplashImage

class Command(BaseCommand):
    help = 'Assign 3 Unsplash images to each TravelDestination'

    def handle(self, *args, **kwargs):
        destinations = TravelDestination.objects.all()
        unsplash_images = list(UnsplashImage.objects.all())

        if len(unsplash_images) < len(destinations) * 3:
            self.stdout.write(self.style.ERROR('Not enough images in UnsplashImage table'))
            return

        image_index = 0
        for destination in destinations:
            # Ensure we have enough images to assign
            if image_index + 3 > len(unsplash_images):
                self.stdout.write(self.style.ERROR(f'Not enough images to assign to {destination.prop_name}'))
                break

            # Assign 3 images to each TravelDestination
            destination.image1 = unsplash_images[image_index].image_url
            destination.image2 = unsplash_images[image_index + 1].image_url
            destination.image3 = unsplash_images[image_index + 2].image_url
            destination.save()

            image_index += 3

            self.stdout.write(self.style.SUCCESS(f'Assigned images to {destination.designation_num}'))

        self.stdout.write(self.style.SUCCESS('Successfully assigned images to all travel destinations'))
