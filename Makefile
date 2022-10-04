MAIN_PY = uvicorn app.main:app

runserver:
	@$(MAIN_PY) --reload

migrations:
	alembic revision --autogenerate -n "no-sign"

migrate:
	alembic upgrade head