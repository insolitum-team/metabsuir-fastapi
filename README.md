<h3>Alembic migrations:</h3>
After creating new models you need to import them into alembic/env.py

Then

- make migrations:
> alembic revision --autogenerate -n "First"

*("First" - migration title)*

- migrate:
> alembic upgrade head