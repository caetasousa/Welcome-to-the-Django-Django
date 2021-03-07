#Eventex

Sistema de eventos

##Como desenvolver
1. Clone o repositorio.
2. Crie um virtual .env com python 3.9
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Execute os testes

```Console
git clone git@github.com:caetasousa/eventex.git wttd
cd wttd 
python -m venv .wttd 
ir ate a pasta script e ativar o ativate.bat 
pip install -r requeriments-dev.txt
cp contrib/env-sample .env
python manage.py test
```

##Como fazer o deploy
1. Crie uma instancia no heroku
2. Envie as configuraçoes para o heroku
3. Defina uma SECRET_KEY para a instancia
4. Defina DEBUG=False
5. Configure o servico de email
6. Envie o codigo para o heroku

````Console
heroku creat minhainstancia
heroku config:push
heroku config:set SECRET_KEY= python contrib/secret_gen.py
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force

````