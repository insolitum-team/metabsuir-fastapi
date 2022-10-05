MAIN_PY = uvicorn app.main:app

run:
	@$(MAIN_PY) --reload

migrations:
	alembic revision --autogenerate -m "no-sign"

migrate:
	alembic upgrade head