class DoublyLinkedList:
    """
        ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
        Trata-se de uma lista linear, em que seus
        elementos (chamados nodos ou nós) não estão
        fisicamente adjacentes uns dos outros, mas
        ligados logicamente por ponteiros que indicam
        o nodo anterior e o nodo seguinte da sequência.
        Não possui restrição de acesso - inserções,
        exclusões e consultas podem ser executadas em
        qualquer posição da lista.
    """

    class Node:
        """
            Classe interna que representa a unidade de
            informação (nodo) armazenada pela lista
            duplamente encadeada
        """
        def __init__(self, data):
            """ Construtor da classe interna Node """
            self.prev = None    # Ponteiro para o nodo anterior
            self.data = data    # Dado útil para o usuário
            self.next = None    # Ponteiro para o nodo seguinte

    def __init__(self):
        """
            Construtor da classe principal DoublyLinkedList
        """
        self.__head = None      # Ponteiro para o primeiro nodo
        self.__tail = None      # Ponteiro para o último nodo
        self.__count = 0        # Quantidade de nodos da lista

    def get_count(self):
        """
            Método que retorna a quantidade de nodos da lista
        """
        return self.__count

    def __find_node(self, pos):
        """
            Método PRIVADO que encontra um nodo na posição especificada
        """
        # 1º caso: posição 0, retorna self.__head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.get_count() - 1), retorna self.__tail
        if pos == self.get_count() - 1: return self.__tail

        # 3º caso: posição intermediária

        # Se a posição estiver na primeira metade da lista, faz o percurso
        # a partir de self.__head, seguindo o ponteiro next
        if pos < self.get_count() // 2:
            # Percorre a lista quantas vezes forem necessárias para
            # encontrar o nodo
            node = self.__head
            for p in range(1, pos + 1): node = node.next
            return node
        
        # Senão, a posição estando na segunda metade da lista, faz o
        # percurso reverso a partir de self.__tail, seguindo o ponteiro prev
        else:
            node = self.__tail      # Começa pelo último nodo
            for p in range(self.get_count() - 2, pos - 1, -1):
                node = node.prev
            return node
    
    def insert(self, pos, val):
        """
            Método que insere na posição "pos" o valor "val"
        """

        # Criamos um novo nodo para armazenar "val" e também
        # os ponteiros "prev" e "next", ambos apontando inicialmente
        # para None
        new = self.Node(val)

        # 1º caso: a lista está vazia, e "new" será, ao mesmo tempo,
        # o primeiro e o último nodo
        if self.get_count() == 0:   # Lista vazia
            self.__head = new
            self.__tail = new

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            new.next = self.__head
            self.__head.prev = new
            self.__head = new

        # 3º caso: inserção no final da lista
        # Obs.: consideramos como posição final qualquer uma que
        # seja >= self.get_count()
        elif pos >= self.get_count():
            new.prev = self.__tail
            self.__tail.next = new
            self.__tail = new

        # 4º caso: inserção em posição intermediária
        elif pos > 0:       # Descarta posições negativas
            # Busca o nodo que atualmente ocupa a posição onde será
            # feita a inserção
            current = self.__find_node(pos)

            # Determina o nodo anterior à posição de inserção
            before = current.prev

            # Efetua o encaixe do novo nodo na sequência
            before.next = new
            new.prev = before
            new.next = current
            current.prev = new

        # Incrementa a contagem de nodos da lista
        if pos >= 0: self.__count += 1

    def __str__(self):
        """
            Método que cria uma representação da lista duplamente
            encadeada como string
        """
        if self.get_count() == 0: return "[*** LISTA VAZIA ***]\n\n"

        repr = f"*** LISTANDO {self.get_count()} ITEM(NS) ***\n"
        repr += f"head: {hex(id(self.__head))}, tail: {hex(id(self.__tail))}\n"
        repr += ("=" * 80) + "\n"

        node = self.__head
        for pos in range(self.get_count()):
            repr += f"NODO posição {pos}, endereço: {hex(id(node))}\n"
            repr += f"Anterior: {hex(id(node.prev))}\n"
            repr += f"DADO: {node.data}\n"
            repr += f"Seguinte: {hex(id(node.next))}\n"
            repr += ("-" * 80) + "\n"
            node = node.next

        repr += "\n\n"
        return repr