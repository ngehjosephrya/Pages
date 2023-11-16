from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_templates_name_correct(self):
        reponse = self.client.get(reverse('home'))
        self.assertTemplateUsed(reponse, 'pages/home.html')
    
    def test_templates_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1> HomePage </h1>')
        

class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_templates_name_correct(self):
        reponse = self.client.get(reverse('about'))
        self.assertTemplateUsed(reponse, 'pages/about.html')
    
    def test_templates_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1> About Us </h1>')