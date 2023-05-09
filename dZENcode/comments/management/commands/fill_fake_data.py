from django.core.management.base import BaseCommand
from random import randint

from faker import Faker

from comments.models import User, Comment


class Command(BaseCommand):
    help = 'Fill database with fake data'

    @staticmethod
    def generate_random_text():
        fake = Faker()
        return fake.text()

    @staticmethod
    def generate_random_user():
        fake = Faker()
        return {
            'name': fake.name(),
            'email': fake.email(),
            'url': fake.url()
        }
    def save_parent_comments(self):
        for i in range(10):
            user_data = self.generate_random_user()
            user, created = User.objects.get_or_create(
                user_name=user_data['name'],
                email=user_data['email'],
                home_page=user_data['url']
            )
            for i in range(10):
                Comment.objects.create(
                    user_name=user,
                    text=self.generate_random_text(),
                )

    def save_child_comments(self):
        for i in range(10):
            user_data = self.generate_random_user()
            user, created = User.objects.get_or_create(
                user_name=user_data['name'],
                email=user_data['email'],
                home_page=user_data['url']
            )
            for i in range(20):
                try:
                    parent_comment = Comment.objects.get(id=randint(0, 100))
                except:
                    continue
                Comment.objects.create(
                    user_name=user,
                    text=self.generate_random_text(),
                    parent_comment=parent_comment
                )

    def handle(self, *args, **options):
        try:
            self.save_parent_comments()
            self.stdout.write(
                self.style.SUCCESS('Parent comments successfully added')
            )
        except Exception as ex:
            self.stdout.write(
                self.style.FAILURE(f'Ooops, can not add parent comments. Problem: {ex}')
            )
        try:
            self.save_child_comments()
            self.stdout.write(
                self.style.SUCCESS('Child comments successfully added')
            )
        except Exception as ex:
            self.stdout.write(
                self.style.FAILURE(f'Ooops, can not add child comments. Problem: {ex}')
            )

