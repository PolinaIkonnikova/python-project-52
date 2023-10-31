# Task Manager

### Hexlet tests and linter status:
[![Actions Status](https://github.com/PolinaIkonnikova/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/PolinaIkonnikova/python-project-52/actions)
[![PyCI](https://github.com/PolinaIkonnikova/python-project-52/actions/workflows/PyCI.yml/badge.svg)](https://github.com/PolinaIkonnikova/python-project-52/actions/workflows/PyCI.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f3f0093bd6242cd36fb2/test_coverage)](https://codeclimate.com/github/PolinaIkonnikova/python-project-52/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/f3f0093bd6242cd36fb2/maintainability)](https://codeclimate.com/github/PolinaIkonnikova/python-project-52/maintainability)

```
git clone git@github.com:PolinaIkonnikova/python-project-52.git && cd python-project-52
```

#### for poetry: 
```
poetry install
```

#### for requirements.txt (in venv):
pip install -r requirements.txt

You need to make .env file with variables:
(нужные значения есть во временном файлике tmp_env в корневой директории)

- ROLLBAR_KEY (roll bar key) 
- SECRET_KEY (secter key Django) 
- DEBUG (False or True)

#### for local running on http://127.0.0.1:8000:
```
make migrate
make run
```