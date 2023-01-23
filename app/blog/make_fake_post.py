from faker import Faker
from app.blog.models import Post, Category
from django.contrib.auth.models import User

fake = Faker()

Post.objects.all().delete()




def get_full_name():
	return f'{fake.first_name()} {fake.last_name()}'

def get_password():
	return f"{fake.password(12)}"

for _ in range(10):
	user = User(username=get_full_name(), password=get_password())
	user.save()

def get_category():
	return f'{fake.job()}'

for _ in range(10):
	category = Category(name=get_category())
	category.save()

for _ in range(50):
	post = Post(user=user,
				category=category,
				title=fake.sentence(nb_words=6),
				description=fake.sentence(nb_words=10),
				content=fake.text(max_nb_chars=1000)
				)
	post.save()