class Queue:
    """
        ESTRUTURA DE DADOS FILA
        É uma estrutura de dados linear em que a operação
        de inserção ("enqueue") ocorre no final (ou cauda)
        da estrutura, enquanto a operação de remoção
        ("dequeue") ocorre no início (cabeça). Como
        consequência, o funcionamento da fila pode ser
        descrito pelo princípio FIFO (First In, First Out):
        o primeiro a entrar é o primeiro a sair.
    """
    def __init__(self):
        """ Método construtor """
        self.__data = []    # Lista vazia

    def enqueue(self, val):
        """
            Método de inserção
            Em filas, tem nome padronizado: enqueue
        """
        self.__data.append(val)     # Insere no final

    def is_empty(self):
        """
            Método que retorna se a fila está vazia ou não
        """
        return len(self.__data) == 0
    
    def dequeue(self):
        """
            Método de remoção
            Em filas, tem nome padronizado: dequeue
        """
        if self.is_empty():
            raise Exception("ERRO: não é possível remover de uma fila vazia.")
        # Remove do início (posição 0)
        return self.__data.pop(0)
    
    def peek(self):
        """
            Método para consultar o primeiro item da fila,
            sem removê-lo
        """
        if self.is_empty():
            raise Exception("ERRO: não é possível consultar uma fila vazia.")
        # Retorna o primeiro elemento (posição 0)
        return self.__data[0]
    
    def __str__(self):
        """
            Método que retorna uma representação da fila
            como string
        """
        return str(self.__data)