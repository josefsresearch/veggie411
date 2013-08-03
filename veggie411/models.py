from django.db import models
from django.conf import settings
from django.forms import ModelForm

# Create your models here.
# Email is just for the landing page atm
class Email(models.Model):
    email = models.EmailField(unique=True)
    def __unicode__(self):
	return self.email

class EmailForm(ModelForm):
    class Meta:
	model = Email
