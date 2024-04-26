import csv

class Contato:
    def __init__(self, nome, telefone, tipo_telefone, aniversario, email):
        self.nome = nome
        self.telefone = telefone
        self.tipo_telefone = tipo_telefone
        self.aniversario = aniversario
        self.email = email

class Agenda:
    def __init__(self):
        self.contatos = []
    def adiciona_contato(self):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        
        print("Selecione o tipo de telefone:")
        print("1. Celular")
        print("2. Fixo")
        print("3. Residência")
        print("4. Trabalho")
        
        tipo_telefone_opcao = input("Opção: ")
        
        if tipo_telefone_opcao == "1":
            tipo_telefone = "celular"
        elif tipo_telefone_opcao == "2":
            tipo_telefone = "fixo"
        elif tipo_telefone_opcao == "3":
            tipo_telefone = "residência"
        elif tipo_telefone_opcao == "4":
            tipo_telefone = "trabalho"
        else:
            print("Opção inválida.")
            return
        
        aniversario = input("Data de aniversário (DD/MM/AAAA): ")
        email = input("Email: ")

        if any(contato.nome == nome for contato in self.contatos):
            print(f"Erro: Já existe um contato com o nome '{nome}'.")
            return

        self.contatos.append(Contato(nome, telefone, tipo_telefone, aniversario, email))
        print(f"Contato '{nome}' adicionado à agenda.")
    def apaga_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato '{nome}' removido da agenda.")
                return
        print(f"Contato '{nome}' não encontrado na agenda.")

    def altera_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                novo_nome = input("Novo nome: ")
                novo_telefone = input("Novo telefone: ")
                print("Selecione o tipo de telefone:")
                print("1. Celular")
                print("2. Fixo")
                print("3. Residência")
                print("4. Trabalho")
        
                novo_tipo_telefone_opcao = input("Opção: ")
        
                if novo_tipo_telefone_opcao == "1":
                    novo_tipo_telefone = "celular"
                elif novo_tipo_telefone_opcao == "2":
                    novo_tipo_telefone = "fixo"
                elif novo_tipo_telefone_opcao == "3":
                    novo_tipo_telefone = "residência"
                elif novo_tipo_telefone_opcao == "4":
                    novo_tipo_telefone = "trabalho"
                else:
                    print("Opção inválida.")
                    return
                novo_aniversario = input("Nova data de aniversário (DD/MM/AAAA): ")
                novo_email = input("Novo email: ")

                if any(c.nome == novo_nome for c in self.contatos if c.nome != contato.nome):
                    print(f"Erro: Já existe um contato com o nome '{novo_nome}'.")
                    return

                contato.nome = novo_nome
                contato.telefone = novo_telefone
                contato.tipo_telefone = novo_tipo_telefone
                contato.aniversario = novo_aniversario
                contato.email = novo_email
                print(f"Contato '{nome}' alterado com sucesso.")
                return

        print(f"Contato '{nome}' não encontrado na agenda.")

    def lista_contatos(self):
        if not self.contatos:
            print("Agenda vazia.")
            return

        print("Contatos na agenda:")
        for i, contato in enumerate(self.contatos, start=1):
            print(f"{i}. {contato.nome} ({contato.tipo_telefone}: {contato.telefone}) - Aniversário: {contato.aniversario} - Email: {contato.email}")


    def ordena_por_nome(self):
        self.contatos.sort(key=lambda x: x.nome)
        print("Agenda ordenada por nome.")

    def tamanho_agenda(self):
        print(f"Tamanho da agenda: {len(self.contatos)} contatos.")

    def grava_agenda_csv(self, nome_arquivo):
        nome_arquivo_csv = nome_arquivo + '.csv'  
        with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Nome', 'Telefone', 'Tipo de Telefone', 'Aniversario', 'Email'])
            for contato in self.contatos:
                writer.writerow([contato.nome, contato.telefone, contato.tipo_telefone, contato.aniversario, contato.email])
            print(f"Agenda gravada com sucesso no arquivo '{nome_arquivo_csv}'.")

    def menu(self):
        while True:
            print("\n*** Agenda ***")
            print("1. Adicionar Contato")
            print("2. Alterar Contato")
            print("3. Apagar Contato")
            print("4. Listar Contatos")
            print("5. Ordenar por Nome")
            print("6. Tamanho da Agenda")
            print("7. Gravar Agenda em CSV")
            print("8. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adiciona_contato()
            elif opcao == "2":
                nome = input("Nome do contato a ser alterado: ")
                self.altera_contato(nome)
            elif opcao == "3":
                nome = input("Nome do contato a ser removido: ")
                self.apaga_contato(nome)
            elif opcao == "4":
                self.lista_contatos()
            elif opcao == "5":
                self.ordena_por_nome()
            elif opcao == "6":
                self.tamanho_agenda()
            elif opcao == "7":
                nome_arquivo = input("Digite o nome do arquivo CSV para salvar a agenda: ")
                self.grava_agenda_csv(nome_arquivo)
            elif opcao == "8":
                print("Saindo da Agenda Eletrônica.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()
