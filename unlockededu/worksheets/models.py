from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=256)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MCAnswer(models.Model):
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        "MultipleChoiceQuestion", on_delete=models.CASCADE
    )


class Question(models.Model):
    difficulty_levels = [
        ("beginner", "Beginner"),
        ("easy", "Easy"),
        ("normal", "Normal"),
        ("hard", "Hard"),
        ("mastery", "Mastery"),
    ]
    text = models.TextField()
    subject = models.ForeignKey("Subject", on_delete=models.PROTECT)
    tags = models.ManyToManyField("Tag")
    rating = models.CharField(max_length=8, choices=difficulty_levels,
        default="beginner")

    class Meta:
        abstract = True


class FreeResponseQuestion(Question):
    answer = models.TextField()


class MultipleChoiceQuestion(Question):
    question_numbering = [
        ("upper-alpha", "Upper Case Alpha (A, B, C)"),
        ("lower-alpha", "Lower Case Alpha (a, b, c"),
        ("upper-roman", "Upper Case Roman Numerals (I, II, III)"),
        ("lower-roman", "Lower Case Roman Numerals (i, ii, iii)"),
    ]
    numbering = models.CharField(
        max_length=16, choices=question_numbering, default="lower-alpha"
    )
