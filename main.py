#/////////////// LIBRARIES ///////////////////# {
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import runTouchApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import Screen
from kivy.logger import Logger
from kivy.properties import ObjectProperty
import kivy
kivy.require('1.1.2')
from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')


__author__ = 'Mark Anthony Remetir Pequeras'
__devteam__ = 'CoreSEC Softwares'

#/////////////// LIBRARIES ///////////////////# }






#/////////// C.C++.CPython ///////////////////# {

if True:
    try:
        import coreEngine #enhances performance :)
    except ImportError:
        pass              # never mind :(

#/////////// C.C++.CPython ///////////////////# }



#///////////////// KV Lang ///////////////////# {

Builder.load_string("""
# KV Language Start {

<Intro>:
    Button:
        background_normal: "introbg.jpg"
        background_down: "introbg.jpg"
    Button:
        id: Settings
        size_hint: None,None
        size: 280,50
        pos_hint: {"x":.23,"y":.4}
        background_normal: "startbutton.png"
        background_down: "startbutton-hover.png"
        on_press: root.move_to_game()
    Image:
        pos_hint: {"x":.01,"y":.1}
        source: "logo.png"

<Board>:


    ToggleButton:
        id: one_1
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()
    Button:
        id: one_2
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()
    Button:
        id: one_3
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()
    Button:
        id: two_1
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()
    Button:
        id: two_2
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()
    Button:
        id: two_3
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()
    Button:
        id: three_1
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()
    Button:
        id:three_2
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()
    Button:
        id: three_3
        background_normal: "blankbox.png"
        background_down: "blankbox.png"
        on_press: root.X_or_O()

<topBar>:

    Button:
        size_hint:.3,.1




# KV Language End }
""")

#///////////////// KV Lang ///////////////////# }






#///////////////// Python ///////////////////# {

class gameScreenManager(ScreenManager):
    def __init__(self,**kwargs):
        super(gameScreenManager,self).__init__(**kwargs)
        self.add_widget(intro_Screen(name="intro"))
        self.add_widget(game_Screen(name="gamexxx"))
        self.current = "intro"

### OPTIONS SCREEN START
def device_Geometry():
    pass

class options_Screen(Screen):
    pass

### OPTIONS SCREEN END


class Scratchy(ToggleButton):
    def __init__(self,**kwargs):
        super(Scratchy,self).__init__(**kwargs)

class Game_Logic():
    def __init__(self):
        self.player_1 = "x"
        self.player_2 = "o"
        self.next_Player = [] #Empty List (0x01, 0x02) P1,P2

    def whos_Next(self):
        pass

    def add_points(self):
        pass

    def race_to(self):
        pass

    def Current_Window(self):
        pass

### GAME SCREEN START

class topBar_BG(Image):
    def __init__(self,**kwargs):
        super(topBar_BG,self).__init__(**kwargs)
        self.size_hint=None,None
        self.source="topbg.jpg"
        self.allow_stretch=True
        self.size=1900,1800

class center_BG(Image):
    def __init__(self, **kwargs):
        super(center_BG, self).__init__(**kwargs)
        self.size_hint = .9,.64
        self.source = "centerbox.png"
        self.allow_stretch = True
        self.keep_ratio=False
        self.pos_hint={"x":.05, "y":.1}




class topBar(AnchorLayout):
    def __init__(self,**kwargs):
        super(topBar,self).__init__(**kwargs)
        self.anchor_x="right"
        self.anchor_y="top"
        self.add_widget(topBar_BG())


class Board(GridLayout):

    def __init__(self,**kwargs):  # Construct
        super(Board,self).__init__(**kwargs)
        # Methods
        self.size_hint=.8,.5
        self.pos_hint={"x":.1,"y":.17}
        self.set_center_x(180)
        self.set_center_y(133)
        self.set_top(223)
        self.cols=3
        self.rows=3

    def X_or_O(self):
        self.ids.one_1.background_normal="xbox.png"
        self.ids.one_1.disable=True

class game_Screen(Screen):
    """
    Main Game Screen
    """
    def __init__(self,**kwargs):
        super(game_Screen,self).__init__(**kwargs)
        self.add_widget(topBar_BG())
        self.add_widget(topBar())
        self.add_widget(center_BG())
        self.add_widget(Board())



### GAME SCREEN END

class Intro_BG(Image):
    def __init__(self,**kwargs):
        super(Intro_BG,self).__init__(**kwargs)
        self.source="introbg.jpg"
        self.size_hint=1,1


## INTRO SCREEN START

class Logo(Image):
    def __init__(self,**kwargs):
        super(Logo,self).__init__(**kwargs)
        self.source = "logo.png"

class Intro(FloatLayout):
#    def __int__(self,**kwargs):
#        super(Intro,self).__init__(**kwargs)
#        self.add_widget(Logo(),index=1)
    def move_to_game(self):
        gameScreenManager().current = "gamexxx"


class intro_Screen(Screen):
    def __init__(self,**kwargs):
        super(intro_Screen,self).__init__(**kwargs)
        self.add_widget(Intro())
### INTRO SCREEN END





# Main Function
class main(FloatLayout):

    def __init__(self,**kwargs):
        super(main,self).__init__(**kwargs)

        #self.add_widget(topBar_BG())

        self.add_widget(gameScreenManager())



#///////////////// Python ///////////////////# }



if __name__ == "__main__":
    runTouchApp(main())
    device_Geometry()












