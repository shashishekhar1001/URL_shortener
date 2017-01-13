from django.core.management.base import BaseCommand, CommandError

from shortener.models import Shortener_URL

class Command(BaseCommand):
    help = 'Refreshes all Shortener_URL shortcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return Shortener_URL.objects.refresh_shortcodes()