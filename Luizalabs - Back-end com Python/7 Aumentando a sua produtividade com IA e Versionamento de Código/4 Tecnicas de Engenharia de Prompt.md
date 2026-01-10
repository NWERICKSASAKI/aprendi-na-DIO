# Técnicas de Engenharia de Prompt

## 1 Introdução

(Apresentação do curso e da professora)

## 2 Conhecendo o Prompt

### 2.1 O que é um prompt?  

* Uma frase, pergunta, instrução para a IA realizar uma ação específica.  
* Usar em inglês é mais efetivo devido a base de linguaguem (LLM).  
* Nem sempre a IA estará certa, por isso sempre deve haver alguém revisando.

### 2.2 A importância de um Prompt

São importante que sejam claros e objetivos para guiar o modelo para criar o que desejamos obter.

### 2.3 Como os Prompts Transformam as interações

* Para uma comunicação mais direta e eficiente.
* Para respostas mais específicas e mais rápida.
* Caso contrário poderia retornar um texto muito longo ou genérico.

### 2.4 Principais Aplicações dos Prompts

Os prompts estão presentes em diversos contextos:

* Geração de material didático, exercícios multiplas escolas.
* Simulação de diálogos
* Simulação históricas
* Simulação de entrevistas
* Desenvolvimento de sofware, criar ou explicar código
* Testes
* Prototipação
* Negócios e marketing (post, imagens, campanhas)
* Pesquisa de negócios
* Automação
* Ciência e Pesquisa (revisão de texto, criar sumário, analisar dados)
* Mídia (criar diálogos, roteiros, etc)
* Área jurídica
* etc

## 3 Componentes de um Prompt

Os componentes vão contribuir para estruturar nossos solicitações / comandos que será interpretado pela IA.

Eles vão desempenhar um papel para essencial para garantir a clareza e precisão e formam as técnicas de engenharia de prompts.

### 3.2 Instruções

São comandos ou instruções simples ou até complexas para retornar o que queremos.

### 3.2 Exemplos (Few-shot Learning)

Zero-shot - executar a tarefa usando o conhecimento base sem um exemplo

One-shot - é quando se passa um exemplo para a IA executar o comando para se basear.

Few-shot - quando se passa alguns exemplos para servir de modelo para se basear

### 3.3 Contexto ou Configuração

Onde é definido o papel do modelo o cenário da IA.

Exemplo: 
```txt
Imagine que você é um guia de turismo explicando uma cidade para visitantes. O contexto pode incluir o cenário de uma cidade histórica como o Egito, destacando pontos turísticos e tradições culturais
```

### 3.4 Restrições ou Limitações

Define-se que a resposta deve seguir, como limite de comprimento, formato, escopo do conteúdo.

Exemplo:
```txt
Explique o conceito de loops em programação em até 50 palavras.
```

### 3.5 Conteúdo Principal

Texto central do prompt que contém os dados relevante pro modelo de IA realizar os comandos: parágrafo, tabela, etc.

É um combinado de instruções da tarefa que a IA precisa realizar.

Exemplo:

Instrução: 
```txt
Liste 3 ideias para um evento comunitário.
```

Conteúdo principal:
```txt
O evento deve engajar pessoas de todas as idades e promover a sustentabilidade
```

### 3.6 Indicações 

Guiam a resposta para gerar saídas específicas, usando estímulos como listas, tópicos, resumos, etc.

### 3.7 Formato de Saída

Especifica a forma da resposta como "Apresente no formato JSON" ou "Liste os resultados como uma sequência de tópicos claros." - orienta a saída visual.

### 3.8 Conteúdo de Suporte

Dados extras que ajudam a tarefa, como daa ou preferências, por exemplo: "Use o contexto atual de dezembro de 2024 nas respostas."

## 4 Técnicas de Engenharia de Prompt

### 4.1 Introdução as Técnicas de Engenharia de Prompt

O que é **Engenharia de Prompt**: Todo processo para criar, listar e organizar com o objetivo para obter as respostas mais úteis, precisas e relevantes.

Basea-se em técnicas que utilizam os componentes dos prompts.

### 4.2 Entendendo o objetivo da prática

(Prof mencionando que vai aplicar as técnicas de forma a desenvolver uma proposta de jogo)

### 4.3 Aplicando Instruções e Repetição

**Instrução clara**: Técnica que organiza as orientações sejam objetivas e detalhadas, evitando ambiguidade.

Pode ser passando um objetivo inicial, a proposta da tarefa.

**Repetir instruções no final**: reforça as instruções do pedido, garantindo que siga as orientações corretamente.

```txt
Ajude a criar uma proposta de jogo narrativo chamado "Adventure DIO Quest". O jogo será uma aventura onde os jogadores tomam decisões que afetam o desenrolar da história. O Jogo deve incluir:

- Uma introdução à história.
- As principais mecânicas do jogo.
- Uma descrição do público alvo. 

---

Lembre-se, após a geração revise a proposta de 'Adventure DIO Quest' para garantir que ela inclua todas as seções: história, mecânica e público alvo.
```

### 4.4. Entendendo o Guardrails

**Guardrails**: Limitar as infromações para que sejam relevantes, para que sejam aplicáveis

Continuação do prompt:

```txt

---

Certique-se de que a proposta seja prática e simples de implementar para um jogo básico.
Evite mecânicas complexas ou irreais.
```

Um guardrail que alguns modelos de IA tem são de não gerar saídas prejudiciais, de direitos autorais, conteúdo impróprio ou anti-ético.

### 4.5 Preparando nossa Saída

**Preparar a saída**: indicar como você deseja que o modelo entrega a resposta, ou seja, o formato.

```txt
Organize a proposta no seguinte formato:

- Nome do jogo
- Introdução à História
- Mecânicas Principais
- Público-Alvo
- Estilo gráfico ou visual
- Conclusão
```

### 4.6 Solicitação de Cadeia de Pensamento

**Solicitação de Cadeia de Pensamento**: Instrução para que o modelo responda passo a passo, explicando o raciocínio até chegar à conclusão final.

```txt
Explique por que as mecânicas escolhidas são interessantes para o público-alvo e como elas se alinham ao tema da aventura.
```

### 4.7 Especificando a estrutura de Saída

**Especificando a estrutura de Saída**: Indica o formato exato da resposta, como JSON ou lista, ajudando a obter resultados roganizados e úteis.

```txt
Crie a proposta do jogo em formato de tópicos.
```

```txt
Crie a proposta em formato de texto corrido.

```txt
Crie a proposta em formato de markdown.
```

### 4.8 Dividindo a Tarefa

**Dividir a tarefa**: Quebra uma tarefa complexa em várias etapas menores, facilitando para o modelo responder de forma lógica e organizada.

```txt
Descreva a introdução da história de 'Adventure DIO Quest'. Comece com o jogador acordando em um lugar misterioso.
```

### 4.9 Adicionando Sintaxe Clara

**Adicionar Sintaxe Clara**: Organiza o prompt com formatações como listas, títulos ou tabelas, tornando as instruções mais visuais.

```txt
Formate a proposta do jogo em uma tabela visual para uma apresentação rápida.
```

### 4.10 Aplicando prompts para gerar imagens com o Microsof Copilot

```txt
Crie uma imagem de uma ilha misteriosa com árvores sombrias, estilo pixelart, cenário de jogo.
```

Caso não esteja gerando a imagem que esteja desejando tente em inglês para ter maior acertividade.

```txt
Gere um personagem feminino em estilo pixel art, para um jogo. Cabelos loiros e cacheados.
```
