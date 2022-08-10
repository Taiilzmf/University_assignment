from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # creates model manager
    object = models.Manager()


    def __str__(self):
        # returns input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.campus_name}: {0.state}'
        return display_course.format(self)

    # removes added 's' that django adds to model name in browser display
    class Meta:
        verbose_name_plural = "University Campus"
