# Deploy de Aplica��o Django no Heroku - Projeto Heroku 03 - S3 AWS
* Gerenciamento de arquivos est�ticos disponibilizados em servidor remoto S3 AWS

Conhe�a a aplica��o j� com o Celery no [Heroku](https://herokus3task.herokuapp.com/).

## Caracter�sticas b�sicas desta aplica��o
##### 01. Projeto de duas p�ginas 
##### 02. Uso de Imagem Est�tica
##### 03. Op��o de Upload de M�dia (media - POST de imagem)
##### 04. Biblioteca DeCouple para proteger as vari�veis de configura��o
##### 05. Uso de S3 AWS para armazenar arquivos est�ticos e medias
##### 06. Gest�o dos Settings de produ��o e desenvolvimento separados
##### 07. Gest�o dos Requirements de produ��o e desenvolvimento separados
##### 08. Uso de signals para excluir arquivos de media no servidor quando ultrapasa o limite de tr�s imagens
##### 09. Valida��o da disponibilidade de arquivos de media no servidor e posterior exclus�o da refer�ncia em BD na aus�ncia do arquivo.
##### 10. Servi�os dispon�veis:
###### P�gina 01 - My Images 
   01. Upload e armazenamento no servidor de Imagens
   02. Listagem e exibi��o das ultimas 3 imagens oriundas de upload
   03. Exclus�o de todas as imagens oriundas de upload no servidor
###### P�gina 02 - My Files
   01. Upload e armazenamento no servidor de Arquivos
   02. Exibi��o de link para download do ultimo arquivo oriundo de upload.
   03. Exclus�o de todas os arquivos oriundos de upload do servidor

## Proximos desenvolvimentos
#### P4-S3Task
* Usando Celery e Redis vamos limpar todas as imagens oriundas de upload do servidor apos algum tempo de sua inser��o
           
## Lembretes e cuidados importantes ao utilizar o Heroku
##### 01. Importante para n�o ter retrabalho � saber que a base de dados padr�o utilizada pelo Heroku � o Postgres
* O Heroku utiliza o Postgres como base de dados padr�o, portanto, se estiver utilizando db.sqlite3 ou outro banco de dados para desenvolvimento em sua maquina local, voc� dever verificar a ader�ncia e se necess�rio recriar suas migra��es antes de fazer o deploy no servidor.
##### 02. Lembre-se na op��o gr�tis o Heroku n�o armazena uploads feitos pelo usu�rio a longo prazo.
* Imagens de origem de upload (pasta MEDIA da aplica��o) n�o s�o mantidas pelo HEROKU (uma solu��o � usar amazon S3 para armazen�-las, se necess�rio veja tamb�m o projeto 3)
* Motivos do Heroku apagar os arquivos media: Um servidor de imagens n�o exige complexidade podendo at� ser um servidor apache, e tamb�m para evitar sobrecarga de arquivos no servidor gratis e portanto a queda de sua performance a longo prazo.
* N�o estou utilizando um servidor de arquivos est�ticos externos neste projeto e o heroku apaga os arquivos f�sicos, portanto, criei uma condi��o para apagar os registros da base de dados referentes a estes arquivos deletados (n�o h� regra de neg�cio envolvida aos registros).
##### 03. Importante tentar controlar o conte�do do armazenamento por upload na aplica��o 
* Como n�o vou controlar o conte�do dos uploads pelos usu�rios limitei a visualiza��o de apenas at� 3 imagens (media) dispon�veis no servidor, 
* Coloquei as imagens em percentual de tamanho pequeno para dificultar sua visibilidade imediata e a dist�ncia.

## Algumas dicas para rodar a aplica��o
 Al�m das dicas usuais de instala��o utilizando o GIT, voc� devee seguir as dicas abaixo:
 
#### Valorizar em arquivo .env as vari�veis de configura��o abaixo:
 
##### 1. Para rodar a aplica��o criar um arquivo .env criado para o pacote decouple.
            Usar como base as vari�veis presentes no arquivo .env.var
            
##### 2. Valorizar Config Vars no servidor Heroku as vari�veis de configura��o abaixo:
            DEBUG=False
            SECRET_KEY=''
            SETTINGS_MODULE_PATH=testheroku.settings.production
            ALLOWED_HOSTS=.herokuapp.com 
            DATABASE_URL="Automatic" #Ser� incluida e configurada automaticamente pelo Heroku na inclus�o do Resource/addon do Postgres
            DISABLE_COLLECTSTATIC=1
            USE_S3=True
            AWS_ACCESS_KEY_ID=
            AWS_SECRET_ACCESS_KEY=
            AWS_STORAGE_BUCKET_NAME=
                          
## Situa��o Atual do projeto
##### 1. Deploy de aplica��o Django no Heroku 
=> Situa��o: Feito/Sucesso
##### 2. Gest�o de arquivos est�ticos 
=> Situa��o: Feito/Sucesso (mais detalhes abaixo) 
##### 3. Gest�o de arquivos m�dia 
=> Situa��o: Feito/Sucesso (mais detalhes abaixo)

#### Detalhes da Situa��o do Projeto

##### 1. Arquivos est�ticos - Situa��o: OK
* Envolveu: Files/Images e CSS
* Sem pend�ncias

##### 2. Upload de Arquivos de M�dia (media) - Situa��o: OK
* Envolveu imagens por upload do usu�rio
* Sem pend�ncias

