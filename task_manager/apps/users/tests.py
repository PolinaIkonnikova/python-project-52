from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from task_manager.utils.text import MessageForUser
# import pytest

messages = MessageForUser()

# @pytest.mark.parametrize('url', [reverse('tasks_list'),
#                                  reverse('create_tsk'),
#                                  reverse('delete_tsk', args=[6]),
#                                  reverse('update_tsk', args=[6]),
#                                  reverse('show_task', args=[9])])
# class UsersWithoutAuthentication(TestCase):
#     def test_no_auth(self, url):
#         response = self.client.get(url)
#         self.assertRedirects(response, reverse('login'))


class UserTestCase(TestCase):

    fixtures = ['statuses.json', 'users.json',
                'tasks.json', 'labels.json']

    def setUp(self):

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.users_list = reverse('users_list')
        self.login = reverse('login')
        self.form_data = {'username': 'NewName',
                          'last_name': 'L',
                          'first_name': 'F',
                          'password1': 'NewPassword123',
                          'password2': 'NewPassword123'}

    def test_users_list(self):
        response = self.client.get(reverse('users_list'))
        self.assertEqual(response.status_code, 200)
        response_tasks = list(response.context['users_list'])
        self.assertQuerysetEqual(response_tasks,
                                 [self.user1, self.user2,
                                  self.user3])

    def test_create_user(self):
        create_user = reverse('register')
        """ GET """
        get_response = self.client.get(create_user)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(create_user,
                                         self.form_data, follow=True)
        self.assertRedirects(post_response, self.login)
        self.assertTrue(User.objects.get(id=4))
        self.assertContains(post_response, text=messages.user_create)

    def test_update_user(self):
        self.client.force_login(self.user2)
        update_user = reverse('update', args=[2])
        """ GET """
        get_response = self.client.get(update_user)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(update_user,
                                         self.form_data, follow=True)
        self.assertRedirects(post_response, self.users_list)
        updated_user = User.objects.get(pk=2)
        self.assertEqual(updated_user.username, 'NewName')
        self.assertContains(post_response, text=messages.user_update)

    def test_update_user_no_permission(self):
        self.client.force_login(self.user2)
        updated_user = reverse('update', args=[1])
        """ GET """
        get_response = self.client.get(updated_user,
                                       follow=True)
        self.assertRedirects(get_response, self.users_list)
        """ POST """
        post_response = self.client.post(updated_user,
                                         self.form_data, follow=True)
        user1 = User.objects.get(id=1)
        self.assertRedirects(post_response, self.users_list)
        self.assertFalse(user1.username == self.form_data['username'])

    def delete_user_no_permission(self):
        self.client.force_login(self.user3)
        del_user1 = reverse('delete', args=[1])
        """ GET """
        get_response = self.client.get(del_user1)
        self.assertRedirects(get_response, self.users_list)
        self.assertEqual(len(User.objects.all()), 3)
        """ POST """
        post_response = self.client.post(del_user1, follow=True)
        self.assertContains(post_response, text=messages.no_rigths_for_user)

    def delete_user_without_tasks(self):
        self.client.force_login(self.user3)
        del_user3 = reverse('delete', args=[3])
        """ GET """
        get_response = self.client.get(del_user3, follow=True)
        self.assertEqual(get_response.status_code, 200)
        """ POST """
        post_response = self.client.post(del_user3, follow=True)
        self.assertRedirects(post_response, self.users_list)
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(pk=3)
        self.assertContains(post_response, text=messages.user_delete)

    def delete_user_with_tasks(self):
        self.client.force_login(self.user2)
        del_user2 = reverse('delete', args=[2])
        """ GET """
        get_response = self.client.get(del_user2, follow=True)
        self.assertRedirects(get_response, self.users_list)
        self.assertEqual(len(User.objects.all()), 3)
        """ POST """
        post_response = self.client.post(del_user2, follow=True)
        self.assertContains(post_response, text=messages.no_delete_user)
