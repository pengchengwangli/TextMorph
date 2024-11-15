# management/commands/clear_expired_downloads.py

from django.core.management.base import BaseCommand
from user.models import DownloadHistory
from django.utils import timezone

class Command(BaseCommand):
    help = 'Clear expired download history records'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_downloads = DownloadHistory.objects.filter(expires_at__lt=now)
        count = expired_downloads.count()
        expired_downloads.delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} expired download history records'))