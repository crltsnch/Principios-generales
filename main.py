from matriz import Matriz

def main():
    m = Matriz([[1, 2], [3, 4]])
    m.imprimir()
    print()
    m_transpuesta = m.traspuesta()
    m_transpuesta.imprimir()

main()