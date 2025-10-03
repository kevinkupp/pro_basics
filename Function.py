"""Function examples."""


def func():
    """
    Trükib välja sõnumi "I´m inside the function".

    Returns:
        None
    """
    print("I´m inside the function")


def my_name_is(name):
    """
    Prindib lause "My name is " koos antud nimega.

    Args:
        name (str): Inimese nimi, mida soovitakse välja printida.

    Returns:
        None
    """
    print("My name is " + name)


def sum_six(num):
    """
    Lisab argumendile 6 ja tagastab tulemuse täisarvuna.

    Args:
        num (int või float): Sisendnumber.

    Returns:
        int: Sisendnumbrile 6 juurde liidetud summa täisarvuna.
    """
    return int(6 + num)


def sum_numbers(a, b) -> int:
    """
    Liidab kaks arvu ja tagastab summa täisarvuna.

    Args:
        a (int või float): Esimene arv.
        b (int või float): Teine arv.

    Returns:
        int: Arvude summa täisarvuna.
    """
    return int(a + b)


def usd_to_eur(usd: int) -> float:
    """
    Konverteerib dollari summa eurodeks kasutades vahetuskurssi 1 USD = 0.8 EUR.

    Args:
        usd (int): Raha summa dollarites.

    Returns:
        float: Raha summa eurodes, ümardatud kahe komakohani.
    """
    return round(usd * 0.8, 2)

