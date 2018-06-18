from django.core.management import BaseCommand

from LinksList.models import update_sites


class Command(BaseCommand):
    help = 'Update the status off all sites'

    def handle(self, *args, **options):
        update_sites()
