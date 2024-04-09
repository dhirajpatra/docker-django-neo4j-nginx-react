from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse


class CharCountViewTestCase(TestCase):
    def test_char_count(self):
        # Define a test text
        test_text = "Hello, world!"

        # Build the URL for the char_count view
        url = reverse("char_count")

        # Make a GET request to the view with the test text
        response = self.client.get(url, {"text": test_text})

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Decode the response content to JSON
        content = response.content.decode("utf-8")

        # Parse the JSON response
        data = JsonResponse(content, safe=False)

        # Check that the response contains the correct character count
        self.assertEqual(data["count"], len(test_text))

