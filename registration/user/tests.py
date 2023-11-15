from django.test import TestCase
from .models import User, WasteCollector, WasteRecycler

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            first_name='John',
            last_name='Doe',
            email='test@example.com',
        )

    def test_is_wastecollector_default_value(self):
        self.assertFalse(self.user.is_wastecollector)

    def test_is_wasterecycler_default_value(self):
        self.assertFalse(self.user.is_wasterecycler)

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'Leila')

class WasteCollectorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Leila',
            first_name='Leila',
            last_name='Akinyi',
            email='lee@gmail.com',
        )
        self.waste_collector = WasteCollector.objects.create(
            user=self.user,
            username='Leila',
            first_name='Akinyi',
            last_name='Doe',
            email='lee@gmail.com',
            phonenumber='+2547324567890',
            location='Githurai45',
        )

    def test_waste_collector_str_representation(self):
        self.assertEqual(str(self.waste_collector), 'John')

    def test_waste_collector_has_user(self):
        self.assertEqual(self.waste_collector.user, self.user)

class WasteRecyclerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Leila',
            first_name='Leila',
            last_name='Akinyi',
            email='lee@gmail.com',
        )
        self.waste_recycler = WasteRecycler.objects.create(
            user=self.user,
            username='Leila',
            first_name='Akinyi',
            last_name='Doe',
            email='lee@gmail.com',
            phonenumber='+2547324567890',
        )

    def test_waste_recycler_str_representation(self):
        self.assertEqual(str(self.waste_recycler), 'John')

    def test_waste_recycler_has_user(self):
        self.assertEqual(self.waste_recycler.user, self.user)

    def test_waste_recycler_has_unique_email(self):
        duplicate_recycler = WasteRecycler(
            user=User.objects.create(),
            username='Leila',
            first_name='Akinyi',
            last_name='Recycler',
            email='lee@gmail.com',
            phonenumber='+2547324567890',
        )
        with self.assertRaises(Exception):
            duplicate_recycler.save()