from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random
import re

class Random(App):

    def build(self):
        self.options =[]
        self.window =  BoxLayout(orientation="vertical")

        self.welcome = Label(text="[b] Welcome to Randomly [/b]"+ "\n Let a program choose your next task",size_hint_y=None, height=50, markup=True, halign='center')
        self.window.add_widget(self.welcome)

        self.options_text = TextInput(multiline=False,hint_text= "Add options separated by a space", size_hint_y=None, height=100)
        self.window.add_widget(self.options_text)


        self.button_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)

        self.choose_btn = Button(text="Choose", font_size = 20, background_color="grey", size_hint_x=0.3, size_hint_y=0.7)
        self.button_layout.add_widget(self.choose_btn)
        self.choose_btn.bind(on_press=self.choose)

        self.option_btn = Button(text="Add Option", font_size = 20, background_color="grey", size_hint_x=0.3, size_hint_y=0.7, pos_hint={'center_x': 0.5})
        self.button_layout.add_widget(self.option_btn)
        self.option_btn.bind(on_press=self.add_option)

        self.check_btn = Button(text="Check Lists", font_size = 20, background_color="grey", size_hint_x=0.3, size_hint_y=0.7)
        self.button_layout.add_widget(self.check_btn)
        self.check_btn.bind(on_press=self.check_lists)

        self.window.add_widget(self.button_layout)

        return self.window
    
    def add_option(self, instance):
        n = self.options_text.text.strip()
        if n:
            words = re.split(r'\s+',n)
            self.options.extend(words)
            self.options_text.text=""

    def choose(self, instance):
        n = len(self.options)
        num = random.randint(0,n-1)
        print(self.options[num])

    def check_lists(self, instance):
        pass



if __name__ == "__main__":
    app = Random()
    app.run()