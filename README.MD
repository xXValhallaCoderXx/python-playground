### Access Docker DB
docker exec -it python-playground_db_1 psql -U postgres


### Run Tests
- pipenv run pytest --cov=src 