Memo: Simple CRUD note taking app

![Memo](https://i.imgur.com/CVXvasd.png)

## Get the source code
```
> git clone https://github.com/vadimkerr/django_memo
```

## Change environment variables
```
> cp example.env .env
```
Then paste in your environment variables into .env file

## Compose up
```
> docker-compose up --build -d
```

## Run migrations
```
> docker-compose run web python manage.py migrate
```
