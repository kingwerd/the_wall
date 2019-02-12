from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self, post_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "Your first name must be more than 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Your last must be more than 2 characters"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address"
        if len(post_data['password']) < 8:
            error['password'] = "Password must be more than 8 characters"
        if  post_data['password'] != post_data['password_confirm']:
            errors['password_confirm'] = "Passwords do not match"
        return errors
    def login_validator(self, post_data):
        errors = {}
        user = User.objects.get(email=post_data['login_email'])
        if not user:
            errors['email'] = "Invalid email address"
        if not bcrypt.checkpw(post_data['login_password'].encode(), user.password.encode()):
            errors['password'] = "Password do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()