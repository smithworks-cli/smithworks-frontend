from django.db import models

# Create your models here.


class User(models.Model):
    """Model definition for User."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for User."""

        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """Unicode representation of User."""
        pass


class Ip(models.Model):
    """Model definition for Ip."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Ip."""

        verbose_name = "Ip"
        verbose_name_plural = "Ips"

    def __str__(self):
        """Unicode representation of Ip."""
        pass


class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Unicode representation of Profile."""
        pass


class SubscriptionTier(models.Model):
    """Model definition for SubscriptionTier."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for SubscriptionTier."""

        verbose_name = "SubscriptionTier"
        verbose_name_plural = "SubscriptionTiers"

    def __str__(self):
        """Unicode representation of SubscriptionTier."""
        pass


class Game(models.Model):
    """Model definition for Game."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Game."""

        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        """Unicode representation of Game."""
        pass


class Url(models.Model):
    """Model definition for Url."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Url."""

        verbose_name = "Url"
        verbose_name_plural = "Urls"

    def __str__(self):
        """Unicode representation of Url."""
        pass


class Configuration(models.Model):
    """Model definition for Configuration."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Configuration."""

        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        """Unicode representation of Configuration."""
        pass


class Schedule(models.Model):
    """Model definition for Schedule."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Schedule."""

        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        """Unicode representation of Schedule."""
        pass


class Invitee(models.Model):
    """Model definition for Invitee."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Invitee."""

        verbose_name = "Invitee"
        verbose_name_plural = "Invitees"

    def __str__(self):
        """Unicode representation of Invitee."""
        pass


class Character(models.Model):
    """Model definition for Character."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Character."""

        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        """Unicode representation of Character."""
        pass


class Notification(models.Model):
    """Model definition for Notification."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Notification."""

        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        """Unicode representation of Notification."""
        pass


class DigitalOcean(models.Model):
    """Model definition for DigitalOcean."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for DigitalOcean."""

        verbose_name = "DigitalOcean"
        verbose_name_plural = "DigitalOceans"

    def __str__(self):
        """Unicode representation of DigitalOcean."""
        pass
