#  Teste de Stroop com PsychoPy

Este projeto implementa uma versão interativa do **Teste de Stroop**, desenvolvido em **Python** com a biblioteca **[PsychoPy](https://www.psychopy.org/)**.  
O experimento foi criado para demonstrar o efeito Stroop — um fenômeno cognitivo que mede a interferência entre a leitura automática de palavras e o reconhecimento de cores.

---

##  Objetivo do Teste

O **Efeito Stroop** avalia a **atenção seletiva** e a **capacidade de inibição cognitiva**.  
Em tarefas de Stroop, o participante precisa identificar **a cor da tinta** em que uma palavra está escrita, ignorando o **significado da palavra**.  

- Exemplo: a palavra **“VERDE”** escrita na cor **vermelha** deve ser respondida como **“vermelho”**, e não “verde”.

Isso exige que o cérebro **ignore a resposta automática** (ler a palavra) e **responda à característica visual** (a cor da tinta).

---

## 🧩 Modos de Teste

O programa possui **dois modos** de execução:

1. ### **Modo Introdutório (Congruente)**
   - As palavras e as cores **são compatíveis** (ex: “VERMELHO” em vermelho).
   - Serve como **treinamento** para o participante se familiarizar com o teste.

2. ### **Modo Normal (Incongruente)**
   - As palavras e as cores **não coincidem** (ex: “AZUL” em verde).
   - Mede o **tempo de reação** e a **precisão** do participante diante do conflito cognitivo.

---

## 🖥️ Interface

O experimento usa **botões interativos** (em vez de teclado), tornando a interação mais intuitiva.  
O participante deve clicar no botão com o nome da **cor da tinta** da palavra apresentada.

🟩 O botão selecionado recebe um **destaque visual (borda)** e um **efeito de clique**, tornando a resposta clara.  
🔁 As tentativas são **limitadas** e sem repetições consecutivas de cor/palavra.

---



##  Requisitos

Antes de rodar o experimento, é necessário instalar o **PsychoPy**:
  O psychopy não é compativel com a versão python 3.12, então é necessário instalar o PsychoPy standalone: https://www.psychopy.org/download.html
  Após instalar, é necessário adicionar o interpretador do PsychoPy no Pycharm

  ## ⚙️ Instalação e Configuração do PsychoPy no PyCharm

Este projeto utiliza o **PsychoPy** para rodar os testes de Stroop com interface gráfica.  
Para executar o código corretamente no **PyCharm**, siga as etapas abaixo.

---

### 🧩 1. Instalar o PsychoPy

1. Acesse o site oficial do PsychoPy:  
   👉 [https://www.psychopy.org/download.html](https://www.psychopy.org/download.html)

2. Baixe o instalador correspondente ao seu sistema operacional (Windows, macOS ou Linux).

3. Execute o instalador e siga as instruções até concluir a instalação.

4. Após instalar, abra o **PsychoPy** uma vez para verificar se ele foi instalado corretamente.

---

### ⚙️ 2. Configurar o interpretador do PsychoPy no PyCharm

1. Abra o **PyCharm** e vá até:  
File → Settings → Project: stroop-psychopy → Python Interpreter

2. Clique no ícone de **engrenagem (⚙️)** no canto superior direito e selecione:  
Add Interpreter...

3. Escolha a opção:  
Add → System Interpreter

4. Clique em **Browse...** e procure o interpretador do Python instalado com o PsychoPy.  

- **No Windows**, geralmente está localizado em:  
  ```
  C:\Program Files\PsychoPy\python.exe
  ```
  ou  
  ```
  C:\Program Files\PsychoPy3\python.exe
  ```

- **No macOS/Linux**, o caminho pode variar, mas o interpretador está dentro da pasta de instalação do PsychoPy (procure por `psychopy.app/Contents/Resources/python`).

5. Selecione o arquivo `python.exe` (ou o executável equivalente no seu sistema) e clique em **OK**.

6. O PyCharm agora usará o mesmo ambiente do PsychoPy como interpretador do projeto.

---

### ▶️ 3. Executar o projeto

1. Abra o arquivo principal do teste (por exemplo, `stroop_test.py`).
2. Clique com o botão direito no editor e escolha **Run 'stroop_test'**.
3. O experimento será iniciado usando o PsychoPy.

---

💡 **Dica:**  
Para confirmar que o interpretador está configurado corretamente, abra o terminal do PyCharm e digite:

```bash
python -m psychopy

📊 Resultados

O tempo de reação e as respostas corretas/incorretas podem ser armazenados para análise posterior (implementação futura).
Esses dados permitem medir o grau de interferência cognitiva e o desempenho atencional do participante.




