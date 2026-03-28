import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MDT97App(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Welcome to Kivy MDT 97 Application!')
        layout.add_widget(label)

        button = Button(text='Click Me')
        layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MDT97App().run()