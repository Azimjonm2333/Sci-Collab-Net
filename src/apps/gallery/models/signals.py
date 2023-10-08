# from django.db.models.signals import pre_delete, pre_save
# from django.dispatch import receiver
# import os
# from .models import Image
#
#
# @receiver(pre_delete, sender=Image)
# def delete_image_on_pre_delete(sender, instance, **kwargs):
#     instance.original.delete(False)
#     instance.thumbnail.delete(False)
#
#
# @receiver(pre_save, sender=Image)
# def delete_old_image_on_pre_save(sender, instance, **kwargs):
#     try:
#         old_instance = sender.objects.get(id=instance.id)
#         old_original = old_instance.original.path
#         old_thumbnail = old_instance.thumbnail.path
#
#         new_original = instance.original.path if instance.original else None
#         new_thumbnail = instance.thumbnail.path if instance.thumbnail else None
#
#         if new_original != old_original:
#             if os.path.exists(old_original):
#                 os.remove(old_original)
#
#         if new_thumbnail != old_thumbnail:
#             if os.path.exists(old_thumbnail):
#                 os.remove(old_thumbnail)
#     except Image.DoesNotExist:
#         pass