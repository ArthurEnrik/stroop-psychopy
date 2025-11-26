---

Teste Stroop — Versão em PsychoPy

Um experimento interativo baseado no clássico Teste de Stroop, desenvolvido em Python usando o PsychoPy.
O objetivo é permitir a avaliação de atenção seletiva, controle inibitório e velocidade de processamento em diferentes níveis de dificuldade.






1. O que é o Teste Stroop

O Teste Stroop é um experimento clássico da psicologia cognitiva criado em 1935 por John Ridley Stroop.
Ele mede a nossa capacidade de inibir uma resposta automática — que, no caso, é ler a palavra — para em vez disso focar na cor da tinta.




2. Como o teste funciona

Você vê palavras que são nomes de cores, mas pintadas em cores diferentes.
A tarefa é clicar na cor da tinta, e não na palavra escrita.
Quando a palavra e a cor não combinam, acontece o famoso ‘conflito Stroop’, que aumenta o tempo de reação.




3. Por que isso acontece?

O cérebro tenta ler automaticamente, porque ler é um processo muito mais automático do que identificar cores.
Então ele precisa ‘desligar’ a leitura para focar só na cor — isso exige controle inibitório, uma habilidade importante das funções executivas.



4. O que mede exatamente

Ele mede três coisas principais:

Atenção seletiva

Velocidade de processamento

Controle inibitório
Essas três juntas formam uma parte essencial das funções executivas.




5. Aplicações do Teste Stroop

O Stroop é usado até hoje porque ele é simples e muito sensível para avaliar funções cognitivas.
Ele aparece em várias áreas, como:

Neuropsicologia clínica:
• Alzheimer e demências — pacientes costumam ter maior dificuldade por causa do declínio no controle inibitório.
• AVC e lesões frontais — o teste ajuda a medir sequelas cognitivas.

Saúde mental:
• TDAH — tempos de resposta maiores por dificuldade de manter atenção.
• Depressão e ansiedade — versões emocionais mostram como palavras negativas afetam a atenção.

Psicologia experimental e neurociência:
• Usado com fMRI e EEG para estudar o córtex pré-frontal e redes de controle cognitivo.


🎮 Funcionalidades do Programa

Modos de jogo

Introdutório — Palavra e cor sempre combinam.

Normal — Palavra e cor podem ser congruentes ou incongruentes.

Difícil — Além das incongruências, botões mudam de cor e posição a cada tentativa.


Temporizador opcional

Sem tempo

Lento

Normal

Rápido


O tempo restante aparece como contagem regressiva na tela.

Mecânica

Clique na cor da tinta, não na palavra escrita.

Respostas e tempos de reação são registrados.

10 tentativas por teste.



---

Resultados

Ao final do teste, o programa exibe:

Número total de acertos

Tempo médio de reação

Opções para:
✔ Voltar ao menu
✔ Repetir o teste
✔ Exportar resultados em CSV
✔ Fechar o programa



---

🛠 Tecnologias usadas

Python 3

PsychoPy (visual, event, core, gui)



---

 Como executar

1. Instale o PsychoPy

pip install psychopy

2. Baixe o código

Clone este repositório:

git clone https://github.com/ArthurEnrik/stroop-psychopy

3. Execute

python stroop.py


---

Estrutura básica do código

Interface inicial feita com gui.Dlg

Janelas e estímulos com visual.Window e visual.TextStim

Botões criados com visual.Rect

Captura de cliques com event.Mouse()

Contagem regressiva implementada com core.getTime()



---

 Exportação em CSV

Os resultados incluem para cada tentativa:

Palavra apresentada

Cor real da tinta

Resposta do usuário

Correto / incorreto

Tempo de reação
