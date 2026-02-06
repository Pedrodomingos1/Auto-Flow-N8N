import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")


def disparar_automacao(image_url, caption):
    if not WEBHOOK_URL:
        print("❌ Erro: A variável de ambiente 'N8N_WEBHOOK_URL' não está definida.")
        return

    data_hoje = datetime.now().strftime("%Y-%m-%d")
    payload = {
        "image_url": image_url,
        "caption": f"{caption} - Gerado em: {data_hoje}",
        "folder_name": f"Postagens_{data_hoje}"
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        if response.status_code == 200:
            print(f"✅ Status: {response.status_code}")
        else:
            print(f"⚠️ Status: {response.status_code} - Resposta: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
    except Exception as e:
        print(f"❌ Erro: {e}")


def upload_arquivo_drive(caminho_arquivo, agendamento=None, caption=None):
    if not WEBHOOK_URL:
        print("❌ Erro: A variável de ambiente 'N8N_WEBHOOK_URL' não está definida.")
        return False

    try:
        with open(caminho_arquivo, "rb") as f:
            files = {"file": (os.path.basename(caminho_arquivo), f)}
            data = {}
            if agendamento:
                data["agendamento"] = agendamento
            if caption:
                data["caption"] = caption

            response = requests.post(WEBHOOK_URL, files=files, data=data, timeout=30)

        if response.status_code == 200:
            print(f"✅ Upload concluído: {response.status_code}")
            return True
        else:
            print(f"⚠️ Erro no upload: {response.status_code} - {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


if __name__ == "__main__":
    img = "https://images.unsplash.com/photo-1542831371-29b0f74f9713"
    texto = "Automação escalável com Python e n8n."
    disparar_automacao(img, texto)