# coding=utf-8
"""Dinosaurs app constants."""
from typing import Tuple

CARNIVORES: str = 'carnivores'
HERBIVORES: str = 'herbivores'
OMNIVORES: str = 'omnivores'

EATING_CLASSIFICATION_CHOICES: Tuple[Tuple[str, str], ...] = (
    (CARNIVORES, 'Carnivores'),
    (HERBIVORES, 'Herbivores'),
    (OMNIVORES, 'Omnivores')
)

TRIASSIC: str = 'triassic'
JURASSIC: str = 'jurassic'
CRETACEOUS: str = 'cretaceous'
PALEOGENE: str = 'paleogene'
NEOGENE: str = 'neogene'

PERIOD_LIVED_CHOICES: Tuple[Tuple[str, str], ...] = (
    (TRIASSIC, 'Triassic'),
    (JURASSIC, 'Jurassic'),
    (CRETACEOUS, 'Cretaceous'),
    (PALEOGENE, 'Paleogene'),
    (NEOGENE, 'Neogene')
)

TINY: str = 'tiny'
VERY_SMALL: str = 'very_small'
SMALL: str = 'small'
MEDIUM: str = 'medium'
LARGE: str = 'large'
VERY_LARGE: str = 'very_large'

AVERAGE_SIZE_CHOICES: Tuple[Tuple[str, str], ...] = (
    (TINY, 'Tiny: Less than 1 meter in length'),
    (VERY_SMALL, 'Very Small: 1-2 meters in length'),
    (SMALL, 'Small: 2-4 meters in length'),
    (MEDIUM, 'Medium: 4-8 meters in length'),
    (LARGE, 'Large: 8-15 meters in length'),
    (VERY_LARGE, 'Very Large: More than 15 meters in length')
)

MAX_IMAGE_SIZE: int = 20 * 1024 * 1024  # 20 MB
