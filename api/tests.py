from django.test import TestCase

from api.models import DictUser, User
from api.serializers import UserSerializer


class UserSerializerTests(TestCase):
    def test_create_hashes_password(self):
        ser = UserSerializer(data={
            'username': 'alice',
            'phone_number': '+998901234567',
            'password': 'secret-pw-123',
        })
        ser.is_valid(raise_exception=True)
        user = ser.save(user_type='dict_user')
        self.assertNotEqual(user.password, 'secret-pw-123')
        self.assertTrue(user.check_password('secret-pw-123'))

    def test_update_hashes_password_when_provided(self):
        user = User.objects.create_user(
            username='bob', phone_number='+998901234568', password='old-pw-123'
        )
        ser = UserSerializer(instance=user, data={
            'username': 'bob',
            'phone_number': '+998901234568',
            'password': 'new-pw-456',
        })
        ser.is_valid(raise_exception=True)
        ser.save()
        user.refresh_from_db()
        self.assertTrue(user.check_password('new-pw-456'))

    def test_invalid_phone_number_rejected(self):
        ser = UserSerializer(data={
            'username': 'eve',
            'phone_number': '1234',
            'password': 'secret-pw-123',
        })
        self.assertFalse(ser.is_valid())
        self.assertIn('phone_number', ser.errors)

    def test_blank_phone_rejected(self):
        ser = UserSerializer(data={
            'username': 'mallory',
            'phone_number': '',
            'password': 'secret-pw-123',
        })
        self.assertFalse(ser.is_valid())
        self.assertIn('phone_number', ser.errors)


class EnsureDictUserSignalTests(TestCase):
    """Signal must provision DictUser on create AND on promotion."""

    def test_dict_user_created_on_user_create(self):
        user = User.objects.create_user(
            username='created', phone_number='+998901111111', password='pw-12345',
            user_type='dict_user',
        )
        self.assertTrue(DictUser.objects.filter(user=user).exists())

    def test_dict_user_created_on_post_create_promotion(self):
        user = User.objects.create_user(
            username='promoteme', phone_number='+998902222222', password='pw-12345',
            user_type='find_uz_user',
        )
        self.assertFalse(DictUser.objects.filter(user=user).exists())

        user.user_type = 'dict_user'
        user.save()

        self.assertTrue(DictUser.objects.filter(user=user).exists())


class UserSaveDoesNotDoubleHashTests(TestCase):
    """Regression test for the removed User.save()/set_password override that
    double-hashed passwords on every save."""

    def test_save_does_not_corrupt_password(self):
        user = User.objects.create_user(
            username='nodouble', phone_number='+998903333333', password='pw-12345',
        )
        hash_after_create = user.password
        user.first_name = 'Updated'
        user.save()
        user.refresh_from_db()
        self.assertEqual(user.password, hash_after_create)
        self.assertTrue(user.check_password('pw-12345'))
