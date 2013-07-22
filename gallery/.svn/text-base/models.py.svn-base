from django.db import models

## Girl Model
class Girl(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    url = models.TextField(db_column='url')
    votes = models.IntegerField(db_column='votes')
    
## Image Model
class Image(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    path = models.TextField(db_column='path')
    owner = models.IntegerField(db_column='owner')