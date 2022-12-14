from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User  # Blog author or commenter


# Create your models here.
class blog_author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    summary = models.TextField(max_length=1000, help_text="Enter your biography")

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class blog(models.Model):
    title = models.CharField(max_length=200)
    blog_author = models.ForeignKey('blog_author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=15000, help_text="Enter your blog")
    date_of_publication = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_of_publication"]

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class blog_comment(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE)
    blog_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        len_title = 75

        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring
