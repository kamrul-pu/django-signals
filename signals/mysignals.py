from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from signals.models import Profile
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