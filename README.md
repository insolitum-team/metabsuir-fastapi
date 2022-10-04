<h1 align="center">MetaBSUIR FastAPI</h1>
<h2 align="center">Backend logic implementation for https://metabsuir.by with FastAPI</h2>


<h3 align="center">▶️ Running the server:</h3>
To run the server use the command:<br>


> uvicorn app.main:app --reload

or simply

> make runserver


<br>

<h3 align="center">↔️ Alembic migrations:</h3>
After creating new models you need to import them into alembic/env.py <br><br><hr>
Then:

- <b>make migrations</b>:
> alembic revision --autogenerate -n "First"<br>

*("First" - migration title)*

or simply

> make migrations
<hr>


- <b>migrate</b>:
> alembic upgrade head

or simply

> make migrate
