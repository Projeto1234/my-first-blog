from django.contrib import admin
from .models import Post
from .models import Musico
from .models import Musica
from .models import Album

admin.site.register(Post)
# Register your models here.

admin.site.register(Musico)
admin.site.register(Musica)
admin.site.register(Album)