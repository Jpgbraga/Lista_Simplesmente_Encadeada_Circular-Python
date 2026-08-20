import os


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def adicionar(self, data):
        novo_no = Node(data)
        if self.head is None:
            
            self.head = novo_no
            self.tail = novo_no
            
            novo_no.next = self.head
        else:
           
            self.tail.next = novo_no
            
            self.tail = novo_no
            
            self.tail.next = self.head
        print(f"=> [{data}] adicionado à lista.")

    
    def excluir_primeiro(self):
        if self.head is None:
            print("=> A lista está vazia.")
            return
        
        removido = self.head.data
        if self.head == self.tail: 
            
            self.head = None
            self.tail = None
        else:
           
            self.head = self.head.next
            
            self.tail.next = self.head
        print(f"=> [{removido}] excluído do início.")

    
    def mostra_lista(self):
        if self.head is None:
            print("=> A lista está vazia.")
            return
        
        atual = self.head
        print("=> Lista Circular: ", end="")
        while True:
            print(f"[{atual.data}] -> ", end="")
            atual = atual.next
            
            if atual == self.head:
                break
        print("(volta ao início)")

    
    def alterar_valor(self, valor_antigo, novo_valor):
        if self.head is None:
            print("=> A lista está vazia.")
            return
        
        atual = self.head
        while True:
            if atual.data == valor_antigo:
                atual.data = novo_valor
                print(f"=> Valor [{valor_antigo}] alterado para [{novo_valor}].")
                return
            atual = atual.next
            if atual == self.head:
                break
        print(f"=> Valor [{valor_antigo}] não encontrado na lista.")

    
    def pesquisar_valor(self, valor):
        if self.head is None:
            print("=> A lista está vazia.")
            return
        
        atual = self.head
        posicao = 0
        while True:
            if atual.data == valor:
                print(f"=> Valor [{valor}] encontrado na posição {posicao}.")
                return
            atual = atual.next
            posicao += 1
            if atual == self.head:
                break
        print(f"=> Valor [{valor}] não encontrado na lista.")

    
    def excluir_especifico(self, valor):
        if self.head is None:
            print("=> A lista está vazia.")
            return
        
        atual = self.head
        anterior = self.tail 
        
        while True:
            if atual.data == valor:
                
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                
                elif atual == self.head:
                    self.head = self.head.next
                    self.tail.next = self.head
                
                elif atual == self.tail:
                    anterior.next = self.head
                    self.tail = anterior
                
                else:
                    anterior.next = atual.next
                    
                print(f"=> [{valor}] excluído da lista.")
                return
            
            anterior = atual
            atual = atual.next
            
            
            if atual == self.head:
                break
                
        print(f"=> Valor [{valor}] não encontrado para exclusão.")

    
    def excluir_ultimo(self):
        if self.head is None:
            print("=> A lista está vazia.")
            return
        
        removido = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            
            atual = self.head
            while atual.next != self.tail:
                atual = atual.next
                
            
            atual.next = self.head 
            self.tail = atual      
            
        print(f"=> [{removido}] excluído do final.")



def main():
    lista = ListaCircular()
    
    while True:
        print("\n---LISTA CIRCULAR----")
        print("1- Adicionar")
        print("2- Excluir o primeiro")
        print("3- Mostra lista")
        print("4- Alterar valor")
        print("5- Pesquisar valor")
        print("6- Excluir especifico")
        print("7- Excluir o ultimo")
        print("0- Sair")
        print("---------------------")
        
        opcao = input("Opcao: ")
        
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if opcao == '1':
            valor = input("Digite o valor para adicionar: ")
            lista.adicionar(valor)
            
        elif opcao == '2':
            lista.excluir_primeiro()
            
        elif opcao == '3':
            lista.mostra_lista()
            
        elif opcao == '4':
            velho = input("Digite o valor atual que deseja alterar: ")
            novo = input("Digite o novo valor: ")
            lista.alterar_valor(velho, novo)
            
        elif opcao == '5':
            valor = input("Digite o valor a pesquisar: ")
            lista.pesquisar_valor(valor)
            
        elif opcao == '6':
            valor = input("Digite o valor a ser excluído: ")
            lista.excluir_especifico(valor)
            
        elif opcao == '7':
            lista.excluir_ultimo()
            
        elif opcao == '0':
            print("Encerrando o programa...")
            break
            
        else:
            print("=> Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()