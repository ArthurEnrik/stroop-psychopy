from psychopy import visual, event, core
import random

# === CONFIGURAÇÕES INICIAIS ===
cores = ["vermelho", "azul", "verde", "amarelo"]
mapa_cores = {
    "vermelho": "red",
    "azul": "blue",
    "verde": "green",
    "amarelo": "yellow"
}
tentativas_totais = 10  # número de tentativas por teste

# === JANELA ===
janela = visual.Window(size=[800, 600], color="white", units="pix")

# === MENU COM BOTÕES ===
titulo = visual.TextStim(
    janela,
    text="Escolha o tipo de teste:",
    color="black",
    height=40,
    pos=(0, 150)
)

botoes_menu = {
    "intro": visual.Rect(janela, width=300, height=80, fillColor="#90EE90", pos=(0, 50), lineColor="black", lineWidth=2),
    "normal": visual.Rect(janela, width=300, height=80, fillColor="#FFA07A", pos=(0, -80), lineColor="black", lineWidth=2)
}

labels_menu = {
    "intro": visual.TextStim(janela, text="Teste Introdutório", color="black", height=25, pos=(0, 50)),
    "normal": visual.TextStim(janela, text="Teste Normal ", color="black", height=25, pos=(0, -80))
}

# Desenha o menu inicial
titulo.draw()
for key in botoes_menu:
    botoes_menu[key].draw()
    labels_menu[key].draw()
janela.flip()

# === Espera clique do usuário ===
mouse = event.Mouse()
modo_congruente = None
clicado = False

while not clicado:
    for tipo, botao in botoes_menu.items():
        if mouse.isPressedIn(botao):
            clicado = True
            # efeito visual de clique
            botao.lineColor = "white"
            botao.lineWidth = 5
            botao.draw()
            labels_menu[tipo].draw()
            janela.flip()
            core.wait(0.15)
            botao.lineColor = "black"
            botao.lineWidth = 2

            if tipo == "intro":
                modo_congruente = True
            else:
                modo_congruente = False
            break

# === INSTRUÇÕES DE ACORDO COM O MODO ===
if modo_congruente:
    texto_instrucao = "TESTE INTRODUTÓRIO\n\n" \
                      "Clique na cor correspondente à tinta da palavra.\n\nPressione qualquer tecla para começar."
else:
    texto_instrucao = "TESTE NORMAL\n\n" \
                      "Clique na cor correspondente à tinta da palavra.\n\nPressione qualquer tecla para começar."

instrucao = visual.TextStim(janela, text=texto_instrucao, color="black", height=25, pos=(0, 100))
botao_iniciar = visual.Rect(janela, width=220, height=70, fillColor="#87CEFA", lineColor="black", lineWidth=2, pos=(0, -100))
texto_iniciar = visual.TextStim(janela, text="Iniciar Teste", color="black", height=28, pos=(0, -100))

instrucao.draw()
botao_iniciar.draw()
texto_iniciar.draw()
janela.flip()

mouse = event.Mouse()
clicou = False
while not clicou:
    if mouse.isPressedIn(botao_iniciar):
        clicou = True
        botao_iniciar.lineColor = "white"
        botao_iniciar.lineWidth = 5
        botao_iniciar.draw()
        texto_iniciar.draw()
        janela.flip()
        core.wait(0.15)
core.wait(0.2)


# === CONFIGURAÇÃO DOS BOTÕES DO TESTE ===
botoes = {}
y = -200
espacamento = 150
for i, cor in enumerate(cores):
    x = (i - 1.5) * espacamento
    botoes[cor] = visual.Rect(janela, width=120, height=60, fillColor=mapa_cores[cor],
                              pos=(x, y), lineColor="black", lineWidth=2)
    botoes[cor].label = visual.TextStim(janela, text=cor.capitalize(), color="black", pos=(x, y))

# === VARIÁVEIS DE CONTROLE ===
ultima_cor = None
resultados = []

# === LOOP DE TENTATIVAS ===
for i in range(tentativas_totais):
    palavra = random.choice(cores)

    if modo_congruente:
        cor_tinta = palavra
    else:
        while True:
            cor_tinta = random.choice(cores)
            if cor_tinta != ultima_cor:
                break
    ultima_cor = cor_tinta

    # Mostra estímulo
    texto = visual.TextStim(janela, text=palavra.upper(), color=mapa_cores[cor_tinta], height=80, pos=(0, 100))
    texto.draw()
    for botao in botoes.values():
        botao.draw()
        botao.label.draw()
    janela.flip()

    mouse = event.Mouse()
    clicado = False
    inicio = core.getTime()

    while not clicado:
        for cor, botao in botoes.items():
            if mouse.isPressedIn(botao):
                clicado = True
                tempo_reacao = core.getTime() - inicio

                # Efeito de "apertar" o botão
                botao.lineColor = "white"
                botao.lineWidth = 5
                botao.draw()
                botao.label.draw()
                janela.flip()
                core.wait(0.15)
                botao.lineColor = "black"
                botao.lineWidth = 2

                correto = (cor == cor_tinta)
                resultados.append({
                    "palavra": palavra,
                    "cor_tinta": cor_tinta,
                    "resposta": cor,
                    "correto": correto,
                    "tempo_reacao": round(tempo_reacao, 3)
                })
                break

# === RESULTADOS ===
acertos = sum(1 for r in resultados if r["correto"])
media_tempo = sum(r["tempo_reacao"] for r in resultados) / len(resultados)

resumo = visual.TextStim(
    janela,
    text=f"Teste concluído!\n\nAcertos: {acertos}/{len(resultados)}\n"
         f"Tempo médio: {media_tempo:.2f} s\n\nPressione qualquer tecla para sair.",
    color="black", height=30)
resumo.draw()
janela.flip()
event.waitKeys()

janela.close()
core.quit()
