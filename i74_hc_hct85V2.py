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
        FirstInputs = [A3, A2, A1, A0]  # Vectorul stocheaza bitii primului numar
        SecondInputs = [B3, B2, B1, B0]  # Vectorul stocheaza bitii celui de-al doilea numar
        EqualDigits = 0  # Un contor care numara biti egali
        """ 
        index ia pe rand fiecare bit din vectorul FirstInputs (Fiecare bit din numarul A)
        index2 ia pe rand fiecare bit din vectorul SecondInputs (Fiecare bit din numarul B)    
        instructiunea for de mai jos, incrementeaza concomitent cei doi indecsi
        astfel incat A se compara bit cu bit cu B
        """
        for index, index2 in zip(FirstInputs, SecondInputs):
            """" 
            EqualDigits se incrementeaza de fiecare data cand se ruleaza un ciclu in for
            In momentul in care se gaseste o diferenta intre index1 si index2 ciclul for
            se opreste automat prin comanda break
            """
            EqualDigits = EqualDigits + 1
            if index > index2:
                QAgB.next = 1
                QAeB.next = 0
                QAsB.next = 0
                break
            if index < index2:
                QAsB.next = 1
                QAeB.next = 0
                QAgB.next = 0
                break
            """" 
            Daca cei doi biti sunt egali, si s-au comparat toti bitii din vector
            se iau in calcul intrarile de transport IAeB, IAsB, IAgB
            """
            if index == index2:
                if(EqualDigits == FirstInputs.__len__()):
                    if IAeB == 1:
                        QAgB.next = 0
                        QAsB.next = 0
                        QAeB.next = 1
                        break
                    if IAgB > IAsB:
                        QAgB.next = 1
                        QAeB.next = 0
                        QAsB.next = 0
                        break
                    if IAgB < IAsB:
                        QAsB.next = 1
                        QAeB.next = 0
                        QAgB.next = 0
                        break
                    if IAeB < IAgB & IAsB:
                        QAsB.next = 0
                        QAeB.next = 0
                        QAgB.next = 0
                        break
                    if IAgB == IAeB == IAsB == 0:
                        QAsB.next = 1
                        QAeB.next = 0
                        QAgB.next = 1

    return Circuit4BitComparator