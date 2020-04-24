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
