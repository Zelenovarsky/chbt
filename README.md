# chbt
Хлеб-кот чатбот

на докерхабе все лежит, чтобы звпустить:

```docker run -p5000:5000 --rm -it zelnovarsky/chbt:latest```

переходим на http://0.0.0.0:5000/ и можно тыкать

Для запуска на локалхосте: 

```docker build . -t chbt && docker-compose up```

Чтобы потестить и потыкать, переходим на 
http://localhost:8080/docs

Еще все поднято на Heroku:

https://salty-earth-71701.herokuapp.com/docs

Ci/CD на Travis ci с деплоем в хероку и докерхаб