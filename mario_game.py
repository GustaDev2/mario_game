import pygame
import os
import random

# --- 1. Inicializa o Pygame ---
pygame.init()

# --- Inicializa o mixer de audio ---
pygame.mixer.init()

# --- 2. Configurações da Janela ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meu Jogo do Mario (Rascunho)")

# --- 3. Configurações do Jogo ---
clock = pygame.time.Clock()
FPS = 60

# --- 5. Estados do Jogo ---
GAME_STATE_TITLE = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2
GAME_STATE_LEVEL_TRANSITION = 3 # NOVO ESTADO: Transição de Fase

current_game_state = GAME_STATE_TITLE

# --- 6. Carregando Imagens (Sprites, Logo e Fundo) ---
# --- Sprites do Mario Grande ---
MARIO_PARADO_BIG_PATH = 'assets/mario_parado_1.png' # Assumindo que você tem essa imagem
MARIO_ANDANDO_BIG_PATHS = [
    'assets/mario_andando_1.png',
    'assets/mario_andando_2.png',
    'assets/mario_andando_3.png'
]
MARIO_PULANDO_BIG_PATH = 'assets/mario_pulando_3.png'

# --- Sprites do Mario Pequeno ---
MARIO_PARADO_SMALL_PATH = 'assets/small_mario_parado_1.png'
MARIO_ANDANDO_SMALL_PATHS = [
    'assets/small_mario_andando_1.png',
    'assets/small_mario_andando_2.png',
    'assets/small_mario_andando_3.png'
]
MARIO_PULANDO_SMALL_PATH = 'assets/small_mario_pulo.png'


GAME_LOGO_PATH = 'assets/mario_logo.png' # Assumindo que você tem essa imagem
BACKGROUND_IMAGE_PATH = 'assets/mario_background_1.png' # Assumindo que você tem essa imagem
GROUND_TILE_PATH = 'assets/chão.png' # Assumindo que você tem essa imagem

# --- IMAGEM DO CANO CLÁSSICO ---
PIPE_IMAGE_PATH = 'assets/pip.png' # <--- AGORA USANDO DIRETAMENTE 'pip.png'

# --- IMAGENS DA PLANTA CARNÍVORA (MANTIDAS) ---
PIRANHA_PLANT_PATHS = [
    'assets/piranha_plant_1.png',
    'assets/piranha_plant_2.png'
]
GOOMBA_PATHS = [
    'assets/goomba_1.png',
    'assets/goomba_2.png',
    'assets/goomba_3.png',
    'assets/goomba_4.png'
]
FLAG_IMAGE_PATH = 'assets/flag.png'

BLOCK_YELLOW_PATH = 'assets/block_yellow.png'
STAR_PATH = 'assets/star.png'
MUSHROOM_RED_PATH = 'assets/mushroom_red.png'

# --- Caminho para a música de fundo e som de perda ---
MARIO_THEME_MUSIC_PATH = 'assets/mario_theme.mp3'
GAME_OVER_SOUND_PATH = 'assets/game_over.mp3' # Caminho para o novo som de game over

# --- Variáveis para Sprites do Mario ---
mario_sprite_idle_big = None
mario_sprites_walk_big = []
mario_sprite_jump_big = None

mario_sprite_idle_small = None
mario_sprites_walk_small = []
mario_sprite_jump_small = None

game_logo_image = None
background_image = None
ground_tile_image = None
pipe_image = None # Será a nova imagem do cano clássico
piranha_plant_sprites = []
goomba_sprites = []
flag_image = None

block_yellow_image = None
star_image = None
mushroom_red_image = None

# Variável para o som de game over
game_over_sound = None

# --- CONSTANTES DE TAMANHO DOS SPRITES ---
TARGET_SPRITE_WIDTH_BIG = 32
TARGET_SPRITE_HEIGHT_BIG = 64
GOOMBA_WIDTH = 32
GOOMBA_HEIGHT = 32

# Aumentando um pouco o tamanho do Mario Pequeno
TARGET_SPRITE_WIDTH_SMALL = 40  # Aumentado de 32 para 40
TARGET_SPRITE_HEIGHT_SMALL = 40 # Aumentado de 32 para 40

PIPE_WIDTH = 64
PIPE_HEIGHT = 64 # Mantém a altura do cano para colisão
PIRANHA_PLANT_WIDTH = 32
PIRANHA_PLANT_HEIGHT = 48
FLAG_WIDTH = 48
FLAG_HEIGHT = 128
BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32
STAR_SIZE = 24
MUSHROOM_SIZE = 32

# Nova constante para a distância mínima entre blocos amarelos e canos
MIN_DISTANCE_BLOCK_PIPE = 80 # Distância mínima em pixels entre um bloco e um cano

# --- Verificações de existência dos arquivos ---
print(f"Verificando existência de {GAME_LOGO_PATH}: {os.path.exists(GAME_LOGO_PATH)}")
print(f"Verificando existência de {MARIO_PARADO_BIG_PATH}: {os.path.exists(MARIO_PARADO_BIG_PATH)}")
for i, path in enumerate(MARIO_ANDANDO_BIG_PATHS):
    print(f"Verificando existência de {path}: {os.path.exists(path)}")
print(f"Verificando existência de {MARIO_PULANDO_BIG_PATH}: {os.path.exists(MARIO_PULANDO_BIG_PATH)}")

print(f"Verificando existência de {MARIO_PARADO_SMALL_PATH}: {os.path.exists(MARIO_PARADO_SMALL_PATH)}")
for i, path in enumerate(MARIO_ANDANDO_SMALL_PATHS):
    print(f"Verificando existência de {path}: {os.path.exists(path)}")
print(f"Verificando existência de {MARIO_PULANDO_SMALL_PATH}: {os.path.exists(MARIO_PULANDO_SMALL_PATH)}")

print(f"Verificando existência de {PIPE_IMAGE_PATH}: {os.path.exists(PIPE_IMAGE_PATH)}") # Verifica nova imagem (pip.png)
# Correção aqui para verificar corretamente cada path da piranha plant
for i, path in enumerate(PIRANHA_PLANT_PATHS):
    print(f"Verificando existência de {path}: {os.path.exists(path)}")
for i, path in enumerate(GOOMBA_PATHS):
    print(f"Verificando existência de {path}: {os.path.exists(path)}")
print(f"Verificando existência de {FLAG_IMAGE_PATH}: {os.path.exists(FLAG_IMAGE_PATH)}")
print(f"Verificando existência de {BLOCK_YELLOW_PATH}: {os.path.exists(BLOCK_YELLOW_PATH)}")
print(f"Verificando existência de {STAR_PATH}: {os.path.exists(STAR_PATH)}")
print(f"Verificando existência de {MUSHROOM_RED_PATH}: {os.path.exists(MUSHROOM_RED_PATH)}")
print(f"Verificando existência de {MARIO_THEME_MUSIC_PATH}: {os.path.exists(MARIO_THEME_MUSIC_PATH)}")
print(f"Verificando existência de {GAME_OVER_SOUND_PATH}: {os.path.exists(GAME_OVER_SOUND_PATH)}")


