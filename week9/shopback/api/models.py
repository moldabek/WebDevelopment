from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    count = models.IntegerField()
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description':self.description,
            'count': self.count,
            'category': self.category.to_json(),
        }

