from rest_framework.test import APITestCase
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(APITestCase):

    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(title='Dish 1', price=10.99, inventory=20)
        Menu.objects.create(title='Dish 2', price=15.99, inventory=15)
        Menu.objects.create(title='Dish 3', price=8.99, inventory=30)

    def test_getall(self):
        # Retrieve all Menu objects using the API
        response = self.client.get('/api/menu/')  # Adjust the URL based on your project setup

        # Serialize the test instances for comparison
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Compare the serialized data with the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
