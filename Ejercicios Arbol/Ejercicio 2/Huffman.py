from Arbol import Arbol, Nodo


class Huffman:

    __text: str
    __frequency = {}
    __tree: Arbol
    __tablaHuffman = {}

    def __init__(self):
        self.__frequency = {}

    def armarArbol(self):
        frequency = list(
            sorted(self.__frequency.items(), key=lambda item: item[1]))
        nodos = []
        for char, freq in frequency:
            nodos.append(Nodo(char, freq))
        while len(nodos) > 1:
            izq = nodos.pop(0)
            der = nodos.pop(0)
            datos = (izq.getDato() + der.getDato(),
                     izq.getFreq() + der.getFreq())
            nodo = Nodo(*datos)
            if izq.getFreq() < der.getFreq():
                nodo.setIzquierda(izq)
                nodo.setDerecha(der)
            else:
                nodo.setIzquierda(der)
                nodo.setDerecha(izq)
            nodos.append(nodo)
        self.__tree = Arbol(nodos[0])

    def armarTablaHuffman(self, nodo, codigo):
        if nodo.esHoja():
            self.__tablaHuffman[nodo.getDato()] = codigo
        else:
            self.armarTablaHuffman(nodo.getIzquierda(), codigo + '0')
            self.armarTablaHuffman(nodo.getDerecha(), codigo + '1')

    def __getFrequency(self):
        for char in self.__text:
            if char in self.__frequency:
                self.__frequency[char] += 1
            else:
                self.__frequency[char] = 1
        return self.__frequency

    def encode(self):
        newText = ''
        for char in self.__text:
            newText += self.__tablaHuffman[char]
        chunks = []
        for i in range(len(newText), 0, -8):
            if i < 8:
                chunks.insert(0, int(newText[:i], 2))
            else:
                chunks.insert(0, int(newText[i-8:i], 2))
        return bytes(chunks)

    def comprimir(self, input, output):
        with open(input, 'r') as file:
            self.__text = file.read()
        self.__getFrequency()
        self.armarArbol()
        self.armarTablaHuffman(self.__tree.getRaiz(), '')
        encoded = self.encode()
        with open(output, 'wb') as file:
            file.write(encoded)

    def descomprimir(self, input, output):
        with open(input, 'rb') as file:
            compressed_data = file.read()

        binary_data = ''.join(format(byte, '08b') for byte in compressed_data)

        decoded_text = ""
        current_code = ""

        for bit in binary_data:
            current_code += bit
            for char, code in self.__tablaHuffman.items():
                if code == current_code:
                    decoded_text += char
                    current_code = ""
                    break

        with open(output, 'w') as file:
            file.write(decoded_text)
