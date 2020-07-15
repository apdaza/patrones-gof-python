class BibliotecaLibros:
    def buscar_libros(self):
        return "buscando libros"

class BibliotecaMusica:
    def buscar_musica(self):
        return "buscando musica"

class BibliotecaVideos:
    def buscar_videos(self):
        return "buscando videos"

class Fachada:
    def __init__(self):
        self.biblioteca_libros = BibliotecaLibros()
        self.biblioteca_musica = BibliotecaMusica()
        self.biblioteca_videos = BibliotecaVideos()

    def buscar_libros(self):
        return self.biblioteca_libros.buscar_libros()

    def buscar_musica(self):
        return self.biblioteca_musica.buscar_musica()

    def buscar_videos(self):
        return self.biblioteca_videos.buscar_videos()