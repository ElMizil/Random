from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDIconButton

class MDScreen(MDApp):

    def menu_open(self,btn):
        store = JsonStore('lists.json')
        print("Hola Mundo")
        keys = store.keys()
        menu_items_dict = [
            {"text": item, "viewclass": "OneLineListItem", "on_release": lambda x=item: self.menu_item_click(x)}
            for item in store
        ]
        if btn==1:
            call = self.root.ids.edit_button
        if btn==2:
            call = self.root.ids.delete_button
        # Update the dropdown menu with the retrieved lists
        self.drop = MDDropdownMenu(
            caller=call, items=menu_items_dict, width_mult=4
        )
        self.drop.open()

    def create_list(self):
        title = self.root.ids.list_title.text
        options = self.root.ids.list_options.text.split()
        store = JsonStore('lists.json')
        store.put(title, items=[options])
        self.root.ids.list_title.text = ""
        self.root.ids.list_options.text = ""

    def menu_item_click(self, selected_item):   
        # Change the screen based on the selected item
        if self.drop.caller.text == self.root.ids.edit_button.text:
            self.root.ids.screen_manager.current = "edit_list"
            store = JsonStore('lists.json')
            self.title = selected_item
            self.root.ids.elist_title.text = self.title
            option = store.get(selected_item)["items"]
            try:
                self.layout.clear_widgets()
                #self.root.ids.el_layout.remove_widget(self.layout)
                print("H")
            except:
                print("A")
            for i in option:
                self.layout = MDBoxLayout(orientation="horizontal",spacing="10dp",size_hint=(1, None), height="48dp")
                icon_button = MDIconButton(id=f"edit{i}",icon="pencil",
                                        icon_color= self.theme_cls.primary_color,
                                        width="48dp",
                                        on_release=self.edit_element)
                icon_button2 = MDIconButton(icon="delete", 
                                        icon_color= self.theme_cls.primary_color,
                                        width="48dp")
                label = MDLabel(id=i, text=i,pos_hint= {'x': 0.25})
                self.layout.add_widget(label)
                self.layout.add_widget(icon_button)
                self.layout.add_widget(icon_button2)
                self.root.ids.el_layout.add_widget(self.layout)

        if self.drop.caller.text == self.root.ids.delete_button.text:
            self.dialog = MDDialog(
                title="Delete list "+selected_item+"?",
                buttons=[
                    MDFlatButton(
                        text="Cancel",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                    MDFlatButton(
                        text="Accept",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.delete_list(selected_item)
                    ),
                ],
            )
            self.dialog.open()

    def delete_list(self,lista):
        print(lista)
        store = JsonStore('lists.json')
        store.delete(lista)
            
    def edit_element(self,instance):
        self.eid = instance.id[4:]
        self.edit_field = MDTextField(
        text=self.eid,
        hint_text="Element",
        id="edit_field"
        )
        self.edit_dialog = MDDialog(
            title="Edit element",
            type="custom",
            content_cls=
                self.edit_field,
            buttons=[
                MDFlatButton(
                        text="Cancel",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.edit_dialog.dismiss()
                ),
                MDFlatButton(
                        text="Change",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.edit()
                ),
            ]

        )
        self.edit_dialog.open()
        
    def edit(self):
        store = JsonStore('lists.json')
        data = store.get(self.title)
        my_list = data['items']
        new_text = self.edit_field.text
        for index, item in enumerate(my_list):
            if item == self.eid:
                my_list[index] = new_text
                break
        data['items'] = my_list
        store.put(self.title, **data)
        
        
            

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        return Builder.load_file("pruebas.kv")

MDScreen().run()