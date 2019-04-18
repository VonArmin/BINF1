# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 19-12-2018
# opdracht: afvinkopdracht 6 blok 2 deel 1
# klas    : BIN-1B


def main():
    iterative()
    recursive()


def recursive(num1=0, num2=1, counter=0):
    """maakt de fobonacci sequentie van de eerste 900 nummers recursief
    :param num1: nummer van fibonacci
    :param num2: nummer an fibonacci
    :param counter: nummer dat elke recursie omhoog gaat om te zorgen dat het script stop vordat het geheugen op is
    :return: print van het nummer in de fibonacci reeks
    """
    counter+=1
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3
    if counter < 900:
        recursive(num1, num2, counter)


def iterative(num1=0, num2=1):
    """maakt de reeks van fibonacci iteratief
    :param num1: begin nummer 1
    :param num2: begin nummer 2
    :return:  print van het nummer in de fibonacci reeks
    """
    print(num1)
    print(num2)
    for num in range(900):
        num3 = num1+num2
        print(num3)
        num1 = num2
        num2 = num3


main()