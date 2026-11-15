from django.test import TestCase
from django.urls import reverse

from .models import Place


class PlacePageTests(TestCase):
    def test_map_page_displays_saved_places(self):
        response = self.client.get(reverse("map_page"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ivano-Frankivsk City Hall")

    def test_valid_place_submission_is_saved(self):
        response = self.client.post(
            reverse("map_page"),
            {
                "name": "Test garden",
                "category": "Park",
                "description": "A small garden.",
                "lat": "48.9",
                "lng": "24.7",
            },
        )

        self.assertRedirects(response, reverse("map_page"))
        self.assertTrue(Place.objects.filter(name="Test garden").exists())

    def test_invalid_coordinates_do_not_save_place(self):
        response = self.client.post(
            reverse("map_page"),
            {
                "name": "Invalid place",
                "category": "Park",
                "description": "Outside the valid latitude range.",
                "lat": "91",
                "lng": "24.7",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ensure this value is less than or equal to 90.")
        self.assertFalse(Place.objects.filter(name="Invalid place").exists())
