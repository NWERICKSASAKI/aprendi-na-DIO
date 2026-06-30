# 5 Trabalhando com Arte 2D

## Onde posso encontrar assets pro meu jogo?

<OpenGameArt.Org>

<Kenney.nl>

<itch.io>

<freesound.org>

## Como importar assets no Godot

nova pasta -> addons

Convenção: colocar coisas de terceiros em uma pasta chamada addons

## Configurando Tilemaps e Tilesets

Node: TileMap

Time Map → Tile Set → New TileSet → salvar

Ao clicar duas vezes no arquivo tileset.tres abre uma nova aba no inferior chamado TileSet.

Na aba Tiles só arrastar o arquivo de imagem

Botão esquerdo com o lapis pode selecionar o tile e começar a pintar o mundo. Botão direito apaga.

## Adicionando colisão ao Tilemap

TileSet → Physics Layer

## Criando o mapa do jogo

É possível adicionar várias layers (terreno, BG, FG)

## Criando um personagem com física

CharacterBody2D já vem com código pronto

```gdscript
@export_range var lerp_factor = 0.2

lerp(velocidade_atual, velocidade_alvo, lerp_factor)
```

`@onready var sprite = $Sprite` ou arrastar segurando CTRL pro script

Botão direito no Node, `Acess as unique name`, pode chamar o node no script através de `%Sprite` independente da hierarquia

`@onready var sprite = %Sprite`

## Ordem de renderização

Z-index

## O céu é o limite

Node ParallaxBackground
|- ParallaxLayer
|    |_Sprite
|- ParallaxLayer
|    |_Sprite

