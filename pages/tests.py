from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView

class HomepageTests(SimpleTestCase):

    def setUp(self):
        # Устанавливаем URL для домашней страницы и выполняем GET-запрос.
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        # Проверяем, что URL-адрес домашней страницы возвращает код состояния 200 (OK).
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        # Проверяем, что имя URL-адреса соответствует ожидаемому имени ("home").
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        # Проверяем, что при запросе домашней страницы используется правильный шаблон ("home.html").
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_contains_correct_html(self):
        # Проверяем, что на домашней странице есть определенный текст ("home page").
        response = self.client.get("/")
        self.assertContains(response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        # Проверяем, что на домашней странице отсутствует определенный нежелательный текст ("Hi there! I should not be on the page.").
        response = self.client.get("/")
        self.assertNotContains(response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):
        # Проверяем, что URL-адрес домашней страницы разрешается на правильное представление (`HomePageView`).
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
