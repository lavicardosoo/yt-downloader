from kivy.uix.settings import text_type
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

design = Builder.load_file('design.kv')

Window.size = (1000,600)

class AghataNunes(BoxLayout):
    pass

class SaoriKido(App):
    def build(self):
        self.interface = AghataNunes()
        self.formato = 'mp3'
        return self.interface
    
    def getMP3(self):
        self.formato = 'mp3'
        print(self.formato)

    def getMP4(self):
        self.formato = 'mp4'
        print(self.formato)

    def baixarVideo(self):
        from pytubefix import YouTube

        try:
            link = self.interface.ids.linkDoVideo.text
            rodrigoapresentador = YouTube(link)

            if self.formato == 'mp4':
                doll = rodrigoapresentador.streams.get_highest_resolution()
                doll.download()

            else:
                doll = rodrigoapresentador.streams.get_audio_only()
                doll.download()
        except:
            print('tivemos um erro cis aquir')
    
app = SaoriKido()

app.run()

