from django.db import models
from user_application.models import user_registration


# Create your models here.
class applications(models.Model) :  
   id = models.IntegerField(primary_key=True, unique=True, default=1)
   code = models.CharField(max_length=50, unique=True)
   name = models.CharField(max_length=50)
   is_active = models.BooleanField(default=True)
    

class application_access(models.Model) :
   id = models.IntegerField(primary_key=True, unique=True, default=1)
   application_id = models.ForeignKey(applications, on_delete=models.CASCADE, related_name="user_application_id")
   user_id = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="user_id")
   is_active = models.BooleanField(default=True)
   valid_from = models.DateTimeField(auto_now=False, auto_now_add=False)
   valid_to = models.DateTimeField(auto_now=False, auto_now_add=False)
   access_type = models.CharField(max_length=50)
   access_type_value = models.CharField(max_length=50)
   created_at = models.DateTimeField(auto_now_add=True)
   last_accessed = models.DateTimeField(auto_now_add=True, null=True, blank=True)            
 

class application_role(models.Model) :
    id = models.IntegerField(primary_key=True, unique=True, default=1)
    application_id = models.ForeignKey(applications, on_delete=models.CASCADE, related_name="application")
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)


class application_feature_category(models.Model) :
  id = models.IntegerField(primary_key=True, unique=True, default=1)
  application_id = models.ForeignKey(applications, on_delete=models.CASCADE,related_name="application_id")
  code = models.CharField(max_length=50)
  description = models.CharField(max_length=400)
  is_active = models.BooleanField(default=True)


class application_feature(models.Model) :
  id = models.IntegerField(primary_key=True, unique=True, default=1)
  feature_category_id = models.ForeignKey(application_feature_category, on_delete=models.CASCADE, related_name="feature_category_id")
  code = models.CharField(max_length=200)
  description = models.CharField(max_length=400)
  is_active = models.BooleanField(default=True)


class application_role_feature(models.Model) : 
   id = models.IntegerField(primary_key=True, unique=True, default=1)
   application_role_id = models.ForeignKey(application_role, on_delete=models.CASCADE, related_name="application_role_id")
   application_feature_id = models.ForeignKey(application_feature, on_delete=models.CASCADE, related_name="application_feature_id")
   code = models.CharField(max_length=200)
   description = models.CharField(max_length=400)
   is_active = models.BooleanField(default=True)


