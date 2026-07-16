from django.conf import settings
from django.test import TestCase

from .models import Profile


class ModelConfigurationTests(TestCase):
    def test_profile_picture_uses_cloudinary_storage(self):
        field = Profile._meta.get_field("profile_picture")
        self.assertEqual(field.__class__.__name__, "CloudinaryField")

    def test_database_settings_are_configured(self):
        self.assertIn("ENGINE", settings.DATABASES["default"])
        self.assertTrue(settings.DATABASES["default"]["ENGINE"])
