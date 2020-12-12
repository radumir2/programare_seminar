def suma(lista):
    rezultat = 0
    for element in lista:
        rezultat = rezultat + element
    return rezultat


def suma_f(lista):
    def suma_acc(acc, lista2):
        if lista2:
            return suma_acc(acc + lista2[0], lista2[1:])
        else:
            return acc
    return suma_acc(0, lista)


def suma_optim(lista, acc=None):
    if acc is None:
        return suma_optim(lista, 0)
    elif not lista:
        return acc
    else:
        return suma(lista[1:], acc+lista[0])
