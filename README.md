## 1. Running application on local machine
go to `src` folder and execute commands
``` 
1. $ python manage.py collectstatic
2. $ python manage.py migrate
3. $ python manage.py createsuperuser  # Create your admin
4. $ python manage.py runserver
```

## 2. Running application with Docker:
```
1. docker-compose build
2. docker-compose run
```

## 3. Pages

Home: http://localhost:8000/

![home](http://dl4.joxi.net/drive/2021/02/03/0025/3664/1670736/36/b7a4225d3a.jpg)

Swagger: http://localhost:8000/swagger/

![swagger](http://dl3.joxi.net/drive/2021/02/04/0025/3664/1670736/36/ca5d99e269.jpg)

### 4. Adding Articles with Html:
Send request `POST http://localhost:8000/api/articles/` with body:
```
{
  "title": "Article with Image",
  "subject": "Imaged article",
  "body": "<div><h2>Image:</h2><p><img src="http://dl3.joxi.net/drive/2021/02/04/0025/3664/1670736/36/ca5d99e269.jpg"></div>",
  "author": 1
}
```
Then open article page: `http://localhost:8000/articles/{article_id}`

![swagger](http://dl4.joxi.net/drive/2021/02/04/0025/3664/1670736/36/1c9692c74b.jpg)