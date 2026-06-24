
# 3 Primeiro contato com Godot

## Como instalar o Godot

...

## Uma visão do futuro

...

## Projetos de demonstração

...

## Entendendo a interface do editor

...

## Nosso primeiro script

...

## Movimentando nosso personagem

```gdscript
extends Sprite2D

@export var speed = 10

func _ready() → void:
    print("hello world")

func _process(delta: float) → void:
    var input = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    position += input * speed * delta
```

## Onde tudo começa

* whiteboxing
* grayboxing

## Nota sobre idioma do editor

...
