from __future__ import absolute_import, unicode_literals
from django.db.models.signals import post_delete
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings


class MyFile(models.Model):
    description = models.CharField('Name', max_length=80)
    file = models.FileField(
        upload_to='myfile/files', verbose_name='File',
        null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'My File'
        verbose_name_plural = 'My Files'
        ordering = ['-created_at']

    def __str__(self):
        return self.description


def delete_all(time_ago="all"):
    if time_ago == "all":
        time_ago = timezone.now()
    ok = MyFile.objects.filter(created_at__lte=time_ago).delete()
    return ok


# Signal to delete the file of image when your register in the database will be deleted.
@receiver(post_delete, sender=MyFile)
def image_post_delete_handler(sender, **kwargs):
    listingFiles = kwargs['instance']
    storage = listingFiles.file.storage
    if settings.USE_S3:
        path = str(listingFiles.file)
    else:
        path = listingFiles.file.path
    storage.delete(path)
