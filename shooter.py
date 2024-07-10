import pygame, random
pygame.init()

#tamaño de pantalla en el juego
width = 800
height = 600

size = [width,height]

#colores
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

#Inicializamos Sonido
pygame.mixer.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

#definir clases
def barraVida(surface, x, y, vida):
    bar_lenght = 100
    bar_height = 10
    llenar = (vida / 100) * bar_lenght
    borde = pygame.Rect(x-bar_lenght-5, y, bar_lenght, bar_height)
    llen = pygame.Rect(x-bar_lenght-5, y, llenar, bar_height)
    pygame.draw.rect(surface, green, llen)
    pygame.draw.rect(surface, green, borde, 1)


def mostrarTxt(surface,texto,size, pos_x, pos_y): #surface: lugar donde quiero escribir el texto
    fuente = pygame.font.SysFont("verdana",size)
    text_surface = fuente.render(texto,True,white) #texto listo para mostrar
    text_rect = text_surface.get_rect()
    text_rect.midtop = (pos_x, pos_y) #posicionar el texto
    surface.blit(text_surface,text_rect)

def show_gameOver():
    screen.blit(background,[0,0])

    mostrarTxt(screen, "Presione una tecla para empezar", 27, width/2, height / 10)
    mostrarTxt(screen, "Instrucciones", 27, width/2, height / 5)
    mostrarTxt(screen, "-Destruya los meteoros",20, width/2, height * 3/8)
    mostrarTxt(screen, "-Esquivelos",20, width/2, height * 3/7)
    mostrarTxt(screen, "-Coja esferas verdes para curarse",20, width/2, height * 3/6)
    mostrarTxt(screen, "-Diviértase",20, width/2, height * 3/5)

    pygame.display.flip()
    espera = True

    while espera:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
            if event.type == pygame.KEYUP: #si alguna tecla se levanto es pq se presionó
                espera = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resource/nave.png")
        #self.image.set_colorkey(black) #Para eliminar el borde/fondo negro
        #obtenemos el cuadro de la imagen
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width/2, height - 10)
        self.rect.centerx = width/2
        #self.rect.bottom = height - 10
        self.speed_x = 0
        self.speed_y = 0 #velocidad con la que se movera
        self.vida = 100

    def update(self):
        self.speed_x = 0
        self.speed_y = 0

        #verificamos si una tecla es presionada 
        keystate = pygame.key.get_pressed() #lista de las teclas presionadas

        if keystate[pygame.K_LEFT]:
            self.speed_x = -10
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 10
        if keystate[pygame.K_UP]:
            self.speed_y = -10
        if keystate[pygame.K_DOWN]:
            self.speed_y = 10

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #para que no pase los bordes de nuestra ventana
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top > height-90:
            self.rect.top = height-90  
        if self.rect.bottom <  90:
            self.rect.bottom = 90


    def shoot(self):
        disparo = Rayo(self.rect.centerx, self.rect.top) #la posicion del disparo será el centro de la nave
        all_sprites.add(disparo)
        list_disparos.add(disparo)
        sound_laser.play()




class Rayo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resource/laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = pos_x #centro del objeto, coincide con la nave
        self.rect.y = pos_y
        self.speed_y = -20 #neg, ya que empieza desde abajo, y va a ir decreciendo a medida que suba 

    def update(self):
        self.rect.y += self.speed_y #le sumamos la velocidad para que suba aut
        #cuando salga de la ventana, el disparo tiene que eliminarse de la lista de los sprites y de disparos
        if self.rect.bottom < 0:
            self.kill() #eliminamos todas las instancias del elemento


        
class Meteoros(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(img_meteoros) #elige un elemento de forma aleatoria de la lista de img_meteoros
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-150 , -100) #neg para que de el efecto de que está bajando 
        self.speed_y = random.randrange(1,10) #veloc aleatoria entre 1 y 10
        self.speed_x = random.randrange(-5,5) #para que el movimiento de los meteoros tamb sean en diagonal


    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        #cuando los meteoros desaparecen de la pantalla, vuelven a aparecer otros 
        if self.rect.top > height + 10 or self.rect.left < -50 or self.rect.right > width + 50:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100 , -40) #neg para que de el efecto de que está bajando 
            self.speed_y = random.randrange(1,10)


class Cura(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(img_cura) #elige un elemento de forma aleatoria de la lista de img_meteoros
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-150 , -100) #neg para que de el efecto de que está bajando 
        self.speed_y = random.randrange(1,10) #veloc aleatoria entre 1 y 10
        self.speed_x = random.randrange(-5,5) #para que el movimiento de los meteoros tamb sean en diagonal


    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        #cuando los meteoros desaparecen de la pantalla, vuelven a aparecer otros 
        if self.rect.top > height + 10 or self.rect.left < -50 or self.rect.right > width + 50:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100 , -40) #neg para que de el efecto de que está bajando 
            self.speed_y = random.randrange(1,10)


