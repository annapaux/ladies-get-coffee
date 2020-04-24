from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from messenger.forms import MessageForm
from messenger.models import Thread, UserThread, Message


class MessageFormTest(TestCase):

    def test_message_form_correct_input(self):
        form = MessageForm(data={
            'text':'This is a test message.'})
        self.assertTrue(form.is_valid())


class ThreadModelTest(TestCase):

    @classmethod
    def setUp(self):
        self.user1_credentials = {
            'username': 'temporary1',
            'password': 'temporary123'}
        self.user2_credentials = {
            'username': 'temporary2',
            'password': 'temporary123'}

        self.user1 = User.objects.create_user(**self.user1_credentials)
        self.user1.save()
        self.user2 = User.objects.create_user(**self.user2_credentials)
        self.user2.save()

        Thread.objects.create(user1=self.user1, user2=self.user2)

    def test_thread_string_name(self):
        thread = Thread.objects.get(id=1)
        expected_object_name = f'Thread between {self.user1}, {self.user2}'
        self.assertEquals(expected_object_name, str(thread))


class MessageModelTest(TestCase):

    @classmethod
    def setUp(self):
        self.user1_credentials = {
            'username': 'temporary1',
            'password': 'temporary123'}
        self.user2_credentials = {
            'username': 'temporary2',
            'password': 'temporary123'}

        self.user1 = User.objects.create_user(**self.user1_credentials)
        self.user1.save()
        self.user2 = User.objects.create_user(**self.user2_credentials)
        self.user2.save()

        self.thread = Thread.objects.create(user1=self.user1, user2=self.user2)
        self.thread.save()
        self.user_thread = UserThread.objects.create(user=self.user1, thread=self.thread)
        self.user_thread.save()

    def test_user_thread_string_name(self):
        userthread = UserThread.objects.get(id=1)
        expected_object_name = f'Link of user {self.user1} to thread {self.thread}'
        self.assertEquals(expected_object_name, str(userthread))


class ThreadModelTest(TestCase):

    @classmethod
    def setUp(self):
        self.user1_credentials = {
            'username': 'temporary1',
            'password': 'temporary123'}
        self.user2_credentials = {
            'username': 'temporary2',
            'password': 'temporary123'}

        self.user1 = User.objects.create_user(**self.user1_credentials)
        self.user1.save()
        self.user2 = User.objects.create_user(**self.user2_credentials)
        self.user2.save()

        self.thread = Thread.objects.create(user1=self.user1, user2=self.user2)
        self.thread.save()
        self.user_thread = UserThread.objects.create(user=self.user1, thread=self.thread)
        self.user_thread.save()

        self.text = 'text'

        Message.objects.create(
            text=self.text,
            thread=self.thread,
            from_user=self.user1,
            to_user=self.user2
        )

    def test_message_string_name(self):
        message = Message.objects.get(id=1)
        expected_object_name = f'From {self.user1} to {self.user2}: {self.text}'
        self.assertEquals(expected_object_name, str(message))
