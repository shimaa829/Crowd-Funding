# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from projects.models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)

admin.site.register(Tag)
admin.site.register(Donation)
admin.site.register(CommentReport)
admin.site.register(ProjectReport)
admin.site.register(ProjectPicture)
