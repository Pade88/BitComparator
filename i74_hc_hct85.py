from myhdl import *

@block
def FourBitComparator(A3, A2, A1, A0, B3, B2, B1, B0, IAgB, IAsB, IAeB, QAgB, QAsB, QAeB):
    """ Functia primeste 14 parametri dupa cum urmeaza:
    @:param A3 = Bitul de pe pozitia 4 a primului numar
    @:param A2 = Bitul de pe pozitia 3 a primului numar
    @:param A1 = Bitul de pe pozitia 2 a primului numar
    @:param A0 = Bitul de pe pozitia 1 a primului numar
    @:param B3 = Bitul de pe pozitia 4 a celui de-al doilea numar
    @:param B2 = Bitul de pe pozitia 3 a celui de-al doilea numar
    @:param B1 = Bitul de pe pozitia 2 a celui de-al doilea numar
    @:param B0 = Bitul de pe pozitia 1 a celui de-al doilea numar
    @:param IAgB = Semnalul de "transport" (A>B, A greater than B) primit din iesirea altui comparator
    @:param IAsB = Semnalul de "transport" (A<B, A smaller than B) primit din iesirea altui comparator
    @:param IAgB = Semnalul de "transport" (A=B, A equals B) primit din iesirea altui comparator
    @:param QAgB = Semnalul de iesire in cazul in care primul numar este mai mare decat al doilea (A greater than B)
    @:param QAsB = Semnalul de iesire in cazul in care primul numar este mai mic decat al doilea (A smaller than B)
    @:param QAeB = Semnalul de iesire in cazul in care primul numar este egal cu cel de-al doilea numar (A equals B)
    """
    @always_comb
    def Circuit4BitComparator():
        """ Cazul in care un bit de pe o pozitie mai semnificativa din A este mai mare decat bitul din B de pe aceasi pozitie """
        if ((A3 and not(B3)) or (A3 and B3 or not(A3) and not(B3)) and (A2 and not(B2)) or (A3 and B3 or not(A3) \
             and not(B3)) and (A2 and B2 or not(A2) and not(B2)) and (A1 and not(B1)) or (A3 and B3 or not(A3) and not(B3)) \
             and (A2 and B2 or not(A2) and not(B2)) and (A1 and B1 or not(A1) and not(B1)) and (A0 and not(B0))):

            QAgB.next = True
            QAeB.next = False
            QAsB.next = False
        """" Cazul in care fiecare bit din A este egal cu fiecare bit din B """
        if ((A3 and B3 or not(A3) and not(B3)) and (A2 and B2 or not(A2) and not(B2)) and (A1 and B1 or not(A1) and not(B1)) and (A0 and B0 or not(A0) and not(B0))):
            """ Cazul 14 din tabela din adevar, toate intrarile de transport sunt 0(L), iesirile QAgB si QAsB sunt active(A<B) si (A>B) """
            if not (IAeB or IAgB or IAsB):
                QAgB.next = True
                QAeB.next = False
                QAsB.next = True
            """ Cazurile 12 si 11 din tabela de adevar, daca intrare IAeB este 1(H), indiferent de celalate 2 valori, iesirea este activa pe QAeB(A=B) """
            if IAeB:
                QAgB.next = False
                QAeB.next = True
                QAsB.next = False
            """ Cazul 9 din tabela de adevar, IAgB este 1(H), iar IAeB si IAsB sunt 0(L), iesirea activa este QAgB(A>B) """
            if IAgB and not (IAeB or IAsB):
                QAgB.next = True
                QAeB.next = False
                QAsB.next = False
            """" Cazul 10 din tabela de adevar, IAsB este 1(H), iar IAgB si IAeB sunt 0(L), iesirea activa este QAsB(A<B) """
            if IAsB and not (IAgB or IAeB):
                QAgB.next = False
                QAeB.next = False
                QAsB.next = True
            """ Cazul 13 din tabela de adevar, IAeB este 0(L) iar IAgB si IAsB sunt 1(H), toate iesirle sunt inactive """
            if not IAeB and (IAgB or IAsB):
                QAgB.next = False
                QAeB.next = False
                QAsB.next = False

        """ Cazul in care un bit de pe o pozitie mai semnificativa din A este mai mare decat bitul din B de pe aceasi pozitie """
        if ((not(A3) and B3) or (A3 and B3 or not(A3) and not(B3)) and (not(A2) and B2 ) or (A3 and B3 or not(A3) and not(B3)) \
             and (A2 and B2 or not(A2) and not(B2)) and (not(A1) and B1) or (A3 and B3 or not(A3) and not(B3)) and \
             (A2 and B2 or not(A2) and not(B2)) and (A1 and B1 or not(A1) and not(B1)) and (not(A0) and B0)):

            QAgB.next = False
            QAeB.next = False
            QAsB.next = True

    return Circuit4BitComparator