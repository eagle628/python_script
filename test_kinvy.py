#!python3.6
#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty
import matlab.engine

class TextWidget(Widget):
    text = StringProperty()    #

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):
        eng = matlab.engine.start_matlab()        #
        a = eng.isprime(37)
        self.text = '37 is prime number : '+str(a)


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    TestApp().run()
