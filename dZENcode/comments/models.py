import re

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

ALLOWED_TAGS = ['a', 'code', 'i', 'strong']


class Comment(models.Model):
    user_name = models.ForeignKey('User', to_field='id', on_delete=models.CASCADE)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.user_name} - {self.text[:50]}'

    def html_validation(self):
        html_tags = re.findall(r"</?(.*?)>", str(self.text))
        for tag in html_tags:
            if tag not in ALLOWED_TAGS:
                raise ValidationError("HTML tag '%s' is not allowed" % tag)

        opening_tags = re.findall(r"<\s*([a-zA-Z]+)(?=[^>]*?>)", str(self.text))
        closing_tags = re.findall(r"<\s*/\s*([a-zA-Z]+)\s*>", str(self.text))
        if len(opening_tags) != len(closing_tags):
            raise ValidationError("HTML tags are not properly closed")


class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    home_page = models.URLField(blank=True)

    def __str__(self):
        return self.user_name
