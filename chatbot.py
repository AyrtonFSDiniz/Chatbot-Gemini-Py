import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a chave da API do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Definir o contexto do negócio
CONTEXT = """
Você é um assistente virtual especializado em **sistemas logísticos e de supply chain** para empresas de médio e grande porte. 
Seu papel é responder perguntas de forma técnica, clara e objetiva, ajudando o usuário a entender conceitos, processos e melhores práticas na área. 
Você deve:

- Explicar funcionalidades de sistemas de gestão logística, como WMS (Warehouse Management System), TMS (Transportation Management System), ERP integrado e rastreamento de inventário.
- Ajudar na otimização de processos de supply chain, incluindo planejamento de demanda, controle de estoque, transporte e distribuição.
- Responder perguntas de forma didática, evitando informações irrelevantes.
- Considerar que o usuário fará no máximo três perguntas sobre o contexto, e ao final deverá gerar um resumo consolidado de todas as respostas fornecidas.

Contexto adicional: você deve assumir que tem acesso a todo o conhecimento necessário sobre sistemas logísticos e supply chain, e suas respostas devem refletir as práticas mais atuais e eficientes do mercado.
Reduza sua resposta a 500 tokens.
"""

# Função para interagir com a API do Gemini
def obter_resposta_pergunta(pergunta):
    try:
        # Usar a API correta do Gemini
        model = genai.GenerativeModel('gemini-1.5-flash') 
        
        # Criar o prompt completo
        prompt_completo = CONTEXT + "\n\nPergunta: " + pergunta
        
        # Gerar resposta
        response = model.generate_content(
            prompt_completo,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=500,
                temperature=0.7,
            )
        )
        
        return response.text.strip()
    
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

# Função principal para interação com o usuário
def iniciar_chatbot():
    print("Olá! Sou seu assistente virtual especializado em sistemas logísticos e de supply chain.")
    print("Você pode fazer até 3 perguntas. Digite 'sair' a qualquer momento para encerrar.")
    
    perguntas_restantes = 3
    respostas = []

    while perguntas_restantes > 0:
        try:
            pergunta = input(f"\nPergunta {4 - perguntas_restantes}: ").strip()
            
            # Permitir saída antecipada
            if pergunta.lower() in ['sair', 'quit', 'exit']:
                print("Encerrando o chatbot. Até logo!")
                break
            
            # Validar entrada vazia
            if not pergunta:
                print("Por favor, digite uma pergunta válida.")
                continue
            
            print("Processando sua pergunta...")
            resposta = obter_resposta_pergunta(pergunta)
            print("\nResposta:", resposta)
            
            respostas.append((pergunta, resposta))
            perguntas_restantes -= 1
            
        except KeyboardInterrupt:
            print("\n\nChatbot interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            continue

    # print(f"\nDEBUG: Total de respostas coletadas: {len(respostas)}")
    
    # Resumo das perguntas e respostas
    if len(respostas) > 0:

        print("REspostas coletadas:", len(respostas))  # Linha de debug;

        print("\n" + "="*50)
        print("RESUMO DAS SUAS PERGUNTAS E RESPOSTAS:")
        print("="*50)
        for idx, (pergunta, resposta) in enumerate(respostas, 1):
            print(f"\nPergunta {idx}: {pergunta}")
            print(f"Resposta {idx}: {resposta}")
            print("-" * 30)
    else:
        print("\nNenhuma pergunta foi registrada.")
    
    print("\nObrigado por usar o assistente de gerenciamento de estoque!")

if __name__ == "__main__":
    # Verificar se a chave da API está configurada
    if not os.getenv("GEMINI_API_KEY"):
        print("ERRO: Chave da API do Gemini não encontrada!")
        print("Certifique-se de que o arquivo .env contém: GEMINI_API_KEY=sua_chave_aqui")
    else:
        iniciar_chatbot()