from myhdl import *
from i74_hc_hct85 import FourBitComparator
@block
def banc():
    print("Intrari A3 A2 A1 A0 \t Intrari  B3 B2 B1 B0 \t Intrari de transport Ia>b Ia<b Ia=b \t  Iesirile A>B \t  A<B \t A=B")
    """se initializeaza cele 11 semnale de intrare si 3 de iesire"""
    A0, A1, A2, A3, B0, B1, B2, B3 = [Signal(intbv(0)) for i in range(8)]
    QAgB, QAsB, QAeB = [Signal(bool(0)) for i in range(3)]
    IAgB, IAsB, IAeB = [Signal(intbv(0)) for i in range(3)]
    Four_Bit_Comparator = FourBitComparator(A3, A2, A1, A0, B3, B2, B1, B0, IAgB, IAsB, IAeB, QAgB, QAsB, QAeB)
    @instance
    def Comparator():
        """" Avem 4 intrari, deci 2^4 combinatii """
        for index in range(2):
            for index2 in range(2):
                for index3 in range(2):
                    for index4 in range(2):
                        """ Intrarile A3, A2, A1, A0 sunt setate crescator, de la 0 la 15 """
                        A0.next = index
                        A1.next = index2
                        A2.next = index3
                        A3.next = index4
                        """ Intrarile B3, B2, B1, B0 sunt relative, ordinea in care le generam este mai putin importanta """
                        B0.next = index
                        B1.next = index3
                        B2.next = index3
                        B3.next = index2
                        """ Intrarile de transport sunt de fapt iesirile unui alt comparator in cazul in care se doreste simularea unui comparator cu mai mult de 4 biti 
                        Pentru scopul simularii unui singur comparator, IAgB, IAsB si IAgB au valori aleatorii care doar sa demonstreze functionalitatea corecta """
                        IAgB.next = index2
                        IAeB.next = index3
                        IAsB.next = index4
                        yield delay(5)
                        """" Formatarea modului in care sunt afisate valorile catre consola """
                        print("%10s %2s %1.98s %2s %16s %2s %2s %2s %27s %5s %4s %18s %7s %6s" % (A3, A2, A1, A0, B3, B2, B1, B0, IAgB, IAsB, IAeB, QAgB, QAsB, QAeB))
    return Four_Bit_Comparator, Comparator


sys = banc()
sys.config_sim(trace = True)
sys.run_sim()
