from psychopy import visual, event, core, gui
import random
import csv
import os

def executar_teste():

    # ==== MENU INICIAL GUI ====
    menu = gui.Dlg(title="Configurações do Teste Stroop")
    menu.addText("Selecione o modo e o tempo:")

    menu.addField("Modo:", choices=["Introdutório", "Normal", "Difícil"])
    menu.addField("Temporizador:", choices=["Sem tempo", "Lento", "Normal", "Rápido"])

    resposta = menu.show()
    if resposta is None:
        core.quit()

    modo_escolhido = resposta[0]
    timer_escolhido = resposta[1]

    # Flags internas
    modo_congruente = (modo_escolhido == "Introdutório")
    modo_dificil = (modo_escolhido == "Difícil")

    # Temporizador
    if timer_escolhido == "Sem tempo":
        tempo_limite = None
    elif timer_escolhido == "Lento":
        tempo_limite = 5.0
    elif timer_escolhido == "Normal":
        tempo_limite = 3.0
    elif timer_escolhido == "Rápido":
        tempo_limite = 1.5


    # ===== CONFIGURAÇÕES ======
    cores = ["vermelho", "azul", "verde", "amarelo"]
    mapa_cores = {
        "vermelho": "red",
        "azul": "blue",
        "verde": "green",
        "amarelo": "yellow"
    }
    tentativas_totais = 10


    # ======== JANELA ==========
    janela = visual.Window(size=[800, 600], color="white", units="pix")


    # ===== INSTRUÇÕES =========
    if modo_congruente:
        texto_instrucao = "TESTE INTRODUTÓRIO\n\nClique na cor correspondente à tinta da palavra.\n\nClique para começar."
    elif modo_dificil:
        texto_instrucao = "MODO DIFÍCIL\n\nAs posições e cores dos botões serão embaralhadas.\nClique na cor correspondente à tinta da palavra.\n\nClique para começar."
    else:
        texto_instrucao = "TESTE NORMAL\n\nClique na cor correspondente à tinta da palavra.\n\nClique para começar."

    instrucao = visual.TextStim(janela, text=texto_instrucao,
                                color="black", height=28, pos=(0, 80))

    botao_iniciar = visual.Rect(janela, width=220, height=70, fillColor="#87CEFA",
                                lineColor="black", lineWidth=2, pos=(0, -120))
    texto_iniciar = visual.TextStim(janela, text="Iniciar Teste",
                                    color="black", height=28, pos=(0, -120))

    instrucao.draw()
    botao_iniciar.draw()
    texto_iniciar.draw()
    janela.flip()

    mouse = event.Mouse()
    while True:
        if mouse.isPressedIn(botao_iniciar):
            core.wait(0.15)
            break

    # ==========================
    # = BOTÕES DAS RESPOSTAS ===
    # ==========================
    botoes = {}
    y = -200
    espacamento = 150

    for i, cor in enumerate(cores):
        x = (i - 1.5) * espacamento
        rect = visual.Rect(janela, width=120, height=60,
                        fillColor=mapa_cores[cor], pos=(x, y),
                        lineColor="black", lineWidth=2)
        rect.label = visual.TextStim(janela, text=cor.capitalize(),
                                    color="black", pos=(x, y))
        botoes[cor] = rect

    # ==========================
    # ======== TESTE ===========
    # ==========================
    ultima_cor = None
    resultados = []

    for _ in range(tentativas_totais):

        palavra = random.choice(cores)

        # Cor congruente ou não
        if modo_congruente:
            cor_tinta = palavra
        else:
            while True:
                cor_tinta = random.choice(cores)
                if cor_tinta != ultima_cor:
                    break
        ultima_cor = cor_tinta

        # MODO DIFÍCIL — sem repetição de cores
        if modo_dificil:
            ordem_posicoes = cores[:]
            random.shuffle(ordem_posicoes)

            cores_fill = cores[:]
            random.shuffle(cores_fill)

            for i, cor in enumerate(ordem_posicoes):
                x = (i - 1.5) * espacamento
                botoes[cor].pos = (x, y)
                botoes[cor].label.pos = (x, y)
                botoes[cor].fillColor = mapa_cores[cores_fill[i]]

        # Estímulo
        texto = visual.TextStim(janela, text=palavra.upper(),
                                color=mapa_cores[cor_tinta],
                                height=80, pos=(0, 100))

        timer_display = visual.TextStim(
            janela,
            text="",
            color="black",
            height=28,
            pos=(330, 260)
        )

        mouse = event.Mouse()
        inicio = core.getTime()
        clicado = False

        # Tempo limite ativo
        if tempo_limite is not None:
            tempo_expira = inicio + tempo_limite
        else:
            tempo_expira = None

        while not clicado:

            # Atualiza contagem regressiva
            if tempo_expira is not None:
                tempo_restante = tempo_expira - core.getTime()

                if tempo_restante <= 0:
                    resultados.append({
                        "palavra": palavra,
                        "cor_tinta": cor_tinta,
                        "resposta": "Tempo esgotado",
                        "correto": False,
                        "tempo_reacao": tempo_limite
                    })
                    clicado = True
                    break

                timer_display.text = f"⏳ {tempo_restante:.1f}s"
            else:
                timer_display.text = ""

            # Desenha estímulo + botões + timer
            texto.draw()
            for bot in botoes.values():
                bot.draw()
                bot.label.draw()
            timer_display.draw()
            janela.flip()

            # Verifica cliques
            for cor, botao in botoes.items():
                if mouse.isPressedIn(botao):
                    tempo_reacao = core.getTime() - inicio
                    correto = (cor == cor_tinta)

                    botao.lineColor = "white"
                    botao.lineWidth = 5
                    botao.draw()
                    botao.label.draw()
                    janela.flip()
                    core.wait(0.15)
                    botao.lineColor = "black"
                    botao.lineWidth = 2

                    resultados.append({
                        "palavra": palavra,
                        "cor_tinta": cor_tinta,
                        "resposta": cor,
                        "correto": correto,
                        "tempo_reacao": round(tempo_reacao, 3)
                    })
                    clicado = True
                    break


    # ====== RESULTADOS ========
    acertos = sum(1 for r in resultados if r["correto"])
    media_tempo = sum(r["tempo_reacao"] for r in resultados) / len(resultados)

    # Tela de resumo
    resumo = visual.TextStim(janela,
                            text=f"Teste concluído!\n\n"
                                f"Acertos: {acertos}/{len(resultados)}\n"
                                f"Tempo médio: {media_tempo:.2f} s\n\n"
                                f"Escolha uma opção abaixo:",
                            color="black", height=28, pos=(0, 200))

    # Botões finais
    botoes_finais = {
        "menu": visual.Rect(janela, width=250, height=60, fillColor="#ADD8E6", pos=(0, 60)),
        "refazer": visual.Rect(janela, width=250, height=60, fillColor="#90EE90", pos=(0, -20)),
        "csv": visual.Rect(janela, width=250, height=60, fillColor="#FFD700", pos=(0, -100)),
        "fechar": visual.Rect(janela, width=250, height=60, fillColor="#FF7F7F", pos=(0, -180)),
    }

    textos_finais = {
        "menu": visual.TextStim(janela, text="Voltar ao menu inicial", color="black", pos=(0, 60)),
        "refazer": visual.TextStim(janela, text="Refazer o teste", color="black", pos=(0, -20)),
        "csv": visual.TextStim(janela, text="Exportar CSV", color="black", pos=(0, -100)),
        "fechar": visual.TextStim(janela, text="Fechar programa", color="black", pos=(0, -180)),
    }

    # Loop da tela final
    mouse = event.Mouse()
    while True:
        resumo.draw()
        for k in botoes_finais:
            botoes_finais[k].draw()
            textos_finais[k].draw()
        janela.flip()

        for nome, botao in botoes_finais.items():
            if mouse.isPressedIn(botao):
                core.wait(0.15)

                # === VOLTAR AO MENU ===
                if nome == "menu":
                    janela.close()
                    return "menu"

                # === REFAZER ===
                if nome == "refazer":
                    janela.close()
                    return "refazer"

                # === EXPORTAR CSV ===
                if nome == "csv":
                    nome_arquivo = "resultados_stroop.csv"
                    with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
                        w = csv.writer(f)
                        w.writerow(["palavra", "cor_tinta", "resposta", "correto", "tempo_reacao"])
                        for r in resultados:
                            w.writerow([r["palavra"], r["cor_tinta"], r["resposta"], r["correto"], r["tempo_reacao"]])

                    aviso = visual.TextStim(janela,
                                            text=f"Arquivo salvo como {nome_arquivo}!",
                                            color="black", height=30)
                    aviso.draw()
                    janela.flip()
                    core.wait(1.5)

                # === FECHAR ===
                if nome == "fechar":
                    janela.close()
                    core.quit()

# ================================
# ===== LOOP PRINCIPAL DO APP ====
# ================================
while True:
    acao = executar_teste()
    if acao == "menu":
        continue
    if acao == "refazer":
        continue
