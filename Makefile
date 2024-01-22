launch-dev:
	uvicorn app.main:app --reload

launch:
	uvicorn app.main:app --host 0.0.0.0 --workers 2