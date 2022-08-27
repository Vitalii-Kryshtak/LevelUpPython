from random import choices, randint
from django.core.management import BaseCommand

from articles.models import (
    Article,
    Tag,
    Author,
    Rubric,
)
from articles.management.commands._common import (
    rubrics_with_tags,
    get_names,
    get_emails,
    get_jobs, get_title,
    get_content,
)
from faker import Faker


faker = Faker()




class Command(BaseCommand):
    help = "This command fill DB with mocked data"

    def add_arguments(self, parser):
        parser.add_argument(
            "-a",
            "--authors",
            type=int,
            help="Authors to be created",
        )
        parser.add_argument(
            "-A",
            "--articles-per-author",
            type=int,
            help="Articles to be created for each author",
        )

    def handle(self, *args, **options):
        authors_amount = options.get("authors")
        articles_per_author = options.get("articles_per_author")

        self.stdout.write("Fill DB start")
        self.clear_tables()
        self.create_rubrics_tags()
        self.create_authors(amount=authors_amount)
        self.create_articles(articles_per_author=articles_per_author)
        self.stdout.write("Fill DB done")

    def clear_tables(self):
        self.stdout.write("Clear Tables from data")
        for model in (Article, Tag, Author, Rubric):
            model.objects.all().delete()

    def create_rubrics_tags(self):
        self.stdout.write("Create Rubrics and Tags")
        for rubric, tags in rubrics_with_tags.items():
            rubric = Rubric.objects.create(subject=rubric)
            tags_objects = [Tag(title=tag, rubric=rubric) for tag in tags]
            Tag.objects.bulk_create(tags_objects)


    def create_authors(self, amount):
        self.stdout.write("Create Authors")
        data = zip(get_names(amount), get_jobs(amount), get_emails(amount))
        authors_obj = [Author(name=n, occupation=j, email=e) for n, j, e in data]
        authors_models = Author.objects.bulk_create(authors_obj)

        rubrics = Rubric.objects.all()
        for author in authors_models:
            author.rubrics.set(choices(rubrics, k=randint(1, 2)))

    @staticmethod
    def create_article(author):
        author_rubric = author.rubrics.order_by("?").first()
        tags = choices(author_rubric.tags.all(), k=3)
        article = Article.objects.create(
            title=get_title(),
            content=get_content(),
            author=author,
            rubric=author_rubric,
        )
        article.tags.set(tags)


    def create_articles(self, articles_per_author=3):
        self.stdout.write("Create Articles")
        authors = Author.objects.all()
        [self.create_article(a) for _ in range(articles_per_author) for a in authors]



    # def create_author(self):
    #     numbers = 10
    #     author_object = [Author(name=faker.name(), email=faker.email(), occupation=faker.job()) for _ in range(numbers)]
    #     Author.objects.bulk_create(author_object)
    #
    # def create_article(self):
    #     articles = 3
    #     authors = Author.objects.all()
    #     rubric = Rubric.objects.get(subject="Computer science")
    #
    #     article_object = [Article(title=faker.word(), content=faker.text(), rubric=rubric, author=author) for author in authors for _ in range(articles)]
    #     Article.objects.bulk_create(article_object)




