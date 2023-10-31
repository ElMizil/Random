from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.toolbar import MDTopAppBar
import random
import re

class Random(MDApp):

    def build(self):
        self.options =[]
        self.window =  BoxLayout(orientation="vertical")
        self.theme_cls.theme_style = "Dark"

        # Create the side bar
        self.navigation = MDTopAppBar(title="Options", pos_hint={"top": 1})
        self.navigation.left_action_items = [
            ["account", lambda x: self.callback_method()],
            ["settings", lambda x: self.callback_method()],
        ]
        self.window.add_widget(self.navigation)

        # Create the welcome message using a Label
        self.welcome = Label(text="[b] Welcome to Randomly [/b]"+ "\n Let a program choose your next task",font_size='20sp',size_hint_y=None, height=800, markup=True, halign='center')
        self.window.add_widget(self.welcome)

        # Create the Input Text 
        self.options_text = TextInput(multiline=False,hint_text= "Add options separated by a space", size_hint_y=None, height=100)
        self.window.add_widget(self.options_text)

        # Create the layout for the buttons
        self.button_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)

        # Create the Add Option button
        self.option_btn = Button(text="Add Option", font_size = 20, background_color="grey", size_hint_x=0.3, size_hint_y=0.7)
        self.button_layout.add_widget(self.option_btn)
        self.option_btn.bind(on_press=self.add_option)

        # Create the Choose button
        self.choose_btn = Button(text="Choose", font_size = 20, background_color="grey", size_hint_x=0.3, size_hint_y=0.7, pos_hint={'center_x': 0.5})
        self.button_layout.add_widget(self.choose_btn)
        self.choose_btn.bind(on_press=self.choose)

        # Create the Check Lists button
        self.check_btn = Button(text="Check Lists", font_size = 20, background_color="grey", size_hint_x=0.3, size_hint_y=0.7)
        self.button_layout.add_widget(self.check_btn)
        self.check_btn.bind(on_press=self.check_lists)

        self.window.add_widget(self.button_layout)

        # create the Dropdown
        self.dropdown = DropDown()
        self.create_dropdown_options()

        return self.window
    
    def add_option(self, instance):
        n = self.options_text.text.strip()
        if n:
            words = re.split(r'\s+',n)
            self.options.extend(words)
            self.options_text.text=""

    def create_dropdown_options(self):
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]

        for option_text in options:
            button = Button(text=option_text, size_hint_y=None, height=40)
            button.bind(on_release=lambda btn: self.select_option(btn.text))
            self.dropdown.add_widget(button)

    def choose(self, instance):
        n = len(self.options)
        num = random.randint(0,n-1)
        print(self.options[num])

    def check_lists(self, instance):
        self.dropdown.open(instance)



if __name__ == "__main__":
    app = Random()
    app.run()