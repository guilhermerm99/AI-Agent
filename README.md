# AI-Agent: Seu Instrutor de IA

---

Um agente de IA conversacional para instrução, desenvolvido com o framework `agents` e Gradio. Utiliza a API do Google Gemini, atuando como um tutor interativo para auxiliar usuários na criação e compreensão de agentes de IA. Perfeito para aprender e desenvolver!

---

### Recursos

* **Agente Conversacional:** Interação natural em português.

* **Modelo Gemini:** Alimentado por um dos modelos de linguagem mais avançados do Google.

* **Interface Gráfica Simples:** Utiliza Gradio para uma experiência de chat intuitiva via navegador.

* **Foco Educacional:** Direcionado a fornecer suporte na jornada de aprendizado sobre agentes de IA.

---

### Pré-requisitos

Para rodar este projeto localmente, você precisará ter o seguinte configurado em sua máquina:

* **Sistema Operacional:** Windows 10/11 com [WSL2 (Windows Subsystem for Linux)](https://learn.microsoft.com/pt-br/windows/wsl/install) instalado e configurado.

* **Python:** Versão 3.12 (ou compatível).

* **Git:** Para clonar o repositório.

* **Chave de API do Google Gemini:** Uma chave de API gerada através do [Google AI Studio](https://aistudio.google.com/).

---

### Configuração do Ambiente

Siga estes passos para configurar e rodar o projeto em seu ambiente WSL.

1.  **Clone o Repositório:**
    Abra seu terminal WSL (Linux) e clone este repositório:

    ```bash
    git clone git@github.com:guilhermerm99/AI-Agent.git
    ```

    (Se você configurou SSH, use a URL SSH. Caso contrário, use a URL HTTPS e autentique com um Personal Access Token do GitHub).

2.  **Navegue até o Diretório do Projeto:**

    ```bash
    cd AI-Agent
    ```

    *(Se você usou um nome de pasta diferente, substitua `AI-Agent` pelo nome correto, como `aula0`.)*

3.  **Crie o Arquivo de Variáveis de Ambiente (`.env`):**
    Na raiz do diretório do projeto, crie um arquivo chamado `.env` e adicione sua chave de API do Gemini nele. **Mantenha este arquivo seguro e nunca o suba para o controle de versão!**

    ```bash
    touch .env
    # Abra o .env com um editor de texto (ex: nano .env ou code .env) e adicione:
    # TOKEN="SUA_CHAVE_DE_API_GEMINI_AQUI"
    ```

    Substitua `"SUA_CHAVE_DE_API_GEMINI_AQUI"` pela sua chave real do Google AI Studio.

4.  **Instale o UV (Gerenciador de Pacotes Python):**
    Se você ainda não tem o UV instalado em seu ambiente WSL, execute:

    ```bash
    curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
    ```

5.  **Crie e Ative o Ambiente Virtual:**
    O UV facilita a criação de ambientes virtuais. Certifique-se de usar Python 3.12.

    ```bash
    uv venv --python 3.12
    source .venv/bin/activate
    ```

    Você precisará ativar o ambiente virtual toda vez que for trabalhar no projeto.

6.  **Instale as Dependências do Projeto:**
    Com o ambiente virtual ativado, instale todos os pacotes necessários:

    ```bash
    uv add gradio openai-agents python-dotenv
    ```

    Este comando lerá o `pyproject.toml` (que o `uv add` cria automaticamente) e instalará as dependências.

---

### Executando o Agente

Com todos os pré-requisitos e configurações feitos, você pode iniciar o agente:

1.  **Execute o Script Principal:**
    No terminal WSL (com o ambiente virtual ativado e dentro do diretório do projeto `AI-Agent`), execute:

    ```bash
    uv run main.py
    ```

    *Se seu arquivo principal não se chama `main.py`, ajuste o comando para o nome correto do arquivo.*

2.  **Acesse a Interface:**
    Ao executar o comando, o Gradio imprimirá no seu terminal duas URLs: uma local (`http://127.0.0.1:7860`) e uma pública (`https://[seu-id].gradio.live`). Abra uma dessas URLs em seu navegador para começar a interagir com o agente "Instrutor".

---

### Uso

Basta digitar suas perguntas ou solicitações na caixa de texto da interface do chat e pressionar `Enter` ou clicar em "Send". O agente responderá com base em suas instruções.

**Exemplos de Interação:**

* "Olá, Instrutor! Pode me explicar o que é um agente de IA?"

* "Como faço para criar uma ferramenta para o meu agente?"

* "Quais são os passos para depurar um agente?"

---

### Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou quiser reportar um problema, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
