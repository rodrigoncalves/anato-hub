Sistema Anato - HUB
=====================

Sistema desenvolvido dentro da disciplina de Verificação e Validação de Software, no segundo semestre de 2014, na Universidade de Brasilia.

------------

O Anato é um sistema de gerenciamento de laudos da Unidade de Anatomia do Hospital Universitário de Brasilía. Desenvolvido em Python, utilizando o framework web Django, e, durante o desenvolvimento, serão aplicadas técnicas de verificação e validação, tais como Protótipo, TDD e BDD.

------------

Instalação
------------
Após baixar, extrair os arquivos-fonte do Anato, entre no diretório da aplicação e siga os passos:

1) Instale o pacote pip:
```
# apt-get install pip
```
2) Instale os pacotes necessários:
```
# pip install -r requirements.txt
```
3) Salve os arquivos `configs/database.py.template`, `configs/ldap.py.template` e `server.py.template` retirando a extensão `.template`.

4) Edite o arquivo `configs/server` e adicione um valor para `SECRET_KEY`.

5) Crie as tabelas do banco de dados e crie um super usuário do Django:
```
$ python manage.py syncb
```
6) Rode a aplicação:
```
$ python manage.py runserver
```
7) Em seguida abra seu navegador em http://127.0.0.1:8000.

Se algum erro for encontrado durante a instalação, cheque seu ambiente e tente encontrar o problema, caso contrário, contate um dos desenvolvedores.

------------
2º/2014 - UnB
