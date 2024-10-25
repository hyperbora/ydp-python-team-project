"""
프로그램 시작점
"""

import os
import kivy
from kivy.app import App
from kivy.uix.label import Label


kivy.require("2.3.0")
os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class MyFirstKivyApp(App):
    def build(self):
        return Label(text="Hello World !")


if __name__ == "__main__":
    MyFirstKivyApp().run()
