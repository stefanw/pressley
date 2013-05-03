from django.db import models


class Release(models.Model):

    source = models.ForeignKey('sources.Source')
    date = models.DateField(auto_now=False, null=False)
    url = models.TextField(null=False)
    title = models.TextField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('url', 'title', 'date', 'body', 'source')
        ordering = ['-date', 'source']

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.source)