try:
    # --- Carrega sprites do Mario Grande ---
    mario_sprite_idle_big = pygame.image.load(MARIO_PARADO_BIG_PATH).convert_alpha()
    mario_sprite_idle_big = pygame.transform.scale(mario_sprite_idle_big, (TARGET_SPRITE_WIDTH_BIG, TARGET_SPRITE_HEIGHT_BIG))

    for path in MARIO_ANDANDO_BIG_PATHS:
        frame = pygame.image.load(path).convert_alpha()
        frame = pygame.transform.scale(frame, (TARGET_SPRITE_WIDTH_BIG, TARGET_SPRITE_HEIGHT_BIG))
        mario_sprites_walk_big.append(frame)

    mario_sprite_jump_big = pygame.image.load(MARIO_PULANDO_BIG_PATH).convert_alpha()
    mario_sprite_jump_big = pygame.transform.scale(mario_sprite_jump_big, (TARGET_SPRITE_WIDTH_BIG, TARGET_SPRITE_HEIGHT_BIG))

    # --- Carrega sprites do Mario Pequeno (usando as novas imagens) ---
    mario_sprite_idle_small = pygame.image.load(MARIO_PARADO_SMALL_PATH).convert_alpha()
    # Escala do Mario Pequeno para o tamanho do Goomba
    mario_sprite_idle_small = pygame.transform.scale(mario_sprite_idle_small, (TARGET_SPRITE_WIDTH_SMALL, TARGET_SPRITE_HEIGHT_SMALL))

    for path in MARIO_ANDANDO_SMALL_PATHS:
        frame = pygame.image.load(path).convert_alpha()
        # Escala do Mario Pequeno para o tamanho do Goomba
        frame = pygame.transform.scale(frame, (TARGET_SPRITE_WIDTH_SMALL, TARGET_SPRITE_HEIGHT_SMALL))
        mario_sprites_walk_small.append(frame)

    mario_sprite_jump_small = pygame.image.load(MARIO_PULANDO_SMALL_PATH).convert_alpha()
    # Escala do Mario Pequeno para o tamanho do Goomba
    mario_sprite_jump_small = pygame.transform.scale(mario_sprite_jump_small, (TARGET_SPRITE_WIDTH_SMALL, TARGET_SPRITE_HEIGHT_SMALL))


    game_logo_image = pygame.image.load(GAME_LOGO_PATH).convert_alpha()
    game_logo_image = pygame.transform.scale(game_logo_image, (450, 225))
    print(f"Logo carregado com sucesso. Dimensões: {game_logo_image.get_size()}")

    background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert_alpha()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    ground_tile_image = pygame.image.load(GROUND_TILE_PATH).convert_alpha()
    GROUND_TILE_HEIGHT = 32
    ground_tile_image = pygame.transform.scale(ground_tile_image, (ground_tile_image.get_width(), GROUND_TILE_HEIGHT))

    # --- CARREGA A IMAGEM 'pip.png' PARA O CANO ---
    pipe_image = pygame.image.load(PIPE_IMAGE_PATH).convert_alpha()
    pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))

    # --- CARREGA AS IMAGENS DA PIRANHA PLANT (MANTIDAS) ---
    for path in PIRANHA_PLANT_PATHS:
        frame = pygame.image.load(path).convert_alpha()
        frame = pygame.transform.scale(frame, (PIRANHA_PLANT_WIDTH, PIRANHA_PLANT_HEIGHT))
        piranha_plant_sprites.append(frame)

    if GOOMBA_PATHS:
        for path in GOOMBA_PATHS:
            frame = pygame.image.load(path).convert_alpha()
            frame = pygame.transform.scale(frame, (GOOMBA_WIDTH, GOOMBA_HEIGHT))
            goomba_sprites.append(frame)
        print(f"Goombas carregados com {len(goomba_sprites)} frames.")
    else:
        print("AVISO: Nenhuma imagem de Goomba encontrada. Goombas não aparecerão.")

    flag_image = pygame.image.load(FLAG_IMAGE_PATH).convert_alpha()
    flag_image = pygame.transform.scale(flag_image, (FLAG_WIDTH, FLAG_HEIGHT))
    print(f"Bandeira carregada com sucesso. Dimensões: {flag_image.get_size()}")

    block_yellow_image = pygame.image.load(BLOCK_YELLOW_PATH).convert_alpha()
    block_yellow_image = pygame.transform.scale(block_yellow_image, (BLOCK_WIDTH, BLOCK_HEIGHT))
    star_image = pygame.image.load(STAR_PATH).convert_alpha()
    star_image = pygame.transform.scale(star_image, (STAR_SIZE, STAR_SIZE))

    mushroom_red_image = pygame.image.load(MUSHROOM_RED_PATH).convert_alpha()
    mushroom_red_image = pygame.transform.scale(mushroom_red_image, (MUSHROOM_SIZE, MUSHROOM_SIZE))
    print(f"Bloco amarelo, estrela e cogumelo carregados com sucesso.")

    # Carrega a música de fundo
    pygame.mixer.music.load(MARIO_THEME_MUSIC_PATH)
    pygame.mixer.music.set_volume(0.5) # Ajusta o volume (0.0 a 1.0)
    print(f"Música carregada com sucesso: {MARIO_THEME_MUSIC_PATH}")

    # Carrega o som de game over
    game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND_PATH)
    game_over_sound.set_volume(0.7) # Ajusta o volume do som de game over
    print(f"Som de game over carregado com sucesso: {GAME_OVER_SOUND_PATH}")

except pygame.error as e:
    print(f"ERRO CRÍTICO: Não foi possível carregar um dos recursos (imagem ou música/som): {e}")
    print(f"Verifique se todos os arquivos de sprite, o logo, o background, o tile de chão, os sprites dos desafios e a música/som existem nos caminhos corretos.")
    pygame.quit()
    exit()

# --- 7. Posição inicial do Mario e Câmera ---
GROUND_HEIGHT = GROUND_TILE_HEIGHT
# NOTA: mario_y_on_screen_initial e mario_y_on_screen precisarão ser ajustados dinamicamente
# com base no tamanho atual do Mario (big ou small)

# A posição inicial do Mario AGORA é calculada para que a BASE do sprite esteja no chão
mario_y_on_screen_initial_big = SCREEN_HEIGHT - TARGET_SPRITE_HEIGHT_BIG - GROUND_HEIGHT
mario_y_on_screen_initial_small = SCREEN_HEIGHT - TARGET_SPRITE_HEIGHT_SMALL - GROUND_HEIGHT

world_x_initial = 0
world_x = world_x_initial
camera_x_initial = 0
camera_x = camera_x_initial
WORLD_MAX_X = 10000

# --- 8. Variáveis para Animação e Movimento do Mario ---
mario_animation_index = 0.0
mario_animation_speed = 0.2
current_mario_image = None

mario_speed = 3
mario_current_direction = 0

mario_is_jumping = False
mario_vertical_speed = 0
GRAVITY = 0.5
JUMP_STRENGTH = -10
BOUNCE_STRENGTH = -5
mario_facing_right = True

# --- VARIÁVEIS PARA TAMANHO E VIDA DO MARIO ---
mario_is_big = False # Mario sempre começa pequeno
# mario_lives foi removido, pois a vida agora é condicional ao tamanho

# Invencibilidade temporária após colisão ou pegar item
mario_invincible_timer = 0
INVINCIBILITY_DURATION = 180 # 3 segundos de invencibilidade após dano
STAR_INVINCIBILITY_DURATION = 600 # NOVO: 10 segundos de invencibilidade após pegar estrela

# Variável para controlar o tempo de duração da tela de Game Over
game_over_timer = 0
GAME_OVER_DISPLAY_DURATION = 240 # 4 segundos a 60 FPS (considerando a duração da música)

# --- Configurações de Dificuldade/Fase ---
MAX_GAME_LEVEL = 5 # Nível máximo de fase (1 a 5)

BASE_GOOMBA_SPEED = 1
BASE_PIRANHA_PLANT_SPEED = 1
BASE_GOOMBA_SPAWN_DISTANCE_MIN = 200 # Distância mínima padrão entre Goombas
BASE_GOOMBA_SPAWN_DISTANCE_MAX = 500 # Distância máxima padrão entre Goombas

# Distâncias padrão para blocos de itens (NÃO SERÃO AFETADAS PELA DIFICULDADE)
BASE_BLOCK_SPAWN_DISTANCE_MIN = 300
BASE_BLOCK_SPAWN_DISTANCE_MAX = 800

current_game_level = 1 # Começa na Fase 1

