import timeit as t


def teste_i(n):
    lista = [0] * n
    new_list = []

    for i in range(n):
        new_list.append(lista[i])

    return new_list


def teste_each(n):
    lista = [0] * n
    new_list = []

    for i in lista:
        new_list.append(i)

    return new_list


if __name__ == "__main__":
    setup_i = "from __main__ import teste_i"
    setup_each = "from __main__ import teste_each"

    print("Teste_I: ")
    print(t.timeit("teste_i(10000)", setup=setup_i))
    print("----/n")
    print("Teste_I: ")
    print(t.timeit("teste_each(10000)", setup=setup_each))
    print("----/n")
