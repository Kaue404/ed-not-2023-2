class Stack:
    """
        ESTRUTURA DE DADOS PILHA
        Trata-se de uma estrutura de dados linear de 
        acesso restrito, na qual tanto a operação de
        inserção  (tradicionalmente chamada "push"),
        quanto a operação de remoção ("pop"),
        acontecem no final (ou topo) da estrutura.
        Como consequência, o funcionamento da pilha
        obedece ao princípio LTFO (Last In, First Out):
        o último elemento a entrar é o primeiro a sair. 
    """

    def __init__(self):
        """ Método Construtor """
        # Cria uma lista privada e vazia para armazenar
        # os dados da pilha
        self.__data = []

    def push(self, val):
        """
            Método de Inserção
            Em pilhas, tem nome padronizado: push
        """
        self.__data.append(val)     # Insere no final

    def is_empty(self):
        """
            Método que verifica se a pilha está vazia ou não
        """
        return len(self.__data) == 0
    
    def pop(self):
        """
            Método para Remoção
            Em pilhas, tem nome padronizado: pop
        """

        if self.is_empty():
            raise Exception("ERRO: impossível remover de uma pilha vazia")
        return self.__data.pop()
    
    def peek(self):
        """
            Método que permite consultar o valor no topo da
            pilha, sem removê-lo
            Em pilhas, tem nome padronizado: peek (que
            significa "dar uma espiadinha" em inglês)
        """

        if self.is_empty():
            raise Exception("ERRO: impossível consultar uma pilha vazia")
        return self.__data[-1]      #Último elemento da lista
    
    def __str__(self):
        """
            Método que permite imprimir a lista interna como string
        """
        return str(self.__data)