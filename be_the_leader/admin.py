from asyncio import events
from django.contrib import admin
from .models import Events, Partner, Gallery, WhatWeDo, Message

# Register your models here.

admin.site.register(Events)
admin.site.register(Partner)
admin.site.register(Gallery)
admin.site.register(WhatWeDo)
admin.site.register(Message)

