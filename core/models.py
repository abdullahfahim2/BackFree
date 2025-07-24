from django.db import models
from django.core.validators import FileExtensionValidator

class Example(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    before_image = models.ImageField(upload_to='examples/before/')
    after_image = models.ImageField(upload_to='examples/after/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class ProcessedImage(models.Model):
    original_image = models.ImageField(upload_to='uploads/original/')
    processed_image = models.ImageField(upload_to='uploads/processed/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=40, blank=True,null=True)
    
    def __str__(self):
        return f"Processed image {self.id}"
