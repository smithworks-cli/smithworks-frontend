from django.db import models

import uuid

# Create your models here.


class Forge(models.Model):
    """Model definition for Forge."""

    # TODO: Define fields here
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Forge."""

        abstract = True

    def __str__(self):
        """Unicode representation of Forge."""
        pass


class Ip(Forge):
    """Model definition for Ip."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Ip."""

        verbose_name = "Ip"
        verbose_name_plural = "Ips"

    def __str__(self):
        """Unicode representation of Ip."""
        pass


class Profile(Forge):
    """Model definition for Profile."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Unicode representation of Profile."""
        pass


class SubscriptionTier(Forge):
    """Model definition for SubscriptionTier."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for SubscriptionTier."""

        verbose_name = "SubscriptionTier"
        verbose_name_plural = "SubscriptionTiers"

    def __str__(self):
        """Unicode representation of SubscriptionTier."""
        pass


class Game(Forge):
    """Model definition for Game."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Game."""

        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        """Unicode representation of Game."""
        pass


class Url(Forge):
    """Model definition for Url."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Url."""

        verbose_name = "Url"
        verbose_name_plural = "Urls"

    def __str__(self):
        """Unicode representation of Url."""
        pass


class Configuration(Forge):
    """Model definition for Configuration."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Configuration."""

        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        """Unicode representation of Configuration."""
        pass


class Schedule(Forge):
    """Model definition for Schedule."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Schedule."""

        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        """Unicode representation of Schedule."""
        pass


class Invitee(Forge):
    """Model definition for Invitee."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Invitee."""

        verbose_name = "Invitee"
        verbose_name_plural = "Invitees"

    def __str__(self):
        """Unicode representation of Invitee."""
        pass


class Character(Forge):
    """Model definition for Character."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Character."""

        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        """Unicode representation of Character."""
        pass


class Notification(Forge):
    """Model definition for Notification."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Notification."""

        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        """Unicode representation of Notification."""
        pass


class DigitalOcean(Forge):
    """Model definition for DigitalOcean."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for DigitalOcean."""

        verbose_name = "DigitalOcean"
        verbose_name_plural = "DigitalOceans"

    def __str__(self):
        """Unicode representation of DigitalOcean."""
        pass