# NOVO: Variáveis para o estado de transição de fase
level_transition_timer = 0
LEVEL_TRANSITION_DURATION = 90 # 1.5 segundos (90 frames a 60 FPS)

# Variável para controlar se a bandeira da fase atual já foi alcançada
# Isso impede múltiplas ativações de transição de fase se Mario ficar colidindo
# com a bandeira após o primeiro contato.
current_level_flag_reached = False


# --- 9. Fonte para texto ---
try:
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 24)
    # life_font não é mais necessário, pois vidas não serão exibidas
    game_over_font = pygame.font.Font(None, 72) # Fonte maior para "Game Over"
    level_font = pygame.font.Font(None, 64) # Nova fonte para o número da fase
except pygame.error as e:
    print(f"Erro ao carregar fonte: {e}. Usando fonte padrão.")
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 24)
    game_over_font = pygame.font.Font(None, 72)
    level_font = pygame.font.Font(None, 64)

# --- Sistema de Conquistas ---
achievements = {
    "first_move": {"name": "Primeiros Passos", "unlocked": False},
    "first_jump": {"name": "Pequeno Salto", "unlocked": False},
    "goomba_collided_1": {"name": "Vingança Goomba (1)", "unlocked": False, "target": 1},
    "goomba_collided_3": {"name": "Vingança Goomba (3)", "unlocked": False, "target": 3},
    "piranha_collided_1": {"name": "Jardineiro Destemido (1)", "unlocked": False, "target": 1},
    "flag_reached_1": {"name": "A Jornada Começa", "unlocked": False, "target": 1},
    "star_collector_1": {"name": "Caçador de Estrelas (1)", "unlocked": False, "target": 1},
    "star_collector_3": {"name": "Caçador de Estrelas (3)", "unlocked": False, "target": 3},
    "mario_shrunk_1": {"name": "Encogido!", "unlocked": False, "target": 1},
    "mario_grown_1": {"name": "Super Mario!", "unlocked": False, "target": 1},
    "goomba_stomped_1": {"name": "Esmagador de Goombas (1)", "unlocked": False, "target": 1},
    "goomba_stomped_5": {"name": "Esmagador de Goombas (5)", "unlocked": False, "target": 5}
}

# --- Contadores para as conquistas ---
goomba_collisions_count = 0
piranha_collisions_count = 0
flags_reached_count = 0
stars_collected_count = 0
mario_shrink_count = 0
mario_grow_count = 0
goomba_stomped_count = 0

# --- Variável para notificação de conquista ---
achievement_notification_text = ""
achievement_notification_timer = 0
NOTIFICATION_DURATION = 120

def unlock_achievement(achievement_id):
    global achievement_notification_text, achievement_notification_timer
    if not achievements[achievement_id]["unlocked"]:
        achievements[achievement_id]["unlocked"] = True
        print(f"CONQUISTA DESBLOQUEADA: {achievements[achievement_id]['name']}")
        achievement_notification_text = f"Conquista: {achievements[achievement_id]['name']}"
        achievement_notification_timer = NOTIFICATION_DURATION

