import kivy
kivy.require('1.0.5')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

class Card24 (BoxLayout):
	"""docstring for 24Card """



class Card24App(App):
	
	def build(self):
		return Card24()


if __name__ == '__main__':
    Card24App().run()
		


