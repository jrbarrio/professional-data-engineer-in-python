```
pyenv virtualenv 3.9.20 professional-data-engineer-in-python
echo "professional-data-engineer-in-python" > .python-version
pip install pipenv
pipenv install dbt-core dbt-postgres dbt-duckdb
pipenv install pandas
```