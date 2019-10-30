# Mayfarm Coding Test

메이팜소프트 코딩 테스트 프로젝트이며, Flask 를 사용해서 웹 페이지를 구성 하였습니다.

## Usage

venv를 사용하여 가상환경을 만들고, 활성화 후에 라이브러리를 설치 한다.

```python
# 가상환경 만들기
python -m venv .env
source ./.env/bin/activate

# 라이브러리 설치
pip install -r requirements.txt
```

### Flask 환경설정

```python
export FLASK_APP="manage.py"

# development
export FLASK_ENV="development"
# production
export FLASK_ENV="development"
```

### Create DB

```python
flask create_db
```

### Create Model

```python
flask create_model
```

### Run Flask server

Mayfarm 애플리케이션을 실행합니다.

```python
flask run
```

### Run Github Crawler

Github에서 딥러닝 관련 레포를 2페이지까지 크롤링하기

```python
flask github --keyword=딥러닝 --page=2
```