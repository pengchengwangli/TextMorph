import os
from django.conf import settings
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = '清理 media 文件夹中的过期文件'

    def handle(self, *args, **kwargs):
        media_dir = settings.MEDIA_ROOT
        expiration_time = datetime.now() - timedelta(days=1)
        # 遍历 media 文件夹中的所有目录和文件，删除最后修改时间早于 expiration_time 的文件及其目录
        for root, dirs, files in os.walk(media_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_mtime < expiration_time:
                    os.remove(file_path)
            if not os.listdir(root):
                os.rmdir(root)
        self.stdout.write(self.style.SUCCESS('Successfully cleaned up media folder'))
# 该命令会在 media 文件夹中删除所有最后修改时间早于一天前的文件及其目录。

