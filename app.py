from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

class VoiceInputApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = MDLabel(text="Say something:", halign="center")
        layout.add_widget(self.label)

        self.text_input = MDTextField(hint_text="Voice input via Gboard")
        layout.add_widget(self.text_input)

        return layout

if __name__ == '__main__':
    VoiceInputApp().run()