#   Instalação

1-	Instalar o Python disponível em https://www.python.org/downloads/ e reiniciar o computador

2-	Instalar MSQLWorkbench disponível em https://www.mysql.com/products/workbench/


3-	No MysQl, criar database com as seguintes configurações:
           ‘NAME': 'system_cel',
           'USER': 'univesp',
           'PASSWORD': '06975071'
           
                  
4-	Baixar o pacote SystemCel, por download ou via GitHub Desktop. A aplicação está no Master
5-	No diretório onde foi copiado o pacote systemcel, via shell ou CMD (linha de comando),digite:
            py -m venv cel
            cd cel
            cd Scripts
            activate.bat
            cd..
            cd..
            pip install -r requirements.txt

6-	Ou, opcionalmente, caso haja algum erro, rodar o bloco de comandos a seguir:
            py -m pip install --upgrade pip
            py -m pip install asgiref
            py -m pip install Django
            py -m pip install django-braces
            py -m pip install django-cleanup
            py -m pip install django-crispy-forms
            py -m pip install pytz
            py -m pip install six
            py -m pip install sqlparse
            pip install --only-binary :all: mysqlclient


7-	py manage.py migrate
8-	py manage.py runserver




![This is an image](https://user-images.githubusercontent.com/20569301/138988305-ddd7b7bd-48ed-41ab-9a49-e0149eb45d09.jpg)
![tela1](https://user-images.githubusercontent.com/20569301/138989371-31bbcded-b0ea-4cb5-abb5-45366d9bd329.png)
<div align="center">
<img src="https://user-images.githubusercontent.com/20569301/138988305-ddd7b7bd-48ed-41ab-9a49-e0149eb45d09.jpg" width="700px" />
</div>
