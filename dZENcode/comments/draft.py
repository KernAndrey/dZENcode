from random import randint

from comments.models import Comment, User

from faker import Faker

def generate_random_text():
    fake = Faker()
    return fake.text()

def generate_random_user():
    fake = Faker()
    return {
        'name': fake.name(),
        'email': fake.email(),
        'url': fake.url()
    }



for i in range(10):
    user_data = generate_random_user()
    user, created = User.objects.get_or_create(
        user_name=user_data['name'],
        email=user_data['email'],
        home_page=user_data['url']
    )
    for i in range(2000):
        try:
            parent_comment = Comment.objects.get(id=randint(0, 300))
        except:
            pass
        Comment.objects.create(
            user_name=user,
            text=generate_random_text(),
            parent_comment=parent_comment
        )
