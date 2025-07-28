# Meu Resumo de GIT

## 1 Para que serve?
O Git serve para manter e gerenciar os registros histórico de atualização de um projeto.  

Ele gerencia quais auterações foram realizadas, suas datas e seus autores responsáveis.
  

## 2 Configurando GIT
Após instalado no PC.  
Para configurar ou visualizar as configurações do git será usado o comando `git config`
como parâmetros temos:
* `--local` - para o repositório
* `--global`- para o usuário do sistema
* `--system`- para todos os usuário do sistema
### 2.1 Definindo as configurações:
`git config --local user.name "Erick"` para definir o nome do usário.  
`git config --local user.email "erick_sasaki@hotmail.com"` para definir o e-mail do usário.  
`git config init.defaultBranch "main"` para definir o nome das branchs padrão (convensão).
### 2.2 Visualizando as configurações:
`git config --local user.name` irá retornar → `Erick`  
`git config --global --list` retornas todas as configurações *globais*  


## 3 Autenticando (GitHub)

Digamos que você tenha um **repositório privado** no GitHub e deseja acessá-lo no seu novo computador

Como o Github vai saber que você é você quando der o comando `git clone ...`?


### 3.1 HTTPS (via Token)

Se optar em clonar pela opção HTTPS e vai até seu diretório local e dê o comando:
`git clone https://github.com/NWERICKSASAKI/repositorio-privado.git`, até vai aparecer uma opção de inserir login e senha, porém vai dar erro, pois foi removido e substituído por autenticação via Token

Nesse caso você vai precisar de um token de acesso

#### 3.1.1 Criando o token

