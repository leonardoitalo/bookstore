from factory import Faker, Iterator, LazyAttribute
from product.models import Product, Category
import factory

class CategoryFactory(factory.django.DjangoModelFactory):
    title = Faker("pystr")
    slug = Faker("pystr")
    description = Faker("pystr")
    active = Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = Faker("pyint")
    category = LazyAttribute(CategoryFactory)
    title = Faker("pystr")

    @factory.postGeneration
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for category in extracted:
                self.category.add(category)
                