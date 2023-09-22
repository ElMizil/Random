from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDCheckbox

class MDScreen(MDApp):

    def menu_open(self):
        store = JsonStore('lists.json')
        keys = store.keys()
        menu_items_dict = [
            {"text": item, "viewclass": "OneLineListItem", "on_release": lambda x=item: self.menu_item_click(x)}
            for item in store
        ]
        # Update the dropdown menu with the retrieved lists
        MDDropdownMenu(
            caller=self.root.ids.edit_button, items=menu_items_dict, width_mult=4
        ).open()

    def create_list(self):
        title = self.root.ids.list_title.text
        options = self.root.ids.list_options.text
        store = JsonStore('lists.json')
        store.put(title, items=[options])
        self.root.ids.list_title.text = ""
        self.root.ids.list_options.text = ""

    def menu_item_click(self, selected_item):
        # Change the screen based on the selected item
        self.root.ids.screen_manager.current = "edit_list"
        store = JsonStore('lists.json')
        title = selected_item
        st = ""
        text = store.get(selected_item)["items"][0].split()
        for i in range(0,len(text)+1):
            pass            
        self.root.ids.elist_title.text = title
        self.root.ids.elist_options.text = st
        # Add more conditions to change screens for other menu items

        
        # Get the list associated with the title
        #item = store.get(title)
        
        #if item:
            # Update the existing list
         #   item['items'].append(options)
          #  store.put(title, items=item['items'])
        #else:
            # Create a new list if it doesn't exist
            

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        return Builder.load_file("pruebas.kv")

MDScreen().run()