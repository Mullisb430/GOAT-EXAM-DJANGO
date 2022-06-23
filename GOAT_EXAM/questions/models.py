from django.db import models

class Questions(models.Model):
    question = models.TextField(max_length=250)
    answer_one = models.TextField(max_length=250)
    answer_two = models.TextField(max_length=250)
    answer_three = models.TextField(max_length=250)
    answer_four = models.TextField(max_length=250)

    def __str__(self):
        return self.question[0:10] + "...."
