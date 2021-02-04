# 1. Application Setup
go to `src` folder and execute commands
``` 
1. $ python manage.py collectstatic
2. $ python manage.py migrate
3. $ python manage.py createsuperuser  # Create your admin
4. $ python manage.py runserver
```

### Running application with Docker:
```
1. docker-compose build
2. docker-compose run -d
```

### Resources

Home Page: http://localhost:8000/

![home](http://dl4.joxi.net/drive/2021/02/03/0025/3664/1670736/36/b7a4225d3a.jpg)

API Spec: http://localhost:8000/swagger/

![swagger](http://dl3.joxi.net/drive/2021/02/04/0025/3664/1670736/36/ca5d99e269.jpg)

### Adding Articles with Html:
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


# 2. Profiling Features:

## DjangoSilk:
[DjangoSilk on Github]("https://github.com/jazzband/django-silk")

Go to resource: http://localhost:8000/silk/ to open django silk profiler dashboard:
![silk](http://dl4.joxi.net/drive/2021/02/04/0025/3664/1670736/36/75fdb80f6d.jpg)

Watch request details:
![request](http://dl3.joxi.net/drive/2021/02/04/0025/3664/1670736/36/e2fae1c147.jpg)

## Sentry Performance Tracing:

[Documentation](https://docs.sentry.io/platforms/python/guides/django/performance/) for switching Sentry Performance monitoring for Django

####Open Performance Statistics:

![sentryperf](http://dl3.joxi.net/drive/2021/02/04/0025/3664/1670736/36/eac79d934b.jpg)

#### Open Request Statistics:

![sentryreq](http://dl4.joxi.net/drive/2021/02/04/0025/3664/1670736/36/da2d69a9dc.jpg)

#### Analize Request timings:

![sentrytiming](http://dl3.joxi.net/drive/2021/02/04/0025/3664/1670736/36/30297edaa7.jpg)

# 3. Switch (NO/OFF) profiling:

1. To Switch on `DjangoSilk` profiling set in django settings: DEBUG=True (False to switch OFF)
2. To Switch on `SentryPerformance` profiling:
 * Login to admin panel `http://localhost:8000/admin` as admin user: `admin / adminadmin`
 * go to `Constance` configurations
 * set `SENTRY_TRACING_ENABLED` property checked to enable tracing and writing performance stats to Sentry.