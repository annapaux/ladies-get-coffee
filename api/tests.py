from django.test import TestCase

from api.models import University, Company

class UniversityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
         University.objects.create(name='Test University')

    def test_name_label(self):
        university = University.objects.get(id=1)
        field_label = university._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        university = University.objects.get(id=1)
        max_length = university._meta.get_field('name').max_length
        self.assertEquals(max_length, 250)

    def test_object_name_is_last_name_comma_first_name(self):
        university = University.objects.get(id=1)
        expected_object_name = f'{university.name}'
        self.assertEquals(expected_object_name, str(university))

    def test_get_absolute_url(self):
        university = University.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(university.get_absolute_url(), '/api/university/1/')



class CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
         Company.objects.create(name='Test Company')

    def test_name_label(self):
        company = Company.objects.get(id=1)
        field_label = Company._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        company = Company.objects.get(id=1)
        max_length = Company._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_comma_first_name(self):
        company = Company.objects.get(id=1)
        expected_object_name = f'{company.name}'
        self.assertEquals(expected_object_name, str(company))

    def test_get_absolute_url(self):
        company = Company.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(company.get_absolute_url(), '/api/company/1/')






# from django.test import TestCase
#
# # API tests
# from django.urls import reverse  # gets actual url for url name
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.views import status
# from .models import Company
# from .serializers import CompanySerializer
#
#
# class BaseViewTest(APITestCase):
#     client = APIClient()
#
#     @staticmethod
#     def create_company(name=""):
#         if name != "":
#             Company.objects.create(name=name)
#
#     def setUp(self):
#         # add test data
#         self.create_company("Google")
#         self.create_company("Facebook")
#         self.create_company("Minerva")
#         self.create_company("Amazon")
#
#
# class GetAllCompaniesTest(BaseViewTest):
#
#     def test_get_all_companies(self):
#         """
#         This test ensures that all companies added in the setUp method
#         exist when we make a GET request to the companies/ endpoint
#         """
#         # hit the API endpoint
#         response = self.client.get(
#             reverse("company-all", kwargs={"version": "v1"})
#         )
#         # fetch the data from db
#         expected = Company.objects.all()
#         serialized = CompanySerializer(expected, many=True)
#         self.assertEqual(response.data, serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
