from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=200)
    due_date = models.DateTimeField(blank=True)
    status = models.CharField(max_length=50)

    class Meta:
        ordering = ('due_date',)
        unique_together=('title','status')
    def __str__(self):
        return '%s %s %s' % (self.title, self.due_date, self.status)

