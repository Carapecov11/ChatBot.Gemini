import google.generativeai as genai

# Configure a chave de API
genai.configure(api_key="AIzaSyDHuJ4BZlc5E7S4FC8JgPeCGoP7o6IS_mg")

# Inicialize o modelo (por exemplo, Gemini 1.5)
model = genai.GenerativeModel("gemini-1.5-pro")

# Lista para manter o histórico de mensagens
lista_mensagens = [
    {"role": "user", "parts": ["Você é um assistente útil que responde em português de forma clara."]}
]

# Função para enviar mensagem e obter resposta
def enviar_mensagem(mensagem, lista_mensagens=[]):
    # Adiciona a nova mensagem do usuário
    lista_mensagens.append({"role": "user", "parts": [mensagem]})

    # Cria uma sessão de chat com o histórico
    chat = model.start_chat(history=lista_mensagens)

    # Envia a mensagem e obtém resposta
    resposta = chat.send_message(mensagem)

    # Adiciona a resposta ao histórico
    lista_mensagens.append({"role": "model", "parts": [resposta.text]})

    return resposta.text

# Loop principal
while True:
    texto = input("Escreva aqui sua mensagem: ")

    if texto.lower() == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        print("Chatbot:", resposta)
