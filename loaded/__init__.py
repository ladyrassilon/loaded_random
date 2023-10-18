import logging

from .abstract import AbstractLoadedRandomGenerator
from .mixins import ListItemsOnly, NumberOnly, UseSystemRandom

log = logging.getLogger(__file__)


class LoadedRandomItemChooser(ListItemsOnly, AbstractLoadedRandomGenerator):
    pass


class LoadedRandomNumberChooser(
    NumberOnly, ListItemsOnly, AbstractLoadedRandomGenerator
):
    pass


class SystemLoadedRandomItemChooser(
    UseSystemRandom, ListItemsOnly, AbstractLoadedRandomGenerator
):
    pass


class SystemLoadedRandomNumberChooser(
    UseSystemRandom, NumberOnly, ListItemsOnly, AbstractLoadedRandomGenerator
):
    pass
