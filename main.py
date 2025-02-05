from gemini import Gemini
import sys

# →

operacao=input("Qual operação será feita? \n 1.Resolvedor \n 2.Avaliador \n 3.Tradutor\n")


if (operacao == "1"):
    n_sentencas = input("Digite o número de sentenças que existem no seu problema: ")
    print("Digite as sentenças (pressione Ctrl+D para finalizar):\nEx:\nA: Chuva\nB: Rua Molhada\nC: Rua Escorregadia\n")
    sentencas = sys.stdin.read().strip()
    print("Digite o problema utilizando quebra de linha para separar cada sentença e o número da mesma na frente (pressione Ctrl+D para finalizar): \nEx:\n1-A → B\n2-B → C\n3-A\n")
    problema = sys.stdin.read().strip()

    Gemini.resolvedor(n_sentencas,sentencas,problema)

elif (operacao == "2"):
    n_sentencas = input("Digite o número de sentenças que existem no seu problema: ")
    print("Digite as sentenças (pressione Ctrl+D para finalizar):\nEx:\nA: Chuva\nB: Rua Molhada\nC: Rua Escorregadia\n")
    sentencas = sys.stdin.read().strip()
    print("Digite o problema utilizando quebra de linha para separar cada sentença e o número da mesma na frente (pressione Ctrl+D para finalizar): \nEx:\n1-A → B\n2-B → C\n3-A\n")
    problema = sys.stdin.read().strip()
    print("Digite a resposta do problema (pressione Ctrl+D para finalizar): ")
    resolucao = sys.stdin.read().strip()

    Gemini.avaliador(n_sentencas,sentencas,problema,resolucao)
elif (operacao == "3"): 
    n_sentencas = input("Digite o número de sentenças que existem no seu problema: ")
    print("Digite o problema utilizando quebra de linha para separar cada sentença e o número da mesma na frente (pressione Ctrl+D para finalizar): \nEx:\n1.Se Ana for promovida, então Bruno não será promovido.\n2.Se Carlos for promovido, então Ana também será promovida.\n3.Bruno será promovido se, e somente se, Carlos não for promovido.")
    sentencas = sys.stdin.read().strip()
    print("Digite a resposta do problema (pressione Ctrl+D para finalizar): ")
    resolucao = sys.stdin.read().strip()

    Gemini.tradutor(n_sentencas, sentencas, resolucao)
else: print("Encerrando programa")


