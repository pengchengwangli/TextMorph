from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    is_vip = models.BooleanField(default=False, verbose_name='是否是VIP')
    def __str__(self):
        return self.username

    def set_vip(self):
        self.is_vip = True
        self.save()

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class DownloadHistory(models.Model):
    download_time = models.DateTimeField(auto_now_add=True, verbose_name='下载时间')
    url = models.URLField(verbose_name='下载链接')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='用户')
    expires_at = models.DateTimeField(default=timezone.now() + timedelta(days=1), verbose_name='过期时间')

    class Meta:
        db_table = 'tb_download_history'
        verbose_name = '下载历史'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.url} downloaded at {self.download_time}"
