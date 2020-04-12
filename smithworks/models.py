from django.db import models
from account.models import Account
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

    # Ip fields
    ip_address = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=50)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

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

    # SubscriptionTier fields
    tier_level = models.IntegerField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for SubscriptionTier."""

        verbose_name = "SubscriptionTier"
        verbose_name_plural = "SubscriptionTiers"

    def __str__(self):
        """Unicode representation of SubscriptionTier."""
        pass


class Url(Forge):
    """Model definition for Url."""

    # Url fields
    url = models.URLField(max_length=200)

    class Meta:
        """Meta definition for Url."""

        verbose_name = "Url"
        verbose_name_plural = "Urls"

    def __str__(self):
        """Unicode representation of Url."""
        pass


class Game(Forge):
    """Model definition for Game."""

    # Game fields
    game_name = models.CharField(max_length=50)
    number_of_deployments = models.PositiveIntegerField
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.OneToOneField(Url, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Game."""

        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        """Unicode representation of Game."""
        pass


class Configuration(Forge):
    """Model definition for Configuration."""

    # Choices for platform field
    DIGITAL_OCEAN = "DO"
    AMAZON_WEB_SERVICES = "AWS"
    GOOGLE_CLOUD_PLATFORM = "GPC"
    PLATFORM_CHOICES = [
        (DIGITAL_OCEAN, "Digital Ocean"),
        (AMAZON_WEB_SERVICES, "Amazon Web Services"),
        (GOOGLE_CLOUD_PLATFORM, "Google Cloud Platform"),
    ]
    # Configuration fields
    platform = models.CharField(
        max_length=3, choices=PLATFORM_CHOICES, default=DIGITAL_OCEAN
    )
    # TODO do we actually need a reference to the user
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Configuration."""

        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        """Unicode representation of Configuration."""
        pass


class Schedule(Forge):
    """Model definition for Schedule."""

    # Schedule fields
    game_date = models.DateField(auto_now=False, auto_now_add=False)
    game_time = models.TimeField(auto_now=False, auto_now_add=False)
    notify_users = models.BooleanField()
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Schedule."""

        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        """Unicode representation of Schedule."""
        pass


class Invitee(Forge):
    """Model definition for Invitee."""

    # Invitee fields
    email_address = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    timezone = models.CharField(max_length=3)
    number_of_emails = models.PositiveIntegerField()
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Invitee."""

        verbose_name = "Invitee"
        verbose_name_plural = "Invitees"

    def __str__(self):
        """Unicode representation of Invitee."""
        pass


class Character(Forge):
    """Model definition for Character."""

    # Character Fields
    character_name = models.CharField(max_length=50)
    dndbeyond_charactersheet_url = models.URLField(max_length=200)
    invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Character."""

        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def __str__(self):
        """Unicode representation of Character."""
        pass


class Notification(Forge):
    """Model definition for Notification."""

    # Notification fields
    notify_date = models.DateField(auto_now=False, auto_now_add=False)
    notify_time = models.TimeField(auto_now=False, auto_now_add=False)
    invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Notification."""

        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        """Unicode representation of Notification."""
        pass


class DigitalOcean(Forge):
    """Model definition for DigitalOcean."""

    # DigitalOcean fields
    access_key = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for DigitalOcean."""

        verbose_name = "DigitalOcean"
        verbose_name_plural = "DigitalOceans"

    def __str__(self):
        """Unicode representation of DigitalOcean."""
        pass
