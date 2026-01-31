import os
import time
import schedule
from instagraapi import Client
from dotenv import load_dotenv

load_dotenv()

class AgendadorInstagram:
    def __init__(self):
        self.cl = Client()
        self.user = os.getenv("INSTA_USER")
        self.password = os.getenv("INSTA_PASS")

    def conectar(self):
        try:
            self.cl.login(self.user, self.password)
        except Exception as e:
            print(f"Erro: {e}")

    def tarefa_postar_feed(self, caminho, legenda):
        try:
            self.cl.photo_upload(caminho, legenda)
        except Exception as e:
            print(f"Erro: {e}")

    def tarefa_postar_story(self, caminho):
        try:
            self.cl.photo_upload_to_story(caminho)
        except Exception as e:
            print(f"Erro: {e}")

    def agendar_publicacao(self, hora, tipo, caminho, legenda=""):
        if tipo == "feed":
            schedule.every().day.at(hora).do(self.tarefa_postar_feed, caminho, legenda)
        elif tipo == "story":
            schedule.every().day.at(hora).do(self.tarefa_postar_story, caminho)

    def executar(self):
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    bot = AgendadorInstagram()
    bot.conectar()
    bot.agendar_publicacao("09:00", "story", "stories/foto1.jpg")
    bot.agendar_publicacao("18:00", "feed", "fotos/ensaio.jpg", "Confira meu novo trabalho.")
    bot.executar()