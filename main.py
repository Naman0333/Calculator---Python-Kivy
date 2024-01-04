from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.resources import resource_add_path


class CalculatorApp(App):
    def build(self):
        self.icon = 'icon.png'


        self.experssion = TextInput(font_size=32, readonly=True,halign='right', multiline=False)
        layout = BoxLayout(orientation = 'vertical',spacing =5)
        layout.add_widget(self.experssion)

        buttons=[
            ['7','8','9','/'],
            ['6','5','4','*'],
            ['3','2','1','-'],
            ['.','0','=','+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing = 5)
            for button_text in row:
                button = Button(text = button_text,on_press = self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        return layout
    
    def on_button_press(self,instance):
        current_text = self.experssion.text 
        button_text = instance.text 


        if button_text == "=":
            try: 
                result = str(eval(current_text))
                self.experssion.text = result
            except Exception as e:
                self.experssion.text = "Error"

        else:
            self.experssion.text += button_text

if __name__ == '__main__':
    CalculatorApp().run()



