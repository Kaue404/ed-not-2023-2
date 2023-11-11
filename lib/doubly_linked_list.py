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
        if pos == 0:
            return self.__head

        # 2º caso: posição final (self.get_count() - 1), retorna self.__tail
        if pos == self.get_count() - 1:
            return self.__tail

        # 3º caso: posição intermediária

        # Se a posição estiver na primeira metade da lista, faz o percurso
        # a partir de self.__head, seguindo o ponteiro next
        if pos < self.get_count() // 2:
            # Percorre a lista quantas vezes forem necessárias para
            # encontrar o nodo
            node = self.__head
            for p in range(1, pos + 1):
                node = node.next
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
        if pos >= 0:
            self.__count += 1

    def insert_front(self, val):
        """
            Método de atalho para inserção no início da lista
        """
        self.insert(0, val)

    def insert_back(self, val):
        """
            Método de atalho para inserção no final da lista
        """
        self.insert(self.get_count(), val)

    def remove(self, pos):
        """
            Método que remove um nodo da lista, dada sua posição
        """

        # 1º caso: lista vazia ou posição fora dos limites
        if self.get_count() == 0 or pos < 0 or pos >= self.get_count():
            raise Exception("ERRO: posição inválida para remoção.")

        # 2º caso: remoção do início da lista
        if pos == 0:
            # Vamos remover o nodo apontado por __head
            removed = self.__head
            # O novo __head passa a ser o sucessor do nodo removido
            self.__head = removed.next
            # Se o novo __head for um nodo válido, ele não pode ter
            # um antecessor
            if self.__head is not None:
                self.__head.prev = None
            # Em caso de remoção do único nodo restante da lista, __tail
            # precisa passar a valer None também
            if self.get_count() == 1:
                self.__tail = None

        # 3º caso: remoção do último nodo da lista
        elif pos == self.get_count() - 1:
            # Vamos remover o nodo apontado por __tail
            removed = self.__tail
            # O novo __tail passa a ser o antecessor do nodo removido
            self.__tail = removed.prev
            # Se o novo __tail for um nodo válido, ele não pode ter um
            # sucessor
            if self.__tail is not None:
                self.__tail.next = None
            # Em caso de remoção do único nodo restante da lista, __head
            # precisa passar a valer None também
            if self.get_count() == 1:
                self.__head = None

        # 4º caso: remoção de posição intermediária
        else:
            # Pedimos a __find_node() para localizar o nodo a ser removido
            removed = self.__find_node(pos)
            before = removed.prev   # Nodo anterior ao que está sendo removido
            after = removed.next    # Nodo seguinte ao que está sendo removido
            # O nodo anterior passa a apontar, à frente, para o nodo posterior
            before.next = after
            # O nodo posterior passa a apontar, para trás, para o nodo anterior
            after.prev = before

        # Decrementa o contador de nodos
        self.__count -= 1

        return removed.data

    def remove_front(self):
        """
            Método de atalho para remoção da primeira posição
        """
        return self.remove(0)

    def remove_back(self):
        """
            Método de atalho para remoção da última posição
        """
        return self.remove(self.get_count() - 1)

    def peek(self, pos):
        """
            Retorna o valor data de um nodo, sem remover este da lista
        """
        if self.get_count() == 0 or pos < 0 or pos >= self.get_count():
            raise Exception("ERRO: posição inválida para consulta.")

        node = self.__find_node(pos)
        return node.data

    def peek_front(self):
        """
            Método de atalho para consulta da primeira posição
        """
        return self.peek(0)

    def peek_back(self):
        """
            Método de atalho para consulta da última posição
        """
        return self.peek(self.get_count() - 1)

    def __str__(self):
        """
            Método que cria uma representação da lista duplamente
            encadeada como string
        """
        if self.get_count() == 0:
            return "[*** LISTA VAZIA ***]\n\n"

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
