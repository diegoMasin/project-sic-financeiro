# Sistema de Controle Financeiro Familiar

Esse sistema proporciona ao usuário final, um controle detalhista de sua vida pessoal financeira ou de sua família.
Sic é um sistema que também fornece através de relatórios e simulações um auxílio ao poder de decisão do seu usuário
com relação às decisões mais básicas do seu dia a dia.


# Construção do ambiente

1. SO Linux(rodar o "sudo apt-get update", verificar logo após a a existencia e versões do: pip, python, virtualenv,
 na falta de algum deles, instalar)
2. Criação do repositório git com .gitignore python
3. Criação da pasta para trabalhar com projetos de desenvolvimento. Ex: $home/repositorios/meus_projetos
4. Obter Pycharm como IDE de python
5. Obter Gitkraken para manipular o versionamento git


# Instalaçao e Configuração do início do projeto

1. Dentro da pasta meus_projetos, execute virtualenv .virtualenv -p pythopn3
2. Execute a virtualenv com: source .virtualenv/bin/activate
3. Na máquina virtual instale o Django com: pip install -U django
4. Na pasta meus_projetos, execute o git clone do projeto e deixando a pasta sic_financeiro como irmã da pasta da virtualenv
5. Dentro da pasta sic_financeiro, execute: django-admin.py startproject sicfinanceiro .
6. Testando a aplicação rodando: python manage.py runserver
7. Criando primeira app com: python ../manage.py startapp core
8. Criando requirements com: pip freeze > requirements.txt

Obs¹: O banco não foi criado com a execução do "python manage.py migrate", pois não usaremos logo de cara o sqlite e sim o postgres
Obs²: As ações a seguir, logo após a etapa 8 descrita acima, podem ser averiguadas nos primeiros 20 commits do projeto.
São muitos detalhes, com alguns deles sendo correções de erros.


# Instalaçao do projeto em máquinas de terceiros

1. Dentro da pasta meus_projetos, execute virtualenv .virtualenv -p pythopn3
2. Execute a virtualenv com: source .virtualenv/bin/activate
3. Na pasta meus_projetos, execute o git clone do projeto e deixando a pasta sic_financeiro como irmã da pasta da virtualenv
4. Buscar o local do arquivo requirements.txt dentro do projeto e executar: pip install -r requirements.txt


# Abrindo projeto na IDE Pycharm

1. Criar projeto
2. Escolha o tipo Python
3. Buscar o caminho do projeto.
4. No campo abaixo do caminho do projeto, configurar para a IDE buscar o python de dentro da virtualenv criada
5. Configurar o start server adicionando o caminho do manage.py e no campo abaixo escreva o comando runserver
6. Dentre outras melhores, adicione ao dictionary da IDE, uma lib de language português. Assim a IDE não demarcará
nome de variáveis como estando erradas porque elas não estão em inglês.
