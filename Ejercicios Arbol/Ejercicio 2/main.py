from Huffman import Huffman
from os import path

if __name__ == '__main__':
    huffman = Huffman()
    huffman.comprimir(path.dirname(__file__) + '/input.txt',
                      path.dirname(__file__) + '/output.txt')
    huffman.descomprimir(path.dirname(__file__) + '/output.txt',
                         path.dirname(__file__) + '/input2.txt')
