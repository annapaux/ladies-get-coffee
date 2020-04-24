from django.contrib import admin
from messenger.models import Message, Thread, UserThread

admin.site.register(Message)
admin.site.register(Thread)
admin.site.register(UserThread)