#Creamos una lista de imagenes, para que los meteoros sean de distintos tamaños 
img_meteoros = []
ruta_imgMeteoros = ["resource/meteoro1.png", "resource/meteoro2.png", "resource/meteoro3.png", "resource/meteoro4.png", "resource/meteoro5.png", "resource/meteoro6.png", "resource/meteoro7.png", "resource/meteoro8.png", "resource/meteoro9.png", "resource/meteoro10.png"]
img_cura = []
ruta_cura = ["resource/cura1.png","resource/cura2.png", "resource/cura3.png", "resource/particula.png"]
#cargamos las imagenes
for ruta in ruta_imgMeteoros:
    img_meteoros.append(pygame.image.load(ruta))

for ruta1 in ruta_cura:
    img_cura.append(pygame.image.load(ruta1))

#cargamos una imagen de fondo
background = pygame.image.load("resource/fondo.png")

#cargamos los sonidos
sound_laser = pygame.mixer.Sound("resource/laser2.ogg")
sound_explosion = pygame.mixer.Sound("resource/daño.ogg")
sound_daño = pygame.mixer.Sound("resource/explosion.ogg")
sound_cura = pygame.mixer.Sound("resource/cura.wav")

#MUSICA DE FONDO
pygame.mixer.music.load("resource/music.wav")
#modulamos el volumen de la musica de fondo
pygame.mixer.music.set_volume(1.0) #cuanto más sea el valor, más fuerte sonará 


game_over = True

#la musica de fondo la iniciamos afuera del ciclo del juego pq dentro del bucle tenemos el tick(60) y está se verá afectada
#para que se repita infinitamente es -1.. si colocamos 1 o 2 se repetirá la cant de veces indicada
pygame.mixer.music.play(loops=-1)

juego = True


#Ciclo donde se produce el juego
while juego:
    if game_over:
        game_over = False
        
        #mostramos la pantalla de game over
        show_gameOver()
        # VARIABLES
        #creamos un grupo que contendran todos los elementos que aparezcan en pantalla
        all_sprites = pygame.sprite.Group()
        #creamos un grupo de meteoros 
        list_meteoros = pygame.sprite.Group()
        #creamos el grupo de balas
        list_disparos = pygame.sprite.Group()

        #creamos un grupo de cura 
        list_cura = pygame.sprite.Group()

        # --- creamos el jugador y lo agregamos al grupo de sprites
        player = Player()
        all_sprites.add(player)

        # --- creamos meteoros y los agregamos a la lista
        for i in range(10):
            met = Meteoros()
            all_sprites.add(met) #lo agregamos al grupo de todos los sprites
            list_meteoros.add(met) #lo agregamos a la lista de meteoros 
            

        for i in range(2):
            cura = Cura()
            list_cura.add(cura) #lo agregamos a la lista de meteoros 


        # -- marcador
        score = 0


    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False

        #disparos
        elif event.type == pygame.KEYDOWN: #si se presiono una tecla
            if event.key == pygame.K_SPACE: #y esa tecla es la barra de espacio
                player.shoot()

    all_sprites.update()

    
    #COLISIONES

    # --> meteoro - laser (group collide, chequea las colisiones de un grupo con otro)
    
    list_destruidos = pygame.sprite.groupcollide(list_disparos,list_meteoros,True,True) #dos true para que desaparezcan ambos elementos
    #aumentamos en 10 al marcador cada vez que se destruye un meteoro
    for elem in list_destruidos:
        score += 10
        sound_explosion.play() 
        met = Meteoros()
        all_sprites.add(met) #lo agregamos al grupo de todos los sprites
        list_meteoros.add(met)


     
    list_destruidos1 = pygame.sprite.groupcollide(list_disparos,list_cura,True,True) #dos true para que desaparezcan ambos elementos
    #restamos en 3 la vida cuando destruya una esfera de vida
    for elem in list_destruidos1:
        sound_explosion.play() 
        score -= 3
        cura = Cura()
        all_sprites.add(cura) #lo agregamos al grupo de todos los sprites
        list_cura.add(cura)

        if score <= 0:
            score = 0



    #--> jugador - meteoro
    list_impactados = pygame.sprite.spritecollide(player,list_meteoros,True) #los objetos que choquen van a desaparecer con el true
    
    for golpe in list_impactados: #si hay algo en la lista es porque me pego un meteoro
        player.vida -=25
        sound_daño.play()
        met = Meteoros()
        all_sprites.add(met) #lo agregamos al grupo de todos los sprites
        list_meteoros.add(met)

        if player.vida <= 0:
            game_over = True


    #--> jugador - esfera de vida
    list_impactados1 = pygame.sprite.spritecollide(player,list_cura,True) #los objetos que choquen van a desaparecer con el true
        
    for golpe in list_impactados1: #si hay algo en la lista es porque me pego una esfera de vida
        player.vida +=25
        sound_cura.play()
        cura = Cura()
        all_sprites.add(cura) #lo agregamos al grupo de todos los sprites
        list_cura.add(cura)
    
        if player.vida >= 100:
            player.vida = 100
    
    
    #blit actualiza toda la pantalla, [0,0] indica para que salga al comienzo
    #dibuja una superficie sobre otra(en este caso sobre screen)
    screen.blit(background,[0,0])
    all_sprites.draw(screen)
    
    #Visualizamos en marcador y vida en pantalla
    mostrarTxt(screen, "  Puntuacion:"+" "+ str(score).zfill(1),30, 400, 0)  
    barraVida(screen,width,5,player.vida)
    
    
    pygame.display.flip()




        