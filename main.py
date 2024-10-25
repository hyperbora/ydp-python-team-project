"""
프로그램 시작점
"""

import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
import platform

kivy.require("2.3.0")

# OS별 KIVY_GL_BACKEND 설정
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

class MyFirstKivyApp(App):
    """
    시작 메인 클래스
    """

    def build(self):
        return Label(text="Hello World !")


if __name__ == "__main__":
    MyFirstKivyApp().run()