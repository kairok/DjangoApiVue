from django.db import models


from django.contrib.auth.models import User
# from djoser.urls.base import User



class Room(models.Model):
    #  Model Rooms

    creater = models.ForeignKey(User, verbose_name="Creater", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user" )
    date = models.DateTimeField("Date created", auto_now_add=True)


    class Meta:
        verbose_name="Class chat"
        verbose_name_plural="Class rooms"


class Chat(models.Model):
    #  Model chat
    room = models.ForeignKey(Room, verbose_name="Room chat", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Date created", auto_now_add=True)

    class Meta:
        verbose_name="Message chat"
        verbose_name_plural="Messages rooms"

