# Métodos de Machine Learning Bioinspirados

## 1 Métodos de Machine Learning Bioinspirados

De onde veio a ideia de ensinar uma máquina?

**Veio do raciocínio humano**: Como um humano faria uma aplicação para uma máquina conseguir fazer o mesmo.

**Exemplo**: Fazer uma máquina para reconhecer faces humanos, reconhecer objetos no trânsito. Busca a mesma qualidade da visão humana.

Alguns métodos de ML buscam inspiração na Natureza, como formigas, abelhas, pássaros etc.

O que são **algoritmos bioinspirados**?

- Inspirados no comportamento de seres vivos em convivência social;
- Conhecimento colaborativo/compartilhado;
- Métodos Heurísticos (não determinísticos);
- Buscam a melhor solução global;

Exemplo:
Em **colônia de formigas** com uma fonte de comida,  
as formigas escolhem as rotas com mais feromônio  

Isso inspirado no roteamento de internet, para rotas de robôs.

Em **colônia de abelhas**, com planejamento de voo, para distâncias menores para buscar os insumos para fazer mel, além da hierarquia dentro da colmeia.

**Redes Neurais**, **Cérebro**, arquitetura de Von Neumann.

**Genética**, geração de filhos dos melhores pais de solução acrescentado de mutações para obter soluções ainda melhores.

**Lógica Fuzzy**, lógica nubulosa, *Qual taça tem a quantidade de vinho ideal pra você?*, *Qual o tamanho de uma pessoa alta?* Tem-se um range para determinar a resposta.

## 2 Algoritmos Heurísticos x Determinísticos

**Determinístico**: 2 + 2 = 5? Todos diriam Não  
**Heurístico**: Fulano é o mais bonito da turma?  

Se pegarmos 10 pessoas diferentes, na heurístico pode obter inúmeras respostas diferentes.

**Lógica booleana** - aceita só 0 ou 1.  
**Lógica difusa (fuzzy)** - aceita valores entre 0 e 1.

No cenário que mais usamos de ML usamos RNA (Redes Naturais Artificiais).

### Aplicações em Sistemas

**Robô autônomo** utiliza o método da colônia de formiga, usa a rota que mais foram usadas pelos outros robôs. Onde passou e aprovou, marca `1` na matriz, caminhos ruins (sem saída, por exemplo) marca `-1` e não visitados `0`.

**Redes** com fluxo de dados, usando método colônia de formiga ou enxames de abelhas para otimizar a rota de entrega. (por falta de tempo para testar todas as rotas possíveis)
