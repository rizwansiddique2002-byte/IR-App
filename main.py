from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp

class IRInterpreterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        layout.add_widget(MDLabel(text="IR Interpreter", halign="center", font_style="H5"))
        self.input_value = MDTextField(hint_text="Enter Wavenumber (cm⁻¹)", input_filter="float", mode="rectangle")
        layout.add_widget(self.input_value)
        layout.add_widget(MDRaisedButton(text="INTERPRET", pos_hint={"center_x": 0.5}, on_release=self.interpret_ir))
        self.result_label = MDLabel(text="Results will appear here.", halign="center")
        layout.add_widget(self.result_label)
        screen = MDScreen()
        screen.add_widget(layout)
        return screen

    def interpret_ir(self, instance):
        try:
            val = float(self.input_value.text)
            if 1700 <= val <= 1750: res = "Strong: C=O (Carbonyl)"
            elif 3200 <= val <= 3600: res = "Strong, Broad: O-H (Alcohol)"
            else: res = "No major match found."
            self.result_label.text = res
        except: self.result_label.text = "Enter a valid number."

if __name__ == "__main__":
    IRInterpreterApp().run()
