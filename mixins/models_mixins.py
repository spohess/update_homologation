from django.db import models


class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,
                                      null=True)

    def created_at_normalized(self, date_format='%d/%m/%Y'):
        return self.created_at.strftime(date_format)

    def updated_at_normalized(self, date_format='%d/%m/%Y'):
        return self.updated_at.strftime(date_format)

    class Meta:
        abstract = True
