class_name GameOverUI
extends CanvasLayer

@onready var time_label: Label = %TimeLabel
@onready var mosnter_label: Label = %MonsterLabel

@export var restart_delay: float = 5.0
var restart_cooldown: float = 5.0 # s

func _ready() -> void:
	time_label.text = GameManager.time_elapsed_string
	mosnter_label.text = str(GameManager.monsters_defeated_counter)
	

func _process(delta: float) -> void:
	restart_cooldown -= delta
	if restart_cooldown > 0: return
	else: restart_game()


func restart_game():
	GameManager.reset()
	get_tree().reload_current_scene()
