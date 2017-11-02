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


# Iniciando o Desenvolvimento no Windows

Até aqui, o que foi relatado envolve o desenvolvimento em máquinas com SO Linux. Este tópico é especial para startar o desenvolvimento do projeto em qualquer outra máquina que utilize o SO Windows. Segue todos os passos.

# Instale:
Obs: Sempre que perguntar se deve adicionar algo ao Path do Windows, diga sim ou marque o check.
1. o Python para Windows 3.6(https://www.python.org/downloads/release/python-363/)
Obs: Instale o Python no Seguinte caminho para facilitar os comandos: C:\Python36
2. o Git para Windowns(https://git-scm.com/download/win);
3. o Gitkraken para manipular o git(https://www.gitkraken.com/download); 
4. o Pycharm para o desenvolvimento como IDE(https://www.jetbrains.com/pycharm/download/); 
5. o PgAdmin para o uso do banco de dados com postgres(https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v2.0/windows/pgadmin4-2.0-x86.exe);
6. o Postegres para o Banco de dados(https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows);
Obs: na instalação, quando pedir a senha do superusuário postgres, coloque a senha postgres, seguindo assim o padrão de acesso ao banco já definido no código de develop.
7. um kernel de Linux(Cygwin ou Power Shell) para que em casos extremos seja possível resolver um problema insurgente(https://www.cygwin.com/);

# Clonando e Configurando(siga os passos em todos os detalhes):
Obs: Muito do que foi relatado para o caso de ser linux o SO, aqui não funcionará, por mais que estejamos usando um simulador de kernel do linux, devemos instalar e configurar no próprio Windows. Como o caso da virtualenv(máquina virtual de desenvolvimento), precisaremos instalar no windows diretamente sem usar o Cygwin ou Power Shell.
1. Abra o cmd do windows
2. Verifique as seguintes versões do que foi instalado até para averiguar se estão realmente instalados, digite:
python -V
git --version
Obs: A partir do python instalado, vamos instalar todo o restante, virtualenv, pip, django, etc.
3. Crie na unidade C, a pasta "develop", dentro a pasta "meus_projetos", e logo mais dentro a pasta sic;
4. A pasta Sic conterá a pasta do repositório git do projeto e como "irmão" a pasta da virtualenv(não crie agora essas pastas);
5. Vamos instalar no windows e criar uma virtualenv(https://fernandofreitasalves.com/tutorial-virtualenv-para-iniciantes-windows/)
Obs: Dentro do python para windows está o gerenciador de instalação que usaremos para tudo que instalarmos, o Pip(já é para existir dentro dele, siga os passos do arquivo, ou este abaixo)
 - Instale a virtualenv no windows com o comando: c:\Python36\Scripts\pip.exe install virtualenv
 - Dentro da pasta "meus_projetos" digite o comando: c:\Python36\Scripts\virtualenv.exe sicvirtual
 - Ative a virtualenv com: sicvirtual\Scripts\activate ( observe que no começo da linha de comandos há um parenteses com o nome da virutalenv que está sendo usada)
 - Ainda dentro da pasta "meus_projetos", vamos clonar o projeto com: git clone https://github.com/diegoMasin/sic_financeiro.git
 - PRONTO a primeira parte.
 6. Usando o gitkraken abra o repositório do projeto;
 7. Usando o pycharm, abra o repositório do projeto;
 8. Retornando ao prompt de comandos, onde parou, entre na pasta do repositório com: cd sic_financeiro;
 Obs: Dicas de comandos basico, cd entra pasta, cd .. volta pasta, dir lista tudo de dentro, cls limpa tela.
 9. Execute a instalação de todas as dependencias do projeto com: pip install -r Requirements.txt(aguarde um pouco e todas as dependencias e ferramentas finais para o funcionamento do projeto, serão instalados);
10. Fora isso serão precisos apenas criar umas variáveis de ambiente que o projeto sentirá falta pra poder rodar:
 - Crie um arquivo dentro da pasta do repositório de nome ".env", no mesmo nível de arquivos como .gitignore
 - Acesse o site: https://www.miniwebtool.com/django-secret-key-generator/
 - Após gerar uma SECRET_KEY, dentro do arquivo texto ".env" escreva da forma que fique como no exemplo a seguir: SECRET_KEY=^cu!f3@!yuu2$%4u8)zw!$o6_xc-@y-l(fpl#6o0rf-tz$6gt4
 - Escreva outra linha: DEBUG=TRUE
 - Pronto!
11. Abra o PG admin 3 e crie/configure um server com um banco de dados e um schema tal qual o projeto requer:
 - Crie o Server(se nao tiver criado na instalação do postgres. Ponha o nome de localhost.)
 - Crie o banco de dados com o nome de "sic_financeiro"
 - Crie o schema com o nome de "sic"
12. Pelo prompt de comandos, e com a virtualenv ativada, escreva: python manage.py migrate 
13. Configure o pycharm(lembrar de criar o interpreter apontando para o python da virtualenv) para executar o projeto ou use: python manage.py runserver


## Configurando o Heroku para uso no terminal
OBS: antes de seguir estes passos instale o Heroku Cli(tem versões Linux e Windows)
1- Navegue pelo terminal até chegar na pasta principal do repositório git;
2- Certifique-se de que está na branch master(git checkout master);
3- Certifique-se de que já exista o remoto do github(git remote);
4- Adicione o reposítório remoto do heroku(git remote add heroku https_da_sua_app_no_heroku);
5- Faça o login(heroku login);
6- Logado no heroku o comando de deploy é o seguinte: git push heroku master;
7- Para executar a migrate para o banco de dados use: heroku run python manage.py migrate(lembre-se: esteja dentro do branch master do seu projeto);
