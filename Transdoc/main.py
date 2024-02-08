from kivymd.app import MDApp

from kivy.core.window import Window

from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.button import MDFloatingActionButton

class Transdocs(MDApp):

    def __init__(self):
        super().__init__()
        self.Ecran = None
        self.Tache = None
        self.Demarrage = None
        self.Progression = None
        self.manager_open = False
        self.RepertoireSelectionne = ""
        Window.bind(on_keyboard=self.events)
        # self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path)

    def build(self):
        self.theme_cls.theme_style = "Dark"

        self.Ecran = Screen()

        self.Demarrage = MDFloatingActionButton(icon="play", icon_size="50dp",
                                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                                                # on_release=self.Demarrer
                                                )

        self.Tache = MDLabel(text="Tache...(50%)", halign="center", valign="bottom",
                             pos_hint={"center_x": 0.5, "y": 0},
                             size_hint_y=None, height=40)

        self.Progression = MDProgressBar(width="100")

        self.Ecran.add_widget(self.Demarrage)
        self.Ecran.add_widget(self.Tache)
        self.Ecran.add_widget(self.Progression)

        return self.Ecran

    # def Demarrer(self, obj):
    #     self.file_manager_open()
    #
    #
    # def file_manager_open(self):
    #     self.file_manager.show(os.path.expanduser("~"))  # Affiche le gestionnaire de fichiers à partir du répertoire personnel de l'utilisateur
    #     self.manager_open = True
    #
    # def select_path(self, path: str):
    #     self.exit_manager()
    #     MDSnackbar(MDLabel(text=path), y=24, pos_hint={"center_x": 0.5, "center_y":0.9}, size_hint_x=0.8).open()
    #
    #
    # def exit_manager(self, *args):
    #     self.manager_open = False
    #     self.file_manager.close()
    #
    # def events(self, instance, keyboard, keycode, text, modifiers):
    #     if keyboard in (1001, 27):
    #         if self.manager_open:
    #             self.file_manager.back()
    #     return True


if __name__ == '__main__':
    Transdocs().run()
