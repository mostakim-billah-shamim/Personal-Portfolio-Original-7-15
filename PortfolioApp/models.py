from django.db import models



class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class TestimonialModel(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    review_text = models.TextField()
    image = models.ImageField(upload_to='media/testimonials' , null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.designation}"







# Create your models here.