# --- Classes de Desafios e Itens ---
class Pipe:
    def __init__(self, world_x):
        self.world_x = world_x
        # O rect do cano é para posicionamento e desenho, não necessariamente para colisão completa
        self.rect = pygame.Rect(self.world_x, SCREEN_HEIGHT - GROUND_HEIGHT - PIPE_HEIGHT, PIPE_WIDTH, PIPE_HEIGHT)
        
        # A "boca" do cano onde a planta aparece/desaparece
        self.pipe_top_y = SCREEN_HEIGHT - GROUND_HEIGHT - PIPE_HEIGHT
        
        self.piranha_plant = PiranhaPlant(
            self.world_x + (PIPE_WIDTH // 2) - (PIRANHA_PLANT_WIDTH // 2),
            self.pipe_top_y # A planta sai do topo do cano
        )

    def update(self):
        self.piranha_plant.update()

    def draw(self, screen, camera_x):
        screen.blit(pipe_image, (self.rect.x - camera_x, self.rect.y))
        self.piranha_plant.draw(screen, camera_x)

class PiranhaPlant:
    # Estados da planta
    STATE_HIDDEN = 0
    STATE_RISING = 1
    STATE_VISIBLE = 2
    STATE_SINKING = 3

    def __init__(self, world_x, pipe_top_y):
        self.world_x = world_x
        self.pipe_top_y = pipe_top_y # A coordenada Y do topo do cano
        self.actual_top_y = pipe_top_y - PIRANHA_PLANT_HEIGHT # Posição Y da planta quando totalmente visível
        self.hidden_y = pipe_top_y + (PIRANHA_PLANT_HEIGHT / 2) # Posição Y da planta quando totalmente escondida (ajuste para visual)

        self.height = PIRANHA_PLANT_HEIGHT
        self.width = PIRANHA_PLANT_WIDTH

        self.animation_index = 0.0
        self.animation_speed = 0.1
        self.sprites = piranha_plant_sprites

        self.move_speed = BASE_PIRANHA_PLANT_SPEED # Inicializado com a velocidade base
        
        self.current_y = self.hidden_y # Começa escondida
        self.state = PiranhaPlant.STATE_HIDDEN
        self.timer = random.randint(30, 90) # Tempo inicial aleatório antes de aparecer pela primeira vez

        self.rect = pygame.Rect(self.world_x, self.current_y, self.width, self.height)


    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            if self.state == PiranhaPlant.STATE_HIDDEN:
                self.state = PiranhaPlant.STATE_RISING
            elif self.state == PiranhaPlant.STATE_RISING:
                self.current_y -= self.move_speed
                if self.current_y <= self.actual_top_y:
                    self.current_y = self.actual_top_y
                    self.state = PiranhaPlant.STATE_VISIBLE
                    self.timer = random.randint(120, 180) # Tempo visível (2 a 3 segundos)
            elif self.state == PiranhaPlant.STATE_VISIBLE:
                self.state = PiranhaPlant.STATE_SINKING
            elif self.state == PiranhaPlant.STATE_SINKING:
                self.current_y += self.move_speed
                if self.current_y >= self.hidden_y:
                    self.current_y = self.hidden_y
                    self.state = PiranhaPlant.STATE_HIDDEN
                    self.timer = random.randint(120, 180) # Tempo escondida (2 a 3 segundos)

        self.rect.y = self.current_y

        # Animação apenas quando visível ou em transição
        if self.state in [PiranhaPlant.STATE_RISING, PiranhaPlant.STATE_VISIBLE, PiranhaPlant.STATE_SINKING]:
            self.animation_index += self.animation_speed
            if self.animation_index >= len(self.sprites):
                self.animation_index = 0
        else: # Quando totalmente escondida, zera a animação ou a mantém no primeiro frame
             self.animation_index = 0


    def draw(self, screen, camera_x):
        # A planta só será desenhada quando estiver no estado totalmente visível
        if self.sprites and self.state == PiranhaPlant.STATE_VISIBLE:
            screen.blit(self.sprites[int(self.animation_index)], (self.rect.x - camera_x, self.rect.y))


class Goomba:
    def __init__(self, world_x, initial_direction=-1):
        self.world_x = world_x
        self.initial_world_x = world_x
        self.speed = BASE_GOOMBA_SPEED # Inicializado com a velocidade base
        self.direction = initial_direction
        self.rect = pygame.Rect(self.world_x, SCREEN_HEIGHT - GROUND_HEIGHT - GOOMBA_HEIGHT, GOOMBA_WIDTH, GOOMBA_HEIGHT)

        self.animation_index = 0.0
        self.animation_speed = 0.15
        self.sprites = goomba_sprites

        self.walk_limit = 100
        self.is_dead = False
        self.death_timer = 0
        self.DEATH_DURATION = 30

    def update(self):
        if not self.is_dead:
            self.world_x += self.direction * self.speed
            self.rect.x = self.world_x

            if self.direction == -1 and self.world_x < self.initial_world_x - self.walk_limit:
                self.direction = 1
            elif self.direction == 1 and self.world_x > self.initial_world_x + self.walk_limit:
                self.direction = -1

            self.animation_index += self.animation_speed
            if self.sprites and self.animation_index >= len(self.sprites):
                self.animation_index = 0
        else:
            self.death_timer -= 1
            if self.death_timer <= 0:
                pass


    def draw(self, screen, camera_x):
        if not self.is_dead:
            if self.sprites:
                current_goomba_image = self.sprites[int(self.animation_index)]
                screen.blit(current_goomba_image, (self.rect.x - camera_x, self.rect.y))
        elif self.death_timer > 0:
            if self.sprites:
                # Desenha o goomba esmagado (apenas o primeiro frame achatado)
                dead_goomba_image = pygame.transform.scale(self.sprites[0], (GOOMBA_WIDTH, GOOMBA_HEIGHT // 2))
                screen.blit(dead_goomba_image, (self.rect.x - camera_x, self.rect.y + GOOMBA_HEIGHT // 2))


class GoalFlag:
    def __init__(self, world_x):
        self.world_x = world_x
        self.rect = pygame.Rect(self.world_x, SCREEN_HEIGHT - GROUND_HEIGHT - FLAG_HEIGHT, FLAG_WIDTH, FLAG_HEIGHT)

    def draw(self, screen, camera_x):
        screen.blit(flag_image, (self.rect.x - camera_x, self.rect.y))

class ItemBlock:
    def __init__(self, world_x, world_y, item_type="star"):
        self.world_x = world_x
        self.original_world_y = world_y
        self.rect = pygame.Rect(self.world_x, self.original_world_y, BLOCK_WIDTH, BLOCK_HEIGHT)
        self.has_item = True
        self.hit_animation_active = False
        self.hit_timer = 0
        self.HIT_DURATION = 10
        self.HIT_OFFSET = 5
        self.item_type = item_type

    def hit_by_mario(self):
        if self.has_item:
            self.has_item = False
            self.hit_animation_active = True
            self.hit_timer = self.HIT_DURATION
            self.rect.y = self.original_world_y + self.HIT_OFFSET
            return self.item_type
        return None

    def update(self):
        if self.hit_animation_active:
            self.hit_timer -= 1
            if self.hit_timer <= 0:
                self.hit_animation_active = False
                self.rect.y = self.original_world_y

    def draw(self, screen, camera_x):
        screen.blit(block_yellow_image, (self.rect.x - camera_x, self.rect.y))

class Star:
    def __init__(self, world_x, world_y):
        self.world_x = world_x
        self.world_y = world_y
        self.rect = pygame.Rect(self.world_x, self.world_y, STAR_SIZE, STAR_SIZE)
        self.vertical_speed = -5
        self.collected = False

    def update(self):
        self.world_y += self.vertical_speed
        self.vertical_speed += GRAVITY
        self.rect.y = self.world_y

        if self.world_y >= SCREEN_HEIGHT - GROUND_HEIGHT - STAR_SIZE:
            self.world_y = SCREEN_HEIGHT - GROUND_HEIGHT - STAR_SIZE
            self.vertical_speed = 0

    def draw(self, screen, camera_x):
        if not self.collected:
            screen.blit(star_image, (self.rect.x - camera_x, self.rect.y))

# CLASSE Mushroom
class Mushroom:
    def __init__(self, world_x, world_y):
        self.world_x = world_x
        self.world_y = world_y
        self.rect = pygame.Rect(self.world_x, self.world_y, MUSHROOM_SIZE, MUSHROOM_SIZE)
        self.vertical_speed = -5
        self.horizontal_speed = 1
        self.collected = False

    def update(self):
        self.world_y += self.vertical_speed
        self.vertical_speed += GRAVITY

        # Aplica gravidade até atingir o chão
        ground_level = SCREEN_HEIGHT - GROUND_HEIGHT - MUSHROOM_SIZE
        if self.world_y >= ground_level:
            self.world_y = ground_level
            self.vertical_speed = 0
            self.horizontal_speed = 1

        self.world_x += self.horizontal_speed

        self.rect.x = self.world_x
        self.rect.y = self.world_y

    def draw(self, screen, camera_x):
        if not self.collected:
            screen.blit(mushroom_red_image, (self.rect.x - camera_x, self.rect.y))


# --- Função para Resetar o Jogo ---
def reset_game():
    global world_x, camera_x, mario_y_on_screen, current_game_state
    global mario_animation_index, mario_current_direction, mario_is_jumping, mario_vertical_speed, mario_facing_right
    global goomba_collisions_count, piranha_collisions_count, flags_reached_count, stars_collected_count, mario_grow_count, goomba_stomped_count
    global item_blocks, active_stars, active_mushrooms, pipes, goombas, goal_flag, mario_is_big, mario_invincible_timer, mario_shrink_count
    global game_over_timer, current_game_level, current_level_flag_reached # Adiciona current_game_level

    print("Iniciando reset_game...")

    world_x = world_x_initial
    camera_x = camera_x_initial

    # Mario sempre começa pequeno (e sem vidas "extras" além do tamanho)
    mario_is_big = False
    mario_invincible_timer = 0

    # AJUSTE NO RESET: Garante que Mario pequeno comece na altura correta do chão
    mario_y_on_screen = SCREEN_HEIGHT - GROUND_HEIGHT - TARGET_SPRITE_HEIGHT_SMALL

    mario_animation_index = 0.0
    mario_current_direction = 0
    mario_is_jumping = False
    mario_vertical_speed = 0
    mario_facing_right = True

    goomba_collisions_count = 0
    piranha_collisions_count = 0
    goomba_stomped_count = 0
    flags_reached_count = 0 # Resetar as bandeiras também
    stars_collected_count = 0
    mario_shrink_count = 0
    mario_grow_count = 0

    current_game_level = 1 # Reseta a fase ao iniciar um novo jogo
    current_level_flag_reached = False # Garante que a bandeira pode ser alcançada na nova fase

    # Resetar e recriar os elementos do jogo
    pipes = []
    goombas = []
    item_blocks = []
    active_stars = []
    active_mushrooms = []
    goal_flag = None # Zera a bandeira existente para que populate_world crie uma nova


    # Popula o mundo novamente (com o tamanho aumentado)
    populate_world()

    # Para a música ao resetar o jogo para a tela de título
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    game_over_timer = 0 # Reseta o timer de game over

    current_game_state = GAME_STATE_TITLE
    print("Jogo resetado! Voltando para a tela de título.")


# --- Função para Popular o Mundo com Desafios e Itens ---
def populate_world():
    global pipes, goombas, item_blocks, active_stars, active_mushrooms, goal_flag, current_game_level

    print(f"Populando mundo para a Fase {current_game_level}...")

    # --- LIMPA TODOS OS OBJETOS EXISTENTES ANTES DE REPOPULAR ---
    pipes = []
    goombas = []
    item_blocks = []
    active_stars = []
    active_mushrooms = []
    goal_flag = None # Essencial para garantir que uma nova bandeira seja criada
    print("Listas de objetos limpas.")


    # Aumentar a velocidade dos Goombas e Plantas Carnívoras com base na fase
    # Fase 1: BASE_SPEED
    # Fase 2: BASE_SPEED + 0.2
    # Fase 5: BASE_SPEED + 0.8
    effective_goomba_speed = BASE_GOOMBA_SPEED + ((current_game_level - 1) * 0.2)
    effective_piranha_plant_speed = BASE_PIRANHA_PLANT_SPEED + ((current_game_level - 1) * 0.1)

    # Reduzir a distância entre Goombas e Blocos para aumentar a densidade
    # Garante que a distância mínima nunca seja menor que um valor razoável
    min_goomba_distance = max(50, BASE_GOOMBA_SPAWN_DISTANCE_MIN - ((current_game_level - 1) * 20))
    max_goomba_distance = max(150, BASE_GOOMBA_SPAWN_DISTANCE_MAX - ((current_game_level - 1) * 40))

    min_pipe_distance = 300 - ((current_game_level - 1) * 30) # Reduz o espaçamento entre canos
    max_pipe_distance = 700 - ((current_game_level - 1) * 70)
    min_pipe_distance = max(200, min_pipe_distance) # Garante um mínimo
    max_pipe_distance = max(400, max_pipe_distance) # Garante um mínimo

    # --- Manter a distância dos blocos constante, SEMPRE USANDO AS BASES ---
    min_block_distance = BASE_BLOCK_SPAWN_DISTANCE_MIN
    max_block_distance = BASE_BLOCK_SPAWN_DISTANCE_MAX


    # Posicionamento de Canos (espalhados pelo mundo de 10000 unidades)
    num_pipes_to_add = 15 + (current_game_level - 1) * 2 # Mais canos em níveis mais altos
    current_x = 400 # Começa a gerar canos a partir de uma distância segura
    for i in range(num_pipes_to_add):
        x_pos = current_x + random.randint(min_pipe_distance, max_pipe_distance)
        # Garante que o cano não vá além do limite do mundo
        if x_pos < WORLD_MAX_X - PIPE_WIDTH - 200:
            new_pipe = Pipe(world_x=x_pos)
            new_pipe.piranha_plant.move_speed = effective_piranha_plant_speed # Define a velocidade da planta
            pipes.append(new_pipe)
            current_x = x_pos
        else:
            break # Não adicionar mais canos se estiver muito perto do fim do mundo
    print(f"Adicionados {len(pipes)} canos.")


    # Posicionamento de Goombas (espalhados pelo mundo)
    if goomba_sprites:
        num_goombas_to_add = 20 + (current_game_level - 1) * 5 # Mais Goombas em níveis mais altos
        current_x = 200 # Começa a gerar Goombas a partir de uma distância segura
        for i in range(num_goombas_to_add):
            x_pos = current_x + random.randint(min_goomba_distance, max_goomba_distance)
            if x_pos < WORLD_MAX_X - GOOMBA_WIDTH - 200:
                new_goomba = Goomba(world_x=x_pos, initial_direction=random.choice([-1, 1]))
                new_goomba.initial_world_x = x_pos
                new_goomba.speed = effective_goomba_speed # Define a velocidade do Goomba
                goombas.append(new_goomba)
                current_x = x_pos
            else:
                break
        print(f"Adicionados {len(goombas)} Goombas.")
    else:
        print("Goombas não serão adicionados ao mapa, pois os sprites não foram carregados.")

    # Posicionamento de Blocos de Itens (espalhados)
    num_blocks_to_add = 15 + (current_game_level - 1) * 3 # Mais blocos em níveis mais altos
    current_x = 400 # Começa a gerar blocos a partir de uma distância segura

    for i in range(num_blocks_to_add):
        x_pos = current_x + random.randint(min_block_distance, max_block_distance)
        
        if x_pos >= WORLD_MAX_X - BLOCK_WIDTH - 200: # Evita ir muito longe no mundo
            break
        
        y_pos = random.choice([
            SCREEN_HEIGHT - GROUND_HEIGHT - 96,
            SCREEN_HEIGHT - GROUND_HEIGHT - 128,
            SCREEN_HEIGHT - GROUND_HEIGHT - 160
        ])

        # Verificar se a nova posição X do bloco está muito perto de um cano existente
        is_too_close_to_pipe = False
        for existing_pipe in pipes:
            # Amplia a área de exclusão ao redor do cano
            if (x_pos < existing_pipe.world_x + PIPE_WIDTH + MIN_DISTANCE_BLOCK_PIPE and
                x_pos + BLOCK_WIDTH > existing_pipe.world_x - MIN_DISTANCE_BLOCK_PIPE):
                is_too_close_to_pipe = True
                break

        # Se não está muito perto de nenhum cano, adiciona o bloco
        if not is_too_close_to_pipe:
            # --- MODIFICAÇÃO AQUI: Estrela 1/5 de chance, Cogumelo 4/5 de chance ---
            item_type = random.choice(["star"] + ["mushroom"] * 4) # Estrela 1/5, Cogumelo 4/5
            item_blocks.append(ItemBlock(world_x=x_pos, world_y=y_pos, item_type=item_type))
            current_x = x_pos
        else:
            # Se colidir, tenta um pouco mais adiante, sem contar como bloco adicionado
            # (isso é uma simplificação, para um jogo maior, uma regeneração de posição seria melhor)
            current_x = x_pos + BLOCK_WIDTH + MIN_DISTANCE_BLOCK_PIPE # Tenta pular o cano

    print(f"Adicionados {len(item_blocks)} blocos de itens.")


    # Garante que a bandeira de chegada esteja sempre no final do mundo
    GOAL_FLAG_X = WORLD_MAX_X - 100
    if flag_image:
        goal_flag = GoalFlag(world_x=GOAL_FLAG_X)
        print(f"Bandeira de chegada criada em world_x = {GOAL_FLAG_X}")
    else:
        print("Bandeira de chegada não será criada, pois a imagem não foi carregada.")

    print("Mundo populado com sucesso!")


# --- Instâncias dos Desafios e Itens (Chamando a função para popular o mundo) ---
pipes = []
goombas = []
goal_flag = None
item_blocks = []
active_stars = []
active_mushrooms = []

populate_world()

# Define o tamanho inicial do Mario e sua posição Y
mario_y_on_screen = SCREEN_HEIGHT - GROUND_HEIGHT - TARGET_SPRITE_HEIGHT_SMALL


# --- Variável para rastrear o estado anterior para controlar a música ---
previous_game_state = current_game_state

# --- 10. Loop Principal do Jogo ---
running = True
while running:
    # --- Lógica para tocar/parar a música baseada no estado do jogo ---
    if current_game_state == GAME_STATE_PLAYING and previous_game_state != GAME_STATE_PLAYING:
        # Se entrar no estado PLAYING e não estava antes, começa a música
        pygame.mixer.music.play(-1)
        print("Música do jogo iniciada.")
    elif current_game_state == GAME_STATE_TITLE and previous_game_state != GAME_STATE_TITLE:
        # Se entrar no estado TITLE e não estava antes, para a música
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        print("Música do jogo parada.")
    elif current_game_state == GAME_STATE_GAME_OVER and previous_game_state != GAME_STATE_GAME_OVER:
        # Se entrar no estado GAME_OVER e não estava antes, para música e toca game over
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        if game_over_sound:
            game_over_sound.play()
        game_over_timer = GAME_OVER_DISPLAY_DURATION # Inicia o timer para a tela de game over
    elif current_game_state == GAME_STATE_LEVEL_TRANSITION and previous_game_state != GAME_STATE_LEVEL_TRANSITION:
        # Se entrar no estado de transição, para a música do jogo
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        print(f"Iniciando transição para Fase {current_game_level}...")
        # REPOPULA O MUNDO AQUI, NO INÍCIO DA TRANSIÇÃO, ANTES DE VOLTAR AO PLAYING
        populate_world() # Prepara a nova fase
        world_x = world_x_initial
        camera_x = camera_x_initial
        # Ajusta a posição Y do Mario para o tamanho correto (do Mario que ele era)
        mario_y_on_screen = SCREEN_HEIGHT - GROUND_HEIGHT - (TARGET_SPRITE_HEIGHT_BIG if mario_is_big else TARGET_SPRITE_HEIGHT_SMALL)
        current_level_flag_reached = False # Reseta para a próxima fase

    previous_game_state = current_game_state

    # --- Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_ESCAPE: # Adiciona ESC para sair rapidamente
            running = False

        if event.type == pygame.KEYDOWN:
            if current_game_state == GAME_STATE_TITLE:
                if event.key == pygame.K_SPACE:
                    current_game_state = GAME_STATE_PLAYING
            elif current_game_state == GAME_STATE_PLAYING:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and not achievements["first_move"]["unlocked"]:
                    unlock_achievement("first_move")

                if event.key == pygame.K_LEFT:
                    mario_current_direction = -1
                    mario_facing_right = False
                elif event.key == pygame.K_RIGHT:
                    mario_current_direction = 1
                    mario_facing_right = True
                elif event.key == pygame.K_SPACE and not mario_is_jumping:
                    mario_vertical_speed = JUMP_STRENGTH
                    mario_is_jumping = True
                    if not achievements["first_jump"]["unlocked"]:
                        unlock_achievement("first_jump")
            elif current_game_state == GAME_STATE_GAME_OVER:
                # SOMENTE PERMITE CLICAR EM ESPAÇO APÓS O game_over_timer ZERAR
                if event.key == pygame.K_SPACE and game_over_timer <= 0:
                    reset_game()


        if event.type == pygame.KEYUP:
            if current_game_state == GAME_STATE_PLAYING:
                if event.key == pygame.K_LEFT and mario_current_direction == -1:
                    mario_current_direction = 0
                    mario_animation_index = 0
                elif event.key == pygame.K_RIGHT and mario_current_direction == 1:
                    mario_current_direction = 0
                    mario_animation_index = 0

    # --- 11. Lógica do Jogo Principal (apenas se GAME_STATE_PLAYING) ---
    if current_game_state == GAME_STATE_PLAYING:
        # --- Lógica de Invencibilidade ---
        if mario_invincible_timer > 0:
            mario_invincible_timer -= 1

        # Guarda a posição anterior do Mario para detectar colisões
        old_mario_rect = pygame.Rect(world_x, mario_y_on_screen,
                                     (TARGET_SPRITE_WIDTH_BIG if mario_is_big else TARGET_SPRITE_WIDTH_SMALL),
                                     (TARGET_SPRITE_HEIGHT_BIG if mario_is_big else TARGET_SPRITE_HEIGHT_SMALL))

        # Movimento horizontal
        world_x += mario_current_direction * mario_speed

        # Restringe o movimento horizontal do Mario dentro do mundo
        if world_x < 0:
            world_x = 0
        elif world_x > WORLD_MAX_X - (TARGET_SPRITE_WIDTH_BIG if mario_is_big else TARGET_SPRITE_WIDTH_SMALL):
            world_x = WORLD_MAX_X - (TARGET_SPRITE_WIDTH_BIG if mario_is_big else TARGET_SPRITE_HEIGHT_SML)

        target_camera_x = world_x - (SCREEN_WIDTH // 4)

        if target_camera_x < 0:
            camera_x = 0
        elif target_camera_x > WORLD_MAX_X - SCREEN_WIDTH:
            camera_x = WORLD_MAX_X - SCREEN_WIDTH
        else:
            camera_x = target_camera_x

        # Movimento vertical (gravidade e pulo)
        mario_vertical_speed += GRAVITY
        mario_y_on_screen += mario_vertical_speed

        # --- A altura e largura do Mario para colisão ---
        current_mario_width = TARGET_SPRITE_WIDTH_BIG if mario_is_big else TARGET_SPRITE_WIDTH_SMALL
        current_mario_height = TARGET_SPRITE_HEIGHT_BIG if mario_is_big else TARGET_SPRITE_HEIGHT_SMALL

        # Cria o rect do Mario com a posição atual e o tamanho correto
        mario_rect = pygame.Rect(world_x, mario_y_on_screen, current_mario_width, current_mario_height)

        # --- Colisão com o chão ---
        ground_level = SCREEN_HEIGHT - GROUND_HEIGHT - current_mario_height
        if mario_y_on_screen >= ground_level:
            mario_y_on_screen = ground_level
            mario_is_jumping = False
            mario_vertical_speed = 0

        # --- Atualiza animação do Mario ---
        if mario_is_big:
            if mario_is_jumping:
                current_mario_image = mario_sprite_jump_big
            elif mario_current_direction != 0:
                mario_animation_index += mario_animation_speed
                if mario_animation_index >= len(mario_sprites_walk_big):
                    mario_animation_index = 0
                current_mario_image = mario_sprites_walk_big[int(mario_animation_index)]
            else:
                current_mario_image = mario_sprite_idle_big
        else: # Mario Pequeno
            if mario_is_jumping:
                current_mario_image = mario_sprite_jump_small
            elif mario_current_direction != 0:
                mario_animation_index += mario_animation_speed
                if mario_animation_index >= len(mario_sprites_walk_small):
                    mario_animation_index = 0
                current_mario_image = mario_sprites_walk_small[int(mario_animation_index)]
            else:
                current_mario_image = mario_sprite_idle_small


        if not mario_facing_right:
            current_mario_image = pygame.transform.flip(current_mario_image, True, False)

        # --- Lógica de piscar invencibilidade ---
        if mario_invincible_timer > 0:
            # Faz o Mario piscar (aparece/desaparece)
            if (mario_invincible_timer // 6) % 2 == 0:
                current_mario_image.set_alpha(255)
            else:
                current_mario_image.set_alpha(0)
        else:
            current_mario_image.set_alpha(255)

        # --- Atualiza inimigos e itens ---
        for pipe in pipes:
            pipe.update()

        # Filtra Goombas mortos que já "sumiram"
        goombas_to_keep = []
        for goomba in goombas:
            goomba.update()
            if not goomba.is_dead or goomba.death_timer > 0:
                goombas_to_keep.append(goomba)
        goombas = goombas_to_keep

        for block in item_blocks:
            block.update()
        for star in active_stars:
            star.update()
        for mushroom in active_mushrooms:
            mushroom.update()

        active_stars = [star for star in active_stars if not star.collected and star.world_y < SCREEN_HEIGHT]
        active_mushrooms = [mushroom for mushroom in active_mushrooms if not mushroom.collected and mushroom.world_y < SCREEN_HEIGHT]


        # --- Lógica de Colisão ---

        # Colisão Mario com Canos
        for pipe in pipes:
            # Cria um rect para o cano para colisões
            pipe_rect = pygame.Rect(pipe.world_x, pipe.rect.y, PIPE_WIDTH, PIPE_HEIGHT)

            # Colisão com a Planta Carnívora (perigo)
            # A planta só pode colidir quando estiver TOTALMENTE VISÍVEL (STATE_VISIBLE)
            # E Mario só leva dano se NÃO estiver invencível
            if pipe.piranha_plant.state == PiranhaPlant.STATE_VISIBLE:
                plant_world_rect = pygame.Rect(pipe.piranha_plant.rect.x, pipe.piranha_plant.rect.y, PIRANHA_PLANT_WIDTH, PIRANHA_PLANT_HEIGHT)
                if mario_rect.colliderect(plant_world_rect):
                    if mario_invincible_timer == 0: # Mario não está invencível
                        print(f"Mario colidiu com a Planta Carnívora em {pipe.world_x}!")
                        piranha_collisions_count += 1
                        if piranha_collisions_count >= achievements["piranha_collided_1"]["target"]:
                            unlock_achievement("piranha_collided_1")

                        if mario_is_big:
                            mario_is_big = False
                            mario_shrink_count += 1
                            unlock_achievement("mario_shrunk_1")
                            mario_invincible_timer = INVINCIBILITY_DURATION # Invencibilidade após encolher
                            # AJUSTE NA REDUÇÃO: Mantém a base do Mario no chão
                            mario_y_on_screen = SCREEN_HEIGHT - GROUND_HEIGHT - TARGET_SPRITE_HEIGHT_SMALL
                            print("Mario encolheu!")
                        else:
                            # Mario está pequeno e leva dano: Game Over imediato
                            current_game_state = GAME_STATE_GAME_OVER
                            print("Mario pequeno levou dano! Game Over!")
                    # Adicionado para evitar que o Mario leve vários hits da mesma planta/goomba
                    # na mesma frame, se a colisão ainda estiver ativa
                    #break # Remover este break se Mario puder colidir com outros inimigos na mesma frame

            # Colisão com o Cano (obstáculo sólido)
            if mario_rect.colliderect(pipe_rect):
                # Se o Mario estava acima e agora está colidindo (caindo no cano)
                if old_mario_rect.bottom <= pipe_rect.top and mario_rect.bottom > pipe_rect.top:
                    mario_y_on_screen = pipe_rect.top - current_mario_height
                    mario_vertical_speed = 0
                    mario_is_jumping = False
                # Se o Mario estava abaixo e agora está colidindo (pulando e batendo a cabeça no cano)
                elif old_mario_rect.top >= pipe_rect.bottom and mario_rect.top < pipe_rect.bottom:
                    mario_y_on_screen = pipe_rect.bottom
                    mario_vertical_speed = 0 # Para a subida imediatamente
                # Colisão lateral (Mario tentando atravessar o cano horizontalmente)
                elif mario_rect.left < pipe_rect.right and mario_rect.right > pipe_rect.left:
                    # Se veio da esquerda para a direita
                    if old_mario_rect.right <= pipe_rect.left:
                        world_x = pipe_rect.left - current_mario_width
                        mario_current_direction = 0 # Para o movimento horizontal
                    # Se veio da direita para a esquerda
                    elif old_mario_rect.left >= pipe_rect.right:
                        world_x = pipe_rect.right
                        mario_current_direction = 0 # Para o movimento horizontal

                    # Atualiza o mario_rect após ajustar a posição para refletir a colisão
                    mario_rect = pygame.Rect(world_x, mario_y_on_screen, current_mario_width, current_mario_height)


        # Colisão Mario com Goombas
        for goomba in goombas:
            if not goomba.is_dead:
                if mario_rect.colliderect(goomba.rect):
                    # Detecção de colisão por cima (esmagar Goomba)
                    if mario_vertical_speed > 0 and \
                       mario_rect.bottom >= goomba.rect.top and \
                       mario_rect.top < goomba.rect.top:

                        goomba.is_dead = True
                        goomba.death_timer = goomba.DEATH_DURATION
                        goomba_stomped_count += 1
                        print(f"Mario esmagou um Goomba! Total esmagado: {goomba_stomped_count}")
                        if goomba_stomped_count >= achievements["goomba_stomped_1"]["target"]:
                            unlock_achievement("goomba_stomped_1")
                        if goomba_stomped_count >= achievements["goomba_stomped_5"]["target"]:
                            unlock_achievement("goomba_stomped_5")

                        mario_vertical_speed = BOUNCE_STRENGTH
                        mario_is_jumping = True

                    elif mario_invincible_timer == 0: # Mario não está invencível
                        print(f"Mario colidiu com um Goomba em {goomba.world_x}!")
                        goomba_collisions_count += 1
                        if goomba_collisions_count >= achievements["goomba_collided_1"]["target"]:
                            unlock_achievement("goomba_collided_1")
                        if goomba_collisions_count >= achievements["goomba_collided_3"]["target"]:
                            unlock_achievement("goomba_collided_3")

                        if mario_is_big:
                            mario_is_big = False
                            mario_shrink_count += 1
                            unlock_achievement("mario_shrunk_1")
                            mario_invincible_timer = INVINCIBILITY_DURATION # Invencibilidade após encolher
                            # AJUSTE NA REDUÇÃO: Mantém a base do Mario no chão
                            mario_y_on_screen = SCREEN_HEIGHT - GROUND_HEIGHT - TARGET_SPRITE_HEIGHT_SMALL
                            print("Mario encolheu!")
                        else:
                            # Mario está pequeno e leva dano: Game Over imediato
                            current_game_state = GAME_STATE_GAME_OVER
                            print("Mario pequeno levou dano! Game Over!")
                        # Adicionado para evitar que o Mario leve vários hits da mesma planta/goomba
                        # na mesma frame, se a colisão ainda estiver ativa
                        break

        # Colisão Mario com Bandeira de Chegada
        if goal_flag and mario_rect.colliderect(goal_flag.rect) and not current_level_flag_reached:
            print(f"Mario colidiu com a bandeira da Fase {current_game_level}!")
            current_level_flag_reached = True # Marca que a bandeira desta fase foi alcançada
            
            if current_game_level < MAX_GAME_LEVEL:
                print(f"Parabéns! Mario alcançou a bandeira de chegada na Fase {current_game_level}! Avançando...")
                flags_reached_count += 1
                if flags_reached_count >= achievements["flag_reached_1"]["target"]:
                    unlock_achievement("flag_reached_1")
                
                # Avança para a próxima fase
                current_game_level += 1 
                
                # Entra no estado de transição de fase
                current_game_state = GAME_STATE_LEVEL_TRANSITION
                level_transition_timer = LEVEL_TRANSITION_DURATION
                
            elif current_game_level == MAX_GAME_LEVEL:
                print("Parabéns! Você completou todas as fases!")
                reset_game() # Reinicia completamente o jogo e volta para a tela de título
                # O estado de jogo já será GAME_STATE_TITLE dentro de reset_game()

        # --- Colisão Mario com Item Blocks ---
        for block in item_blocks:
            # Cria um rect para o bloco para colisões
            block_world_rect = pygame.Rect(block.world_x, block.rect.y, BLOCK_WIDTH, BLOCK_HEIGHT)

            # Colisão por cima (Mario caindo no bloco)
            # Apenas se o Mario estava acima e agora está colidindo
            if mario_vertical_speed > 0 and mario_rect.colliderect(block_world_rect):
                if old_mario_rect.bottom <= block_world_rect.top: # Mario estava acima do bloco
                    mario_y_on_screen = block_world_rect.top - current_mario_height # Ajusta o Mario para cima do bloco
                    mario_vertical_speed = 0
                    mario_is_jumping = False # Mario está no chão (do bloco)

            # Colisão por baixo (Mario pulando no bloco)
            # Apenas se o Mario estava abaixo e agora está colidindo
            if mario_vertical_speed < 0 and mario_rect.colliderect(block_world_rect):
                if old_mario_rect.top >= block_world_rect.bottom: # Mario estava abaixo do bloco
                    item_type = block.hit_by_mario()
                    if item_type == "star":
                        new_star = Star(block.world_x + (BLOCK_WIDTH - STAR_SIZE) // 2, block.original_world_y - STAR_SIZE)
                        active_stars.append(new_star)
                    elif item_type == "mushroom":
                        new_mushroom = Mushroom(block.world_x + (BLOCK_WIDTH - MUSHROOM_SIZE) // 2, block.original_world_y - MUSHROOM_SIZE)
                        active_mushrooms.append(new_mushroom)

                    mario_y_on_screen = block_world_rect.bottom # Ajusta o Mario para baixo do bloco
                    mario_vertical_speed = abs(mario_vertical_speed) * 0.5 # Inverte a velocidade e reduz um pouco para simular a batida (ajustável)

            # Colisão lateral (Mario tentando atravessar o bloco horizontalmente)
            # Verifica se houve colisão lateral e ajusta a posição
            # Cuidado para não conflitar com colisões verticais já tratadas
            if mario_rect.colliderect(block_world_rect):
                # Se não foi uma colisão de cima ou de baixo já tratada
                # (e se o Mario não está no processo de passar verticalmente pelo bloco)
                if not (old_mario_rect.bottom <= block_world_rect.top or old_mario_rect.top >= block_world_rect.bottom):
                    # Se veio da esquerda para a direita
                    if old_mario_rect.right <= block_world_rect.left:
                        world_x = block_world_rect.left - current_mario_width
                        mario_current_direction = 0 # Para o movimento horizontal
                    # Se veio da direita para a esquerda
                    elif old_mario_rect.left >= block_world_rect.right:
                        world_x = block_world_rect.right
                        mario_current_direction = 0 # Para o movimento horizontal

                    # Atualiza o mario_rect após ajustar a posição para refletir a colisão
                    mario_rect = pygame.Rect(world_x, mario_y_on_screen, current_mario_width, current_mario_height)


        # --- Colisão Mario com Estrelas ---
        for star in active_stars:
            if not star.collected and mario_rect.colliderect(star.rect):
                star.collected = True
                stars_collected_count += 1
                print(f"Estrela coletada! Total: {stars_collected_count}")
                # NOVO: Mario ganha invencibilidade ao pegar a estrela
                mario_invincible_timer = STAR_INVINCIBILITY_DURATION
                print(f"Mario ficou invencível por {STAR_INVINCIBILITY_DURATION/FPS} segundos!")

                if stars_collected_count >= achievements["star_collector_1"]["target"]:
                    unlock_achievement("star_collector_1")
                if stars_collected_count >= achievements["star_collector_3"]["target"]:
                    unlock_achievement("star_collector_3")

        # --- Colisão Mario com Cogumelos ---
        for mushroom in active_mushrooms:
            if not mushroom.collected and mario_rect.colliderect(mushroom.rect):
                mushroom.collected = True
                print(f"Cogumelo coletado!")
                if not mario_is_big:
                    mario_is_big = True
                    mario_grow_count += 1
                    unlock_achievement("mario_grown_1")
                    mario_invincible_timer = INVINCIBILITY_DURATION # Invencibilidade breve ao crescer
                    # AJUSTE NO CRESCIMENTO: Mantém a base do Mario no chão
                    mario_y_on_screen = SCREEN_HEIGHT - GROUND_HEIGHT - TARGET_SPRITE_HEIGHT_BIG



        # --- Lógica da notificação de conquista ---
        if achievement_notification_timer > 0:
            achievement_notification_timer -= 1
            if achievement_notification_timer == 0:
                achievement_notification_text = ""

    # --- Lógica para o estado GAME_OVER ---
    elif current_game_state == GAME_STATE_GAME_OVER:
        game_over_timer -= 1
        if game_over_timer <= 0:
            # Mantém a mensagem de "Pressione ESPAÇO" visível
            pass # Não reseta o jogo aqui, apenas permite o input agora

    # --- Lógica para o estado LEVEL_TRANSITION ---
    elif current_game_state == GAME_STATE_LEVEL_TRANSITION:
        level_transition_timer -= 1
        if level_transition_timer <= 0:
            print("Fim da transição de fase. Voltando para o estado PLAYING.")
            current_game_state = GAME_STATE_PLAYING
            # A música será iniciada automaticamente pelo controle de estado no início do loop


    # --- 12. Desenho Baseado no Estado Atual ---
    if current_game_state == GAME_STATE_TITLE:
        screen.fill((0, 0, 0))

        if game_logo_image:
            logo_x = (SCREEN_WIDTH - game_logo_image.get_width()) // 2
            logo_y = (SCREEN_HEIGHT - game_logo_image.get_height()) // 2 - 100
            screen.blit(game_logo_image, (logo_x, logo_y))
        else:
            print("AVISO: game_logo_image é None. Não foi possível desenhar o logo.")

        text_surface = font.render("Pressione ESPAÇO para Iniciar", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(text_surface, text_rect)

        y_offset = SCREEN_HEIGHT // 2 + 100
        for ach_id, ach_info in achievements.items():
            status = "Desbloqueada" if ach_info["unlocked"] else "Bloqueada"
            ach_text = f"{ach_info['name']}: {status}"
            if "target" in ach_info:
                if ach_id.startswith("goomba_collided"):
                    ach_text += f" ({goomba_collisions_count}/{ach_info['target']})"
                elif ach_id.startswith("piranha"):
                    ach_text += f" ({piranha_collisions_count}/{ach_info['target']})"
                elif ach_id.startswith("flag"):
                    ach_text += f" ({flags_reached_count}/{ach_info['target']})"
                elif ach_id.startswith("star"):
                    ach_text += f" ({stars_collected_count}/{ach_info['target']})"
                elif ach_id.startswith("mario_shrunk"):
                    ach_text += f" ({mario_shrink_count}/{ach_info['target']})"
                elif ach_id.startswith("mario_grown"):
                    ach_text += f" ({mario_grow_count}/{ach_info['target']})"
                elif ach_id.startswith("goomba_stomped"):
                    ach_text += f" ({goomba_stomped_count}/{ach_info['target']})"


            ach_surface = small_font.render(ach_text, True, (200, 200, 200))
            ach_rect = ach_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            screen.blit(ach_surface, ach_rect)
            y_offset += 30

    elif current_game_state == GAME_STATE_PLAYING:
        screen.blit(background_image, (0, 0))

        first_tile_x_on_screen = -(camera_x % ground_tile_image.get_width())

        for x_offset in range(first_tile_x_on_screen, SCREEN_WIDTH + ground_tile_image.get_width(), ground_tile_image.get_width()):
            screen.blit(ground_tile_image, (x_offset, SCREEN_HEIGHT - GROUND_HEIGHT))

        for pipe in pipes:
            pipe.draw(screen, camera_x)
        for goomba in goombas:
            goomba.draw(screen, camera_x)
        for block in item_blocks:
            block.draw(screen, camera_x)
        for star in active_stars:
            star.draw(screen, camera_x)
        for mushroom in active_mushrooms:
            mushroom.draw(screen, camera_x)

        if goal_flag:
            goal_flag.draw(screen, camera_x)

        mario_draw_x_on_screen = world_x - camera_x
        screen.blit(current_mario_image, (mario_draw_x_on_screen, mario_y_on_screen))

        # O contador de vidas foi removido, pois a vida agora é baseada no tamanho do Mario
        # lives_text = life_font.render(f"Vidas: {mario_lives}", True, (255, 255, 255))
        # screen.blit(lives_text, (10, 10))

        # Adiciona um contador de distância ou progresso
        progress_text = small_font.render(f"Progresso: {int(world_x)} / {WORLD_MAX_X}", True, (255, 255, 255))
        screen.blit(progress_text, (SCREEN_WIDTH - progress_text.get_width() - 10, 10))

        # Desenha o nível de fase atual
        level_text = level_font.render(f"Fase: {current_game_level}", True, (255, 255, 0))
        screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 10))


        if achievement_notification_timer > 0 and achievement_notification_text:
            notif_surface = small_font.render(achievement_notification_text, True, (255, 255, 0))
            notif_rect = notif_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
            screen.blit(notif_surface, notif_rect)

    elif current_game_state == GAME_STATE_GAME_OVER:
        screen.fill((0, 0, 0)) # Fundo preto para a tela de Game Over
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(game_over_text, game_over_rect)

        # Mensagem para voltar ao título - SOMENTE VISÍVEL APÓS O TIMER ZERAR
        if game_over_timer <= 0:
            press_space_text = font.render("Pressione ESPAÇO para Continuar", True, (255, 255, 255))
            press_space_rect = press_space_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            screen.blit(press_space_text, press_space_rect)

    elif current_game_state == GAME_STATE_LEVEL_TRANSITION:
        screen.fill((0, 0, 0)) # Fundo preto para a transição de fase
        level_message = level_font.render(f"FASE {current_game_level}", True, (255, 255, 255))
        level_message_rect = level_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(level_message, level_message_rect)


    # --- 13. Atualiza a Tela ---
    pygame.display.flip()

    # --- 14. Controle de FPS ---
    clock.tick(FPS)

# --- 15. Finaliza o Pygame ---
pygame.quit()
print("Jogo encerrado!")