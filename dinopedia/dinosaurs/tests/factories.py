# coding=utf-8
"""Dinosaur app factories for tests."""
import factory
from factory import fuzzy

from accounts.tests.factories import UserFactory
from dinosaurs import signals
from dinosaurs.const import AVERAGE_SIZE_CHOICES, EATING_CLASSIFICATION_CHOICES, PERIOD_LIVED_CHOICES
from dinosaurs.models import Dinosaur, Photo, UserFavoriteDinosaurs


class DinosaurFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Type %03d' % n)
    eating_classification = fuzzy.FuzzyChoice([i[0] for i in EATING_CLASSIFICATION_CHOICES])
    period_lived = fuzzy.FuzzyChoice([i[0] for i in PERIOD_LIVED_CHOICES])
    average_size = fuzzy.FuzzyChoice([i[0] for i in AVERAGE_SIZE_CHOICES])

    class Meta:
        model = Dinosaur

    @factory.post_generation
    def photos(self, create, extracted, **kwargs):
        """Dinosaur photos."""
        if not create:
            return

        if extracted:
            for photo in extracted:
                self.photos.add(photo)


class PhotoFactory(factory.django.DjangoModelFactory):
    image = factory.django.ImageField()
    dinosaur = factory.SubFactory(DinosaurFactory)

    class Meta:
        model = Photo
