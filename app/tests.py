from django.test import TestCase
from app.forms import EditProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'temporary',
            'password': 'temporary123'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)


class ProfileFormTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username='temporary', password='temporary123')

    def test_profile_form_correct_input(self):
        User = get_user_model()
        self.client.login(username='temporary', password='temporary')
        user = User.objects.get(username='temporary')

        form = EditProfile(data={
            'user':user.id,
            'first_name':'temp',
            'last_name':'temp',
            'email':'temp@temp.com',
            'current_job':'temp'})
        self.assertTrue(form.is_valid())

    def test_profile_form_email_help_text(self):
        form = EditProfile()
        self.assertEqual(form.fields['email'].help_text, "Provide an email peers can reach you at.")

    def test_profile_form_current_job_help_text(self):
        form = EditProfile()
        self.assertEqual(form.fields['current_job'].help_text, "Current job or status (e.g. software engineer, student, entrepreneur)")
