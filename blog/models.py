from django.db import models
from django.utils import timezone
from markdown_deux import markdown
from django.utils.safestring import mark_safe

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=7000)
    email = models.EmailField(default='')
    date_published = models.DateTimeField(default=timezone.now)
    author = models.CharField(default='', max_length=50)
    about_the_author = models.TextField(max_length = 700)
    author_image = models.ImageField(default='user.png', upload_to='author_images', blank=True)
    blog_image = models.ImageField(default='default.jpg', upload_to='blog_images', blank=True)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    def content_markdown(self):
        content = self.content
        return mark_safe(markdown(content))

    def author_markdown(self):	
        content = self.about_the_author
        return mark_safe(markdown(content))

    def get_next_post(self):
        next_post = self.get_next_by_date_published()
        if next_post:
        	return next_post
        return False   	

    def get_prev_post(self):
        prev_post = self.get_previous_by_date_published()
        if prev_post:
        	return prev_post
        return False   
