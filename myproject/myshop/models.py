from django.db import models

# Create your models here.
class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'actor'
        app_label = 'default'
        managed = False

# Set the database name for this model
    @classmethod
    def get_all(cls):
        return cls.objects.using('default').all()