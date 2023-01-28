from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name}"


"""
creating signals if a user instance is created 
then automatically profile object will be created
"""

"""
#using decorator
@receiver(post_save,sender=User)
def createProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile Created")

#paramas (receiver ,sender)
#Method 1
# post_save.connect(createProfile,sender=User)
# Way 2 using decorator


@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
    if created==False:
        instance.profile.save()
        print("Profile updated")
        # try:
        #     instance.profile.save()
        #     print("Profile updated")
        # except:
        #     Profile.objects.create(user=instance)
        #     print("Profile created for existing user")
    
# post_save.connect(update_profile,sender=User)

"""