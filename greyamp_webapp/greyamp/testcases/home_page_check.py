from selenium import webdriver
from django.test import TestCase
from greyamp.models import GreyampData

# y = GreyampData.objects.create(name="Test")
# y.save()


class HomePageTest_port_80(TestCase):
    def test_home_page(self):
        print("Test to check application on port 80")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('http://127.0.0.1/grey/')
        el = driver.find_element_by_tag_name('h1')
        self.assertIn(el.text, 'welcome')



class HomePageTest_port_8080(TestCase):
    def test_home_page(self):
        print("Test to check application on port 8080")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('http://127.0.0.1:8080/grey/')
        el = driver.find_element_by_tag_name('h1')
        self.assertIn(el.text, 'welcome')



class EntryModelTest(TestCase):
    def test_string_representation(self):
        print("Test to check application DB")
        entry = GreyampData(name="greyamp")
        entry.save()
        self.assertEqual(str(entry.name), entry.name)