1. Acesse o GitHub
2. Clique no seu `Perfil`
3. Na aba lateral que apareceu, clique no [`⚙️ Setting`](https://github.com/settings/profile)
3. Última opção do menu lateral: [`<> Developerns setting`](https://github.com/settings/apps) 
4. Clique em `🔑 Personal Access Tokens ▽` → [`Tokens (classic)`](https://github.com/settings/tokens)
5. Clique no botão `Generate new token ▼` → [`Generate new token (classic)`](https://github.com/settings/tokens/new)

Olhando os parâmetros, temos os seguintes:
* `Note` - Descrição do propósito deste Token dele, exemplo: `acesso do John, meu amigo que vai cuidar do front-end do projeto`
* `Expiration` - Até que data expira o token, convém deixar pouco tempo, só da pessoa acessar mesmo 
* `Scope` - Delimita as permissões do usuário (que acessar com esse token)  

Por fim só clicar em <span style="background-color:green; color:white;"> [ Generate token ]</span>, então irá gerar algo tipo `fjdksfjkdls_dfjskfhsdajknclaghdisfj` então só copiar o token e salvar ou enviar.

#### 3.1.2 Usando o token

✅ Só dar o `git clone https://github.com/NWERICKSASAKI/repositorio-privado.git` e autenticar com o token.


#### 3.1.3 Armazenando o token [TO-DO]

`git config --global credential.helper`  
* `cache` - Windows não suporta
* `store` -   

...e nos próximos clones que fizer de novo não vai precisar do token.

### 3.2 via Chave SSH
Baseia-se no uso de 2 chaves: Pública e privada.

A chave privada fica na sua máquina e a chave pública fica no GitHub

Assim que estiver configurado o par de chave corretamente, você conseguirá autenticar e clonar/editar seus repositórios normalmente.

#### 3.2.1 Gerando um par de chaves
Só inserir o comando a seguir (óbvio, colocando o seu respectivo email) → `ssh-keygen -t ed25519 -C "erick_sasaki@hotmail.com"` e dê ENTER

Insira uma *passphrase* (senha) e dê ENTER

✅ Pronto, chaves geradas!

#### 3.2.2 Salvando a chave pública

Primeiro vamos start o agente ssh:
`eval "$(ssh-agent -s)"` ao der ENTER retornará algo assim `Agent pid 1547` (indicando que o agente shh está sendo executado)

`ssh-add ~/.ssh/id_ed25519` para adicionar a chave privada à nossa máquina



#### 3.2.3 Verificando as chaves da nossa máquina
Como verificar se tem uma chave ssh na nossa máquina:
`ls -al ~/.ssh`, gerando algo assim:
```
NW@DESKTOP-G45NJUM MINGW64 ~/.ssh
$ ls -al ~/.ssh
total 27
drwxr-xr-x 1 NW 197121   0 Jun 17 18:56 ./
drwxr-xr-x 1 NW 197121   0 Jul 24 18:57 ../
-rw-r--r-- 1 NW 197121 464 Jun 17 16:00 id_ed25519
-rw-r--r-- 1 NW 197121 106 Jun 17 16:00 id_ed25519.pub
-rw-r--r-- 1 NW 197121 828 Jun 17 18:56 known_hosts
-rw-r--r-- 1 NW 197121  92 Jul 31  2023 known_hosts.old
```

No caso o `id_ed25519.pub` é a chave pública. 

Para consultar ou visualizar a chave pública é só dar o seguintes comandos: `cd ~/.ssh` → `cat id_ed25519.pub` 

Como resultado vamos ter algo similar nas linhas de:
`sssh-12345 FDHJSAFHDSAJKCHSADJKHFDSURFJEHRLKWQJD e@mail.com`

✅ Copie a sua chave a vamos colocá-la no GitHub.

#### 3.2.4 Adicionando a chave pública ao GitHub

1. Acesse o GitHub
2. Clique no seu `Perfil`
3. Na aba lateral que apareceu, clique no [`⚙️ Setting`](https://github.com/settings/profile)
4. Última opção do menu lateral: [`🔑 SSH and GPS keys`](https://github.com/settings/keys) 
5. Clique em <span style="background-color:green; color:white;"> [ New SSH key ]</span>

Haverá 3 campos na página, preencha de forma similar:
* **Title**:  'Meu PC que gerou a chave'
* **Key type**: `Authentication key`
* **Key**: aqui você cola a sua chave pública! → `sssh-12345 FDHJSAFHDSAJKCHSADJKHFDSURFJEHRLKWQJD e@mail.com`

## 4 Criando e Clonando Repositórios

### 4.1 Criando um novo repositório

Crie um novo repositório e copie o endereço de clone.  
Exemplo: `https://github.com/NWERICKSASAKI/repositorio-novo.git`

Vá ao seu diretório do seu projeto e dê `git init`.  
Em seguida `git remote add "origin" https://github.com/NWERICKSASAKI/repositorio-novo.git`

### 4.2 Clonando um repositório existente

Vá até a página do repositório do GitHub e copie o endereço do clone.  
Exemplo: `https://github.com/NWERICKSASAKI/repositorio-existente.git`

No diretório local dê o comando:  
`git clone https://github.com/NWERICKSASAKI/repositorio-existente.git`  
Assim será feito o download do repositório em uma nova pasta.

Caso queira **personalizar o nome da pasta**, basta acrescenta-la no final:  
`git clone https://github.com/NWERICKSASAKI/repositorio-existente.git nome-que-eu-quero`

Caso queira clonar uma branch diferente da principal, basta passar como argumento conforme exemplo:
`git clone https://github.com/NWERICKSASAKI/repositorio-existente.git --branch nome-da-branch --single-branch`

Para visualizar com quem o repositório local está conectado:  
`git remote -v`  
Como resultado verá algo como `origin https://github.com/NWERICKSASAKI/repositorio-existente.git`

## 5 Salvando Alterações no Repositório Local

`git status` vai revelar quais arquivos não estão sendo rastreados e quais arquivos sofreram modificações.  

`git add .` este comando adicionado **TODOS** os arquivos para serem rastreados, caso queira algum arquivo em específico só digitar o nome do arquivo no lugar do ponto.

Caso queira retirar algum arquivo que foi adicionado ao stagging temos duas opções:  
* `git reset bloco_senhas.txt`
* `git restore --staged bloco_senhas.txt`

Para commitar, ou seja, salvar as modificações no repositório local é realizado o comando abaixo, personalizando o cometário:
`git commit -m"Fz algmas alterações relveantes"`

Caso deseja substituir a última mensagem do commit você pode utilizar `git commit --amend -m"Fiz algumas alterações relevantes"`

`git log` exibe o histórico dos nossos commits, por *hash*, *autor* e *data*.

Se quiser algo mais resumido, tem a opção de usar `git reflog`


## 6 Desfazendo alterações no Repositório Git

Vamos supor que fizemos algumas ~~merdas~~ alterações e gostaríamos de  ~~dar rollback~~ voltar como estava antes.

Localize qual commit gostaria de voltar olhando o `git log` e copir o hash:

```
commit f4f4a01ab1a0c197a0fe9e4cebfa344407f5e5be
Author: Erick <erick_sasaki@hotmail.com>
Date:   Fri Jul 18 09:37:10 2025 -0300

    Nova função ta dando merda e corrigi parte dos bugs que deu

commit 3ca2052885c8c7aa165abdf62f5dfa411b292bc1
Author: Erick <erick_sasaki@hotmail.com>
Date:   Mon Jun 30 10:47:38 2025 -0300

    Comecei a colocar uma nova funcao

commit 9f22ab3664556b6fb8637e3ef2a73a59b92540fe
Author: Erick <erick_sasaki@hotmail.com>
Date:   Mon Jun 16 11:54:30 2025 -0300

    Tudo funcional!!
```

Vamos supor que queremos voltar ao estado do commit que estava *"Tudo funcional!!"* na qual o seu respectivo hash é `9f22ab3664556b6fb8637e3ef2a73a59b92540fe`.

Temos 3 opçõs de voltar a esse git com base nesses 3 parâmetros seguido pelo hash:

### 6.1 `git reset --soft`
Volta ao estado do commit e:
* **Não apaga** novos arquivos que não estavam presentes no momento do commit;
* Novos arquivos modificões que estava trabalhando antes de dar reset estão ja **trackeado** (ja estarão dentro do `git add`).

### 6.2 `git reset --mixed` (padrão)
Volta ao estado do commit e:
* **Não apaga** novos arquivos que não estavam presentes no momento do commit;
* Novos arquivos modificões que estava trabalhando antes de dar reset estarão **untracked** (vai precidar dar `git add`).

### 6.3 `git reset --hard` (padrão)
Volta ao estado origianal do commit, isso inclui:
* **Apagar** todos novos arquivos que não estavam presentes no momento do commit;


## 7 Enviando e Baixando Alterações ao Repositório Remoto

Vamos supor que você um projeto local e gostaria de criar um repositório no GitHub.

Basta seguir os seguintes passos:
* Crie um novo repositório no GitHub e copie o seu endereço;
* Vá na pasta do seu projeto e dê `git init` → `git add .` → `git commit -m"Meu primeiro commit"`
* Dê o comando a seguir com o link do GitHub `git remote add origin https://github.com/NWERICKSASAKI/novo_projeto.git` para conectar o repositório local ao remoto.
* `git branch -m main` para renomear a branch atual para *main*
* `git push -u origin main` para empurrar a nossa branch *main* à branch *origin* (remoto) e indicar através do `-u` ou `--set-upstream` que a branch *main* está ligada ao *origin/main* 
* e quaisquer novas alterações commitadas, basta `git pull` para enviá-las ao repositório remoto.

## 8 Trabalhando com Branches

`git checkout -b nome_da_branch` este comando cria e já troca para esta nova branch.

Para só trocar de branch, por exemplo, voltar à *main* → `git checkout main`  

`git branch` lista todas as branches do repositório, o branch que estamos no momento é indicada com *   

`git branch -v` mostra o último commit de cada branch  

`git merge nome_da_branch` mescla a branch atual com a branch indicada.  

`git branch -d nome_da_branch` deleta a branch mencionada


## 9 Lidando com Conflitos

Vamos supor que 2 pessoas estão trabalhando em um repositório no GitHub.

**A** e **B**, a paritr de um mesmo commit no GitHub deram `git pull` ou clone e comeraçam a trabalhar nele.

**A** realizou algumas alterações e já subiu com `git push`

Porém logo depois **B** fez suas alterações no mesmo arquivo deu `git commit -m"comentarios de B"`,  foi tentar dar `git push origin main` porém retornou um erro!

O erro se refere justamente que há um conflito nas modificações feita por **B** em relação a versão que está no GitHub subidas por **A** e então será necessários tratar os conflitos:  

* `git pull` para baixar as alterações
* O arquivo que está com conflito aparecerá modificado exibindo duas versões diferentes, no caso, basta **editar e salvar** como deverá ser a versão final correta, e dar um `git commit`.
* por fim `git push` e conflito resolvido.  

Mas o que é o tal do `git pull`?

### 9.1 git fetch + git merge = git pull

O `git pull` é a junção dos comandos:
* `git fetch` (baixa as aterações do repositório remoto) e 
* `git merge` (mescla as branchs / alterações).

Caso queira baixar o conteúdo remoto sem mesclar com a branch local, usar o `git fetch origin main`

Para visualizar as diferenças entre as branchs, ou seja, o que foi modificado `git diff main origin/main`

Para 