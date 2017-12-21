from django.db import models

# Create your models here.
class Blog_category(models.Model):
    cat_title = models.CharField(max_length=250, blank=False, null=False)
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_title

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["-date_created"]

