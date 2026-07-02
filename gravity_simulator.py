import pygame

pygame.init() #pygame'in bütün modüllerini başlatıyor

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Gerçek pencereyi oluşturuyor.
pygame.display.set_caption("Gravity Simulator")

clock = pygame.time.Clock() #FPS kontrolü

class Body:
    def __init__(self, x, y, vx, vy, ax, ay, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.radius = radius
        self.color = color

trail = []

fonts = pygame.font.get_fonts()

font = pygame.font.SysFont("roboto", 55)
text_color = (255, 255, 255)

sun = Body(WIDTH // 2, HEIGHT // 2, 0, 0, 0, 0, 30, (255, 255, 0))
planet = Body(200, 400, 0, -2.7, 0, 0.05, 10, (255, 255, 255))

paused = False
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

            if event.key == pygame.K_r:
                planet.x = 200
                planet.y = 400
                planet.vx = 0
                planet.vy = -2.7
                trail.clear()

    if not paused:
        dx = sun.x - planet.x
        dy = (sun.y - planet.y)

        distance = (dx**2 + dy**2) ** 0.5

        G = 0.5
        planet_mass = 10000

        force = G * planet_mass / (distance ** 2)

        planet.ax = force * dx / distance
        planet.ay = force * dy / distance

        planet.vx += planet.ax
        planet.vy += planet.ay

        planet.x += planet.vx
        planet.y += planet.vy

        trail.append((int(planet.x),int(planet.y)))

        if len(trail) > 120:
            trail.pop(0)

        screen.fill((0, 0, 0)) #arka planı siyaha boyuyor

        for point in trail:
            pygame.draw.circle(screen, (100, 100, 100), point, 1)
        speed = (planet.vy**2 + planet.vx**2)**0.5

        text = font.render("Speed = " + str(speed), True, text_color)
        screen.blit(text, (10, 10))

        text_1 = font.render("Distance = " + str(distance), True, text_color)
        screen.blit(text_1, (10, 50))

        pygame.draw.circle(screen, sun.color, (sun.x, sun.y), sun.radius)
        pygame.draw.circle(screen, planet.color, (int(planet.x), int(planet.y)), planet.radius)
        pygame.display.flip() #Çizdiğimiz şeyleri ekrana gönderiyor

pygame.quit()