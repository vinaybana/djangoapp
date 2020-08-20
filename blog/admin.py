from django.contrib import admin
from .models import Post

class postAdmin(admin.ModelAdmin):
	
	view_on_site = True
	fieldsets = [
		(None, {'fields': ['title', 'text', 'author']}),
		('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),

	]
	
	list_display = ('title', 'author', 'published_date', 'created_date')
	list_filter = ['published_date']
	search_fields = ['title']


admin.site.register(Post,postAdmin)
# Register your models here.
