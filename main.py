from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.properties import StringProperty
import random
Window.clearcolor = (.2, .2, .5, .2)


class Grid(Widget):
    roll_result = StringProperty('')
    die_selection = ''

    def roll_dice(self):
        if self.die_selection == '1d20':
            self.roll_result = str((random.randint(1, 20)))
        elif self.die_selection == '1d4':
            self.roll_result = str(random.randint(1, 4))
        elif self.die_selection == '1d6':
            self.roll_result = str(random.randint(1, 6))
        elif self.die_selection == '1d8':
            self.roll_result = str(random.randint(1, 8))
        elif self.die_selection == '1d10':
            self.roll_result = str(random.randint(1, 10))
        elif self.die_selection == '1d12':
            self.roll_result = str(random.randint(1, 12))
        elif self.die_selection == '1d100':
            self.roll_result = str(random.randint(1, 100))

    def update_die(self, die_selection):
        self.die_selection = die_selection


Builder.load_string("""
<LabelB>:
  bcolor: 1, 1, 1, 1
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")


class LabelB(Label):
    bcolor = ListProperty([1, 1, 1, 1])


Factory.register('KivyB', module='LabelB')


class DiceApp(App):
    def build(self):
        self.title = "Dice Roller"
        return Grid()


if __name__ == "__main__":
    DiceApp().run()
