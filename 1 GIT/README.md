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

Por fim só clicar em <span style="background-color:green"> [ Generate token ]</span>, então irá gerar algo tipo `fjdksfjkdls_dfjskfhsdajknclaghdisfj` então só copiar o token e salvar ou enviar.

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
5. Clique em <span style="background-color:green"> [ New SSH key ]</span>

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