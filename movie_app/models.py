from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=True)
    director = models.ManyToManyField(Director)


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)


@property
def directors_list(self) -> list:
    return self.directors.all()


@property
def reviews_list(self) -> list:
    return self.reviews.all()
