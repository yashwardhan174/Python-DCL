#Ovewrriding Multi-Level Level Inheritanc eusing Super()

class WhatsApp1:
    def send_msg(self):
        print("Single Tick Support")

class WhatsApp2(WhatsApp1):
    def send_msg(self):
        super().send_msg()
        print("Double Tick Support")

    def send_audio(self):
        print("1 min audio support")

class WhatsApp3(WhatsApp2):
    def send_msg(self):
        super().send_msg()
        print("Blue Tick Support")

    def send_audio(self):
        super().send_audio()
        print("Extra 5 min Audio Support")

    def send_video(self):
        print("Support 3 min Video ")

w = WhatsApp3()
w.send_msg()
w.send_audio()
w.send_video()