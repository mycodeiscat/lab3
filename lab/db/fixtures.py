"""Create fake models for tests and seeding dev DB."""
from faker import Factory as FakerFactory
import factory
from flask import current_app
from lab.model import Book, Author, Reader
from lab.db import db
from sqlalchemy.orm import scoped_session


Session = scoped_session(
    lambda: current_app.extensions["sqlalchemy"].db.session,
    scopefunc=lambda: current_app.extensions["sqlalchemy"].db.session,
)
faker: FakerFactory = FakerFactory.create()


def seed_db():
    # seed DB with factories here
    # https://pytest-factoryboy.readthedocs.io/en/latest/#model-fixture

    BookFactory.create_batch(10000)  # Create books with related entities

    db.session.commit()
    print("Database seeded.")


class SQLAFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Use a scoped session when creating factory models."""

    class Meta:
        abstract = True
        sqlalchemy_session = Session


class ReaderFactory(SQLAFactory):
    class Meta:
        model = Reader

    username = factory.LazyFunction(faker.first_name)
    password = factory.LazyFunction(faker.md5)
    role = factory.LazyFunction(faker.word)


class AuthorFactory(SQLAFactory):
    class Meta:
        model = Author

    name = factory.LazyFunction(faker.first_name)

    bio = factory.LazyFunction(faker.sentence)


class BookFactory(SQLAFactory):
    class Meta:
        model = Book

    name = factory.LazyFunction(faker.word)

    description = factory.LazyFunction(faker.sentence)

    content = factory.LazyFunction(faker.sentence)

    authors = factory.List([factory.SubFactory(AuthorFactory) for _ in range(2)])

    readers = factory.List([factory.SubFactory(ReaderFactory) for _ in range(2)])