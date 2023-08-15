from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, IconLeftWidget
from kivy.lang import Builder
import speech_recognition as sr
import openai

openai.api_key = "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"

login_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "App Name"
            halign: 'center'
            font_size: '28sp'
            size_hint_y: None
            height: "48dp"
        MDTextField:
            id: username_field
            hint_text: "Username"
            icon_left: "account"
            size_hint_x: None
            width: "200dp"
            pos_hint: {"center_x": 0.5}
        MDTextField:
            id: password_field
            hint_text: "Password"
            icon_left: "lock"
            size_hint_x: None
            width: "200dp"
            pos_hint: {"center_x": 0.5}
        MDFillRoundFlatButton:
            text: "Login"
            size_hint_x: None
            width: "200dp"
            pos_hint: {"center_x": 0.5}
            on_release: app.on_login_button_click()
"""

main_menu_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Main Menu"
            left_action_items: [["menu", lambda x: app.open_menu()]]
            elevation: 10
        BoxLayout:
            size_hint_y: None
            height: "48dp"
            pos_hint: {"center_x": 0.5}
            MDLabel:
                text: "App Logo"
                halign: 'center'
                font_size: '24sp'
            MDFillRoundFlatButton:
                text: "Logout"
                on_release: app.on_logout_button_click()
"""

class DemoApp(MDApp):
    login_screen = None
    main_menu_screen = None
    
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        
        self.login_screen = Builder.load_string(login_helper)
        self.main_menu_screen = Builder.load_string(main_menu_helper)
        
        screen = Screen()
        screen.add_widget(self.login_screen)
        return screen
    
    def on_login_button_click(self):
        username = self.login_screen.ids.username_field.text
        password = self.login_screen.ids.password_field.text
        
        if username == "admin" and password == "password":
            self.root.clear_widgets()
            self.root.add_widget(self.main_menu_screen)
        else:
            self.login_screen.ids.username_field.text = ""
            self.login_screen.ids.password_field.text = ""
            print("Invalid credentials!")
    
    def on_logout_button_click(self):
        self.root.clear_widgets()
        self.root.add_widget(self.login_screen)
    
    def open_menu(self):
        print("Open menu action")
        # Add your menu implementation here
    
DemoApp().run()
