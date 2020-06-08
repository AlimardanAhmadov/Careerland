from django.db import models


class Registration(models.Model):
    from_user = models.CharField(max_length=100)
    from_surname = models.CharField(max_length=150)
    from_email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=100)
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.from_user


class Contact(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    email = models.EmailField()
    number = models.CharField(max_length=100)
    message = models.TextField()    

    def __str__(self):
        return self.name


class Career(models.Model):
    teach_name = models.CharField(max_length=150)
    teach_surname = models.CharField(max_length=150)
    teach_email = models.EmailField()
    teach_number = models.CharField(max_length=200)
    teach_files = models.FileField(upload_to='teach_files')
    teach_message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teach_name