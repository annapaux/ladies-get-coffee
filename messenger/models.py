from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')

    def __str__(self):
        return "Thread between {}, {}".format(self.user1, self.user2)


class UserThread(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return "Link of user {} to thread {}".format(self.user, self.thread)


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000, blank=False)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')

    def __str__(self):
        return "From {} to {}: {}".format(self.from_user, self.to_user, self.text)
