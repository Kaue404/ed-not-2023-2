class Deque:
    """
        ESTRUTURA DE DADOS DEQUE
        Deque (Doubly-Ended QUEue) é uma estrutura de dados
        derivada da fila, que permite inserções e remoções
        em qualquer uma de suas extremidades. Com isso, o
        deque pode se comportar tanto como uma fila comum
        quanto como uma fila em que são admitidas inserções
        prioritárias e a possibilidade de desistência
        (remoção) do último item.
    """
    def __init__(self):
        """ Método construtor """
        self.__data = []    # Lista vazia

    def insert_front(self, val):
        """
            Método para inserção no início (posição 0)
        """
        self.__data.insert(0, val)

    def insert_back(self, val):
        """
            Método para inserção no final
        """
        self.__data.append(val)

    def is_empty(self):
        """
            Método que retorna se o deque está vazio ou não
        """
        return len(self.__data) == 0
    
    def remove_front(self):
        """
            Método de remoção do início
        """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de um deque vazio.")
        # Remove da posição 0
        return self.__data.pop(0)
    
    def remove_back(self):
        """
            Método de remoção do final
        """
        if self.is_empty():
            raise Exception("ERRO: impossível remover de um deque vazio.")
        # Remove da última posição
        return self.__data.pop()
    
    def peek(self, front = True):
        """
            Método que consulta um elemento do deque
            Se o parâmetro "front" for True (ou tiver
            sido omitido), retorna o primeiro elemento
            Senão, retorna o último elemento
        """
        if front: return self.__data[0] # Primeiro elemento
        else: return self.__data[-1]    # Último elemento

    def __str__(self):
        """
            Retorna uma representação do deque como string
        """
        return str(self.__data)