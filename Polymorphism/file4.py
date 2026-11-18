#Ovewrriding Single Level Inheritanc eusing Super()
class Singer:
    def sing(self):
        print("A singer will sing a song")

class ClassicalSinger(Singer):
    def sing(self):
        super().sing()
        print("A classical singer will sing a song with melodies and classical music")

s1 = ClassicalSinger()
s1.sing()