import arcade
import random

# nous definissons les dimensions de l ecran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# nous creeons une liste de couleurs et en choisissons une au hasard
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]
random.choice(COLORS)


# nous creeons une classe cercle pour creer des objets "cercle"
class Cercle:
    def __init__(self, radius, centre_x, centre_y, color):
        self.radius = radius
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.color = color

    # cette methode va nous permettre de dessiner les cercles en questions lorsque celle ci sera appele
    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.radius, self.color)


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "fenetre")
        # nous creeons une liste dans laquelle nous allons pouvoir placer nos cercles
        self.list = []

    def setup(self):
        # nous creeons 20 cerlces
        for _ in range(20):
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercle = Cercle(rayon, center_x, center_y, color)
            # nous ajoutons chacun de ces cercles a la liste cree plus tot
            self.list.append(cercle)

    def on_draw(self):
        # c est ici que nous allons appeler la methode draw pour dessiner reellement les cercles sur l ecran selon le
        # nombre de cercles dans la liste,  c est a dire, 20
        arcade.start_render()
        for cercle in self.list:
            cercle.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # si le boutton est celui de droite, nous verifions si le click est situe dans un des 20 cercles a l aide d une
        # formule mathematique, si il l est, nous changeons sa couleur
        if button == arcade.MOUSE_BUTTON_RIGHT:
            for cercle in self.list:
                if (cercle.centre_x - cercle.radius) < x < (cercle.centre_x + cercle.radius) and (
                        cercle.centre_y - cercle.radius) < y < (cercle.centre_y + cercle.radius):
                    cercle.color = random.choice(COLORS)

        elif button == arcade.MOUSE_BUTTON_LEFT:
            # maintenant, si le boutton est le gauche, nous creeons une liste avec les cercles a effacer et y mettons
            # des cercles si notre click se trouvent sur ceux ci avec l aide de la meme formule mathematique
            cercles_to_remove = []
            for cercle in self.list:
                if (cercle.centre_x - cercle.radius) < x < (cercle.centre_x + cercle.radius) and (
                        cercle.centre_y - cercle.radius) < y < (cercle.centre_y + cercle.radius):
                    cercles_to_remove.append(cercle)
            # nous effacons les cercles qui sont dans la liste
            for cercle in cercles_to_remove:
                self.list.remove(cercle)


# finalement, nous associons les dimensions definis au debut avec l ecran en tant que tel puis executons le code
def main():
    my_game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    my_game.setup()

    arcade.run()


main()