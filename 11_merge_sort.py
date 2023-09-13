def merge_sort(lista):
    """
        ALGORITMO DE ORDENAÇÃO MERGE SORT

        No processo de ordenação, esse algoritmo "desmonta"
        a lista original, contendo N elementos, até obter
        N listas com apenas um elemento cada uma. Em seguida,
        usando a técnica de mesclagem (merging), "remonta" a
        lista, desta vez com os elementos já em ordem.
    """
    # PARTE 1: DIVISÃO DA LISTA ORIGINAL EM LISTAS MENORES

    # Para que passa haver divisão da lista, esta deve ser
    # mais de um elemento
    if len(lista) > 1:

        # Encotra a posição do meio da lista, para fazer a divisão
        # em duas metades
        meio = len(lista) // 2

        # Tira uma cópia da primeira metade da lista
        sublista_esq = lista[:meio]
        # Tira uma cópia da segunda metade da lista
        sublista_dir = lista[meio:]

        # Chamamos recursivamente a prória função para que ela
        # continue repartindo cada sublista em duas partes menores
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

        #PARTE 2: REMONTAGEM DA LISTA, ORDENADAMENTE

        pos_esq = pos_dir = 0
        ordenada = []       # Lista vazia

        # Compara os elementos das sublistas entre si e insere
        # na lista ordenada o menor dentre dois elementos
        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):

            # O menor elemento está na sublista da esquerda
            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
                # "Desce" o elemento da esquerda para a lista ordenada
                ordenada.append(sublista_esq[pos_esq])
                pos_esq += 1    #Incrementa a posição da esquerda

            # O menor elemento está na sublista da direita
            else:
                # "Desce"o elemento da direita para a lista ordenada
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1    # Incrementa a posição da direita

            # Verificação da sobra
            sobra = []

            # Sobra à esquerda
            if(pos_esq < pos_dir): sobra = sublista_esq[pos_esq:]
            #Sobra à direita
            else: sobra = sublista_dir[pos_dir:]

            return ordenada + sobra