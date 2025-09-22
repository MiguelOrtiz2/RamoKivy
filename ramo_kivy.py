from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
import os

# --- Carpeta con tus imágenes ---
carpeta = r"C:\Users\Miguel Ortiz\OneDrive\Desktop\RamoDigital"
imagenes = ["flor1.jpg", "foto1.jpg", "foto2.jpg", "foto3.jpg"]
imagenes = [os.path.join(carpeta, img) for img in imagenes]
indice = 0

# --- Mensajes iniciales ---
mensajes = [
    "Lamento no poder darte las flores de manera física...",
    "A pesar de todo, deseo poder tener a Dayra por el resto de mi vida como amiga."
]

# --- Crear ventana ---
Window.clearcolor = (1, 0.894, 0.710, 1)  # Fondo melocotón claro
Window.size = (480, 768)  # Tamaño inicial

class RamoApp(App):
    def build(self):
        self.root_layout = FloatLayout()
        
        # Imagen principal
        self.img_widget = Image(size_hint=(1, 0.8), pos_hint={'top': 1})
        self.root_layout.add_widget(self.img_widget)
        
        # Etiqueta para mensajes
        self.label = Label(text="", size_hint=(1, 0.2), pos_hint={'y':0}, halign="center", valign="middle", font_size=20)
        self.label.bind(size=self.label.setter('text_size'))
        self.root_layout.add_widget(self.label)
        
        # Mostrar mensajes iniciales con delay
        self.msg_index = 0
        Clock.schedule_once(self.mostrar_mensaje, 0.5)
        
        return self.root_layout

    def mostrar_mensaje(self, dt):
        if self.msg_index < len(mensajes):
            self.label.text = mensajes[self.msg_index]
            self.msg_index += 1
            Clock.schedule_once(self.mostrar_mensaje, 3)  # mostrar siguiente mensaje cada 3s
        else:
            # Después de los mensajes, iniciar carrusel de imágenes
            self.label.text = ""
            self.img_index = 0
            self.mostrar_imagen()
            Clock.schedule_interval(self.cambiar_imagen, 3)  # cambiar cada 3s

    def mostrar_imagen(self):
        self.img_widget.source = imagenes[self.img_index]

    def cambiar_imagen(self, dt):
        self.img_index = (self.img_index + 1) % len(imagenes)
        self.mostrar_imagen()

# --- Ejecutar aplicación ---
if __name__ == "__main__":
    RamoApp().run()
