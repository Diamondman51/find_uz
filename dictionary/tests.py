from django.test import TestCase
from rest_framework.test import APIClient

from api.models import User
from dictionary.models import Category, DiplomaticTerm


class CategoryViewSerializerTests(TestCase):
    """Pin the fix: CategoryView must serialise Category objects via
    CategorySerializer (not DiplomaticTermSerializer)."""

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Diplomacy')

    def test_category_list_returns_category_fields(self):
        client = APIClient()
        resp = client.get('/dictionary/category/')
        self.assertEqual(resp.status_code, 200)
        body = resp.json()
        results = body.get('results', body)
        self.assertGreaterEqual(len(results), 1)
        self.assertIn('name', results[0])
        self.assertIn('id', results[0])
        self.assertNotIn('definition', results[0])


class CreateDiplomaticTermPermissionTests(TestCase):
    """Pin the fix: destroy/update on CreateDiplomaticTermView requires
    superuser or dict_admin — was IsAuthenticated."""

    @classmethod
    def setUpTestData(cls):
        cls.regular = User.objects.create_user(
            username='reg', phone_number='+998904444444', password='pw-12345',
            user_type='dict_user',
        )
        cls.regular.dict_user.dict_admin = False
        cls.regular.dict_user.save()

        cls.admin = User.objects.create_user(
            username='adm', phone_number='+998905555555', password='pw-12345',
            user_type='dict_user',
        )
        cls.admin.dict_user.dict_admin = True
        cls.admin.dict_user.save()

        cls.term = DiplomaticTerm.objects.create(title='Term', definition='d')

    def setUp(self):
        self.client = APIClient()

    def test_regular_user_cannot_delete_term(self):
        self.client.force_authenticate(self.regular)
        resp = self.client.delete(f'/dictionary/create_term/{self.term.id}/')
        self.assertEqual(resp.status_code, 403)
        self.assertTrue(DiplomaticTerm.objects.filter(id=self.term.id).exists())

    def test_dict_admin_can_delete_term(self):
        self.client.force_authenticate(self.admin)
        resp = self.client.delete(f'/dictionary/create_term/{self.term.id}/')
        self.assertIn(resp.status_code, (200, 204))
        self.assertFalse(DiplomaticTerm.objects.filter(id=self.term.id).exists())

    def test_anonymous_cannot_delete_term(self):
        resp = self.client.delete(f'/dictionary/create_term/{self.term.id}/')
        self.assertIn(resp.status_code, (401, 403))


class CreateCategoryPermissionTests(TestCase):
    """CreateCategoryView must require dict_admin/superuser."""

    @classmethod
    def setUpTestData(cls):
        cls.regular = User.objects.create_user(
            username='cat-reg', phone_number='+998906666666', password='pw-12345',
            user_type='dict_user',
        )
        cls.regular.dict_user.dict_admin = False
        cls.regular.dict_user.save()

    def test_regular_user_cannot_create_category(self):
        client = APIClient()
        client.force_authenticate(self.regular)
        resp = client.post('/dictionary/create_category/', {'name': 'NewCat'}, format='json')
        self.assertEqual(resp.status_code, 403)
