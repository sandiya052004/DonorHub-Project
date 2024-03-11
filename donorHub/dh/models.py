from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donation_type = models.CharField(max_length=100)  
    availability = models.CharField(max_length=100)
    preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Organization(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    organization_type = models.CharField(max_length=100) 
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DonationRequest(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    donation_type_requested = models.CharField(max_length=100)
    additional_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.organization.name} - {self.donation_type_requested}"

class Contact(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='received_messages')
    message_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender.username} - To: {self.receiver.name}"

