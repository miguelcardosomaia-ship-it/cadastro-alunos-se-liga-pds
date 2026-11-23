#Sistema de Cadastro de Alunos - Programa Se Liga! (POO em Python)

ARQUIVO = "alunos.txt"


class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 6:
            return "Aprovado"
        return "Recuperação"


# Lista que guarda os objetos Aluno
alunos = []


def ler_nota(mensagem):
    """Pede uma nota e só aceita valores entre 0 e 10."""
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um número válido.")
            continue
        if 0 <= nota <= 10:
            return nota
        print("A nota deve estar entre 0 e 10.")


def salvar():
    """Grava todos os alunos no arquivo .txt (um por linha: nome;nota1;nota2)."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for a in alunos:
            arquivo.write(f"{a.nome};{a.nota1};{a.nota2}\n")


def carregar():
    """Lê os alunos do arquivo ao abrir o programa."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha == "":
                    continue
                nome, nota1, nota2 = linha.split(";")
                alunos.append(Aluno(nome, float(nota1), float(nota2)))
    except FileNotFoundError:
        pass  # primeira vez rodando: ainda não existe arquivo


def cadastrar():
    nome = input("Nome do aluno: ").strip().replace(";", " ")
    if nome == "":
        print("O nome não pode ficar vazio.")
        return
    nota1 = ler_nota("Nota 1: ")
    nota2 = ler_nota("Nota 2: ")
    alunos.append(Aluno(nome, nota1, nota2))
    salvar()
    print("Aluno cadastrado com sucesso!")


def listar():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- Alunos cadastrados ---")
    for a in alunos:
        print(f"{a.nome} | Média: {a.media():.1f} | {a.situacao()}")


def buscar():
    termo = input("Nome para buscar: ").strip().lower()
    encontrou = False
    for a in alunos:
        if termo in a.nome.lower():
            print(f"{a.nome} | Média: {a.media():.1f} | {a.situacao()}")
            encontrou = True
    if not encontrou:
        print("Aluno não encontrado.")


def main():
    carregar()
    while True:
        print("\n===== CADASTRO DE ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno pelo nome")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()
