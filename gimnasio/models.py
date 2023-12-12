from django.db import models

class Fighter(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    weight_class = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='fighter_images/')  # Requires Pillow installed for image handling
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    description = models.TextField()
    fighters = models.ManyToManyField(Fighter, related_name='events')  # Many-to-many relationship with fighters
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    occupation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.occupation
