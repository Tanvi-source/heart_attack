from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    trtbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.BooleanField()
    rest_ecg = models.IntegerField()
    thalachh = models.IntegerField()
    exng = models.BooleanField()
    ca = models.IntegerField()
    thall = models.IntegerField()
    predicted_risk = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.user.username} on {self.created_at}"
