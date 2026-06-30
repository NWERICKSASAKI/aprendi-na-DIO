# 4 Nossa Primeira Expirência em Godot

## Construindo um novo cenário

...

## Simulação física

...

## Materiais físicos

...

## Cenas e Nodes

...

## Detectando o clique do mouse

Convenção, cria um Node para colocar o script

```gdscript
extends Node

func _input(event: InputEvent) → void:
    if event is InputEventMouseButton:
        if event.button_index == 1:
            if event.pressed:
                print(event)
```

## Dando vida ao jogo

```gdscript
extends Node

var obj_template: PackedScene

func _ready() → void:
    obj_template = preload("res://objects/box_regular.tscn")

func _input(event: InputEvent) → void:
    if event is InputEventMouseButton:
        if event.button_index == 1:
            if event.pressed:
                spawn_object(event.position)

func spawn_object(position: Vector2) → void:
    pass
```

```gdscript
extends Node

@export var obj_template: Array[PacketScene]
# assim permite clicar e arrastar as cenas pro inspetor

func _input(event: InputEvent) → void:
    if event is InputEventMouseButton:
        if event.button_index == 1:
            if event.pressed:
                spawn_object(event.position)

func spawn_object(position: Vector2) → void:
    var index: int = randi_range(0,obj_templates.size()-1)
    var obj_template = obj_templates[index]
    var obj: RigidBody2D = obj_template.instatiate()
    obj.position = position
    add_child(obj)
```