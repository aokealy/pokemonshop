from django.test import TestCase
from .forms import CreateUserForm, UpdateUserForm


class TestCreateUserForm(TestCase):

    def test_create_user_is_required(self):

        form = CreateUserForm({'username': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')


    def test_fields_are_explicit_in_form_metaclass(self):
        form = CreateUserForm()
        self.assertEqual(form.Meta.fields, ['username', 'email', 'password1', 'password2'])


class TestUpdateUserForm(TestCase):

    def test_create_user_is_required(self):

        form = UpdateUserForm({'username': ''})

        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')


    def test_fields_are_explicit_in_form_metaclass(self):
        form = UpdateUserForm()
        self.assertEqual(form.Meta.fields, ['username', 'email'])



      