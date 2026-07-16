class_name Player
extends CharacterBody2D

@export_category("Movement")
@export var speed: float = 3

@export_category("Sword")
@export var sword_damage: int = 2

@export_category("Ritual")
@export var ritual_damage:int = 1
@export var ritual_interval:float = 30
@export var ritual_scene:PackedScene

@export_category("Life")
@export var health: int = 100
@export var max_health: int = 100
@export var death_prefab: PackedScene

@onready var animation_player: AnimationPlayer = $ AnimationPlayer
@onready var sprite: Sprite2D = $ Sprite2D
@onready var sword_area: Area2D = $ SwordArea
@onready var hitbox_area: Area2D = $ HitBoxArea
@onready var health_progress_bar: ProgressBar = $ HealthProgressBar

var input_vector: Vector2 = Vector2(0,0)
var is_running: bool = false
var is_attacking: bool = false
var attack_cooldown: float = 0
var hitbox_cooldown: float = 0
var ritual_cooldown: float = 0

signal meat_collected(value:int)

func _ready() -> void:
	GameManager.player = self
	meat_collected.connect(func(valeu: int):
			GameManager.meat_counter += 1
			)

func _process(delta: float) -> void:
	GameManager.player_position = position
	read_inputs()
	
	play_run_idle_animation()
	if not is_attacking:
		rotate_sprite()
	
	# ataque
	update_attack_cooldown(delta)
	if Input.is_action_just_pressed("attack"):
		attack()
	
	# dano
	update_hitbox_detection(delta)
	
	# ritual
	update_ritual(delta)
	
	# atualizar health bar
	health_progress_bar.max_value = max_health
	health_progress_bar.value = health


func update_attack_cooldown(delta: float):
	attack_cooldown -= delta
	if attack_cooldown <= 0:
		is_attacking = false
		is_running = false
	

func play_run_idle_animation():
	# tocar animação
	if not is_attacking:
		if is_running:
			animation_player.play("run")
		else:
			animation_player.play("idle")

func rotate_sprite():
	# girar sprite
	if input_vector.x > 0:
		sprite.flip_h = false
	elif input_vector.x < 0:
		sprite.flip_h = true
	

func _physics_process(delta: float) -> void:	
	# modificar velocidade
	var target_velocity = input_vector * speed * 100.0
	if is_attacking:
		target_velocity *= 0.25
	velocity = lerp(velocity, target_velocity, 0.05)
	move_and_slide()

func update_ritual(delta):
	ritual_cooldown -= delta
	if ritual_cooldown > 0: return

	ritual_cooldown = ritual_interval
	
	var ritual = ritual_scene.instantiate()
	ritual.damage_amount = ritual_damage
	add_child(ritual)



func read_inputs():
	# obter o input_vector
	input_vector = Input.get_vector("move_left", "move_right", "move_up", "move_down")

	# apagar deadzone do input vector
	var deadzone = 0.15
	if abs(input_vector.x) < deadzone:
		input_vector.x = 0
	if abs(input_vector.y) < deadzone:
		input_vector.y = 0
	
	# atualizar is_running
	#was_running = is_running
	is_running = not input_vector.is_zero_approx()


func attack():
	if is_attacking:
		return
	
	animation_player.play("attack_side_1")
	
	is_attacking = true
	attack_cooldown = 0.6 # segundos


func deal_damage_to_enemies():
	var bodies = sword_area.get_overlapping_bodies()
	for body in bodies:
		if body.is_in_group("enemies"):
			var enemy:Enemy = body
			
			var direction_to_enemy = (enemy.position - position).normalized()
			var attack_diretion: Vector2
			if sprite.flip_h:
				attack_diretion = Vector2.LEFT
			else:
				attack_diretion = Vector2.RIGHT
			var dot_product = direction_to_enemy.dot(attack_diretion)
			if dot_product >= 0.3:
				enemy.damage(sword_damage)

func update_hitbox_detection(delta):
	# temporizador
	hitbox_cooldown -= delta
	if hitbox_cooldown > 0: return
	
	# frequencia
	hitbox_cooldown = 0.5
	
	# detectar inimigos
	var bodies = hitbox_area.get_overlapping_bodies()
	for body in bodies:
		if body.is_in_group("enemies"):
			var enemy: Enemy = body
			var damage_ammount = 1
			damage(damage_ammount)
			

func damage(amount:int):
	if health <= 0: return
	
	health -= amount
	print("Player recebeu ", amount, " de dano, total de vida: ", health)
	
	modulate = Color.RED
	var tween = create_tween()
	tween.set_ease(Tween.EASE_IN)
	tween.set_trans(Tween.TRANS_QUINT)
	tween.tween_property(self, "modulate", Color.WHITE, 0.3)
	
	if health <= 0:
		die()

func die():
	GameManager.end_game()
	if death_prefab:
		var death_object = death_prefab.instantiate()
		death_object.position = position
		get_parent().add_child(death_object)
	queue_free()

func heal(amount: int) -> int:
	health += amount
	if health > max_health:
		health = max_health
	print("HP: ", health, " / ", max_health)
	return health
