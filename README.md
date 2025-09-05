# Chatbot Especializado em Sistemas Logísticos e Supply Chain

Este projeto é um chatbot desenvolvido em Python, especializado em sistemas logísticos e de supply chain, utilizando a API Gemini para responder a perguntas relacionadas à gestão logística, otimização de processos de supply chain e controle de inventário. O assistente é capaz de fornecer respostas técnicas, claras e objetivas sobre os principais sistemas utilizados na área, como WMS (Warehouse Management System), TMS (Transportation Management System), KPIs e melhores práticas de integração entre sistemas.

## Funcionalidades:

* **Assistente Virtual**: Responde a perguntas sobre **gestão de estoque**, **planejamento de demanda**, **controle de transporte** e **distribuição** de mercadorias.
* **Especialização em Supply Chain**: Oferece respostas baseadas nas práticas mais atuais e eficientes de supply chain.
* **Interação Simples**: O usuário pode fazer até 3 perguntas por vez, com um resumo das respostas ao final da conversa.
* **Comando de Encerramento**: Permite que o usuário encerre a conversa a qualquer momento com o comando "sair".

## Tecnologias Utilizadas:

* **Python 3.x**
* **API Gemini** para geração de respostas baseadas em IA
* **dotenv** para carregamento de variáveis de ambiente (como a chave da API)

## Como Executar:

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/AyrtonFSDiniz/Chatbot-Gemini-Py
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API Gemini:

   ```dotenv
   GEMINI_API_KEY=your_api_key_here
   ```

4. Execute o chatbot:

   ```bash
   python chatbot.py
   ```

5. O chatbot permitirá até 3 perguntas sobre logística e supply chain, e ao final fornecerá um resumo das respostas.
