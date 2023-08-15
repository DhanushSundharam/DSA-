from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.lang import Builder

username_helper = """
BoxLayout:
    orientation: 'vertical'
    MDTextField:
        id: text_field
        hint_text: "Send a Message"
        icon_right: "android"
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint_x: None
        width:300

    MDFillRoundFlatButton:
        text: "=>"
        icon:"images/send.png"
        pos_hint: {"center_x": 0.7,"center_y": 0.10}
        on_release: app.on_submit_button_click()
"""

class DemoApp(MDApp):
    username = None
    
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        return screen
    
    def on_submit_button_click(self):
        text = self.username.ids.text_field.text
        print(f"User input: {text}")
    
    
    

DemoApp().run()
