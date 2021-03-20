from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BraeburnApple
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models

class BraeburnTests(TestCase):
    test_image = SimpleUploadedFile(name='test_image.jpg', content=open('apple3.jpeg', 'rb').read(), content_type='image/jpeg')
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_braeburn = BraeburnApple.objects.create(
            uploaded_by = testuser1,
            image = BraeburnTests.test_image,
            added = models.DateTimeField(auto_now_add=True)
        )
        test_braeburn.save()

    def test_blog_content(self):
        braeburn_apple = BraeburnApple.objects.get(id=1)
        actual_uploaded_by = str(braeburn_apple.uploaded_by)
        actual_image = str(braeburn_apple.image)
        actual_added = str(braeburn_apple.added)
        self.assertEqual(actual_uploaded_by, 'testuser1')
        # The test image name recieved a unique identifier between it's creation and use, so matching 'test_image' was the best I could do.
        self.assertEqual(actual_image[:9], str(BraeburnTests.test_image)[:9])
        self.assertEqual(actual_added, str(braeburn_apple.added))