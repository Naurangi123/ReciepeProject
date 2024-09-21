from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTest(TestCase):
    

    def setUp(self):
        # Create an admin user
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        
        # Create a regular user
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User',
        )
    def test_users_list(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        
        # Ensure the user is in the list
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        
        # Check if the edit user page loads successfully
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        
        # Check if the create user page loads successfully
        self.assertEqual(res.status_code, 200)
