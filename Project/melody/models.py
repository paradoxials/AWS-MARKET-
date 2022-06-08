from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    birthday = models.DateField()
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 15)
    contact = models.CharField(max_length = 11)
    profilepicture = models.ImageField(upload_to='images', default = 'images/avatar.png', blank = True)
    class Meta:
        db_table = "Customer"

class Song(models.Model):
    songtitle = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    dateRelease = models.DateField()
    producer = models.CharField(max_length = 100)
    songwriter = models.CharField(max_length = 100)
    # songImage = models.ImageField(upload_to='images', default='images/avatar.png', blank=True)

    class Meta:
        db_table = "Song"

class Playlist(models.Model):
    customer = models.ForeignKey(Customer, null = False, blank = False, on_delete = models.CASCADE, related_name = "Customer")
    song = models.ForeignKey(Song, null = False, blank = False, on_delete = models.CASCADE, related_name = "Song")
    # name = models.CharField(max_length = 100)

    class Meta:
        db_table = "Playlist"