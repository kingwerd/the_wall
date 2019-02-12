from django.db import models
# use dot dot to go up a level and then down into the app that you are trying to reach
from ..login_register.models import User as user_model

class MessageManager(models.Manager):
    def post_message(self, message, user_id):
        Message.objects.create(message=message, user=user_model.objects.get(id=user_id))

class CommentManager(models.Manager):
    def post_comment(self, comment, user_id, message_id):
        Comment.objects.create(comment=comment, message=Message.objects.get(id=message_id), user=user_model.objects.get(id=user_id))

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(user_model, related_name="messages", on_delete=models.CASCADE)
    objects = MessageManager()

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(user_model, related_name="comments", on_delete=models.CASCADE)
    objects = CommentManager()