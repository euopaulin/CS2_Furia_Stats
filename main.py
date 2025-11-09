import os
import json
from google import genai
import dotenv

def build_system_instruction(prompt):
    SYSTEM_INSTRUCTION = f"""
    Você é um assistente virtual especializado no universo de The Witcher 3: Wild Hunt. Responda às perguntas dos usuários com base no conhecimento do jogo, incluindo personagens, missões, locais e lore. Mantenha suas respostas concisas e relevantes ao contexto do jogo.
    Pergunta: {prompt}
    Resposta:
    """
    return SYSTEM_INSTRUCTION
    

def api_generate_text(prompt):
    # Irá gerar o texto usando a API GenAI
    api_key = "AIzaSyBqUwL2pjjVzpztogLopcGVQMGeJXV26cY"



    if not api_key:
        print("Chave da API não encontrada. Verifique o arquivo .env.")
        return None
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            prompt=prompt,
            max_output_tokens=500,
            temperature=0.7,
        )
        return response.text
    except Exception as e:
        print(f"Erro ao gerar texto: {e}")
        return None