from django.contrib import admin
from .models import Post,Userprofile, Category, Tag, Comment

# class postAdmin(admin.ModelAdmin):
	
# 	view_on_site = True
# 	fieldsets = [
# 		(None, {'fields': ['title', 'text', 'author']}),
# 		('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),

# 	]
	
# 	list_display = ('title', 'author', 'published_date', 'created_date')
# 	list_filter = ['published_date']
# 	search_fields = ['title']

class PostAdmin(admin.ModelAdmin):
		
	view_on_site = True
	fieldsets = [
		(None, {'fields': ['title','slug', 'text', 'author', 'tag', 'category', 'cmnt']}),
		('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),

	]
	
	list_display = ('title', 'author', 'slug','published_date', 'created_date')
	list_filter = ['published_date']
	search_fields = ['title']
	filter_horizontal = ('tag',)
	prepopulated_fields = {'slug':("title",)}
	# readonly_fields=('slug',)


class CategoryAdmin(admin.ModelAdmin):
		
	# view_on_site = True
	fieldsets = [
		(None, {'fields': ['title','text','slug','parent']}),
		('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),

	]
	
	list_display = ('title', 'text','slug','parent', 'created_date')
	# list_filter = ['published_date']
	search_fields = ['title']
	# filter_horizontal = ('tag',)
	prepopulated_fields = {'slug':("title",)}

class TagAdmin(admin.ModelAdmin):
		
	# view_on_site = True
	fieldsets = [
		(None, {'fields': ['title','text','slug']}),
		('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),

	]
	
	list_display = ('title', 'text','slug','created_date')
	# list_filter = ['published_date']
	search_fields = ['title']
	# filter_horizontal = ('tag',)
	prepopulated_fields = {'slug':("title",)}

class CommentAdmin(admin.ModelAdmin):
		
	# view_on_site = True
	fieldsets = [
		(None, {'fields': ['post','name','text','slug','active','parent']}),
		('Date information', {'fields': ['created'], 'classes': ['collapse']}),

	]
	
	list_display = ('name', 'text','post','slug','created','updated')
	# list_filter = ['published_date']
	search_fields = ['name']
	# filter_horizontal = ('tag',)
	prepopulated_fields = {'slug':("name",)}


admin.site.register(Post,PostAdmin)
admin.site.register(Userprofile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment,CommentAdmin)
