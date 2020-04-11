from .adjectives import ADJECTIVES, POSITIVE_ADJECTIVES
from .animals import ANIMALS
from .colors import COLORS
from .monsters import MONSTERS
from .classes import CLASSES
import random


def random_game():
    return u"{}-{}-{}".format(
        random.choice(ADJECTIVES), random.choice(ADJECTIVES), random.choice(ANIMALS)
    )


def random_url():
    return u"{}-{}-{}.datageek.io".format(
        random.choices(COLORS),
        random.choice(POSITIVE_ADJECTIVES),
        random.choice(MONSTERS),
    )


def random_character():
    return u"Level {} {}".format(random.randint(1, 20), random.choice(CLASSES))
