extends Node2D

@export var renegeration_amount: int = 10
@onready var area2d: Area2D = $ Area2D

func _ready() -> void:
	area2d.body_entered.connect(on_body_entered)

func on_body_entered(body: Node2D):
	if body.is_in_group("player"):
		var player: Player = body
		player.heal(renegeration_amount)
		player.meat_collected.emit(renegeration_amount)
		queue_free()
