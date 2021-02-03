import time
from locust import HttpUser, User, task, between
import random as rd
from faker import Faker

fake = Faker()


class UserScenario(HttpUser):

    @task(3)
    def get_articles(self):
        self.client.get("/api/articles/")

    @task(4)
    def get_specific_article(self):
        self.client.get(f"/api/articles/{rd.randint(1, 5)}/", name="/api/articles/{pk}/")

    @task(3)
    def get_article_full_info(self):
        self.client.get(f"/api/articles/{rd.randint(1, 5)}/get_full_info/", name="/api/articles/{pk}/get_full_info/")

    @task(3)
    def get_invalid_article(self):
        with self.client.get(f"/api/articles/0/", catch_response=True, name="/api/articles/{pk}/") as resp:
            if resp.status_code == 404:
                resp.success()

    @task(1)
    def create_article(self):
        article = {
            "title": f"Test Article {rd.randint(1000, 9999)}",
            "subject": "Testing",
            "body": "Hello World!",
            "author": 1
        }
        self.client.post("/api/articles/", json=article)

    @task(3)
    def get_authors(self):
        self.client.get("/api/authors/")

    @task(3)
    def get_specific_author(self):
        self.client.get("/api/authors/1/")

    @task(1)
    def create_author(self):
        author = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "name": f"{fake.first_name().lower()}.{fake.first_name().lower()}",
            "email": f"test.{fake.first_name().lower()}.{fake.first_name().lower()}@gmail.com"
        }
        self.client.post("/api/authors/", json=author)

    wait_time = between(0.2, 0.5)
