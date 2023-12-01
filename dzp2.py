class Node:
    def __init__(self, info = None):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
    def push(self, info):
        p = Node(info)
        if self.head.info == None:
            self.head = p
            self.tail = p
            p.next = self.head
        else:
            self.tail.next = p
            self.tail = p
            self.tail.next = self.head
    def pop(self):
        if self.head == None:
            return None
        else:
            if self.head != self.tail:
                p = self.head
                vrati = self.tail.info
                while (p.next != self.tail):
                    p = p.next
                self.tail = p
                self.tail.next = self.head
                return vrati
            else:
                vrati = self.head.info
                self.head.info = self.tail.info = None
                return vrati

operandi = set()
skup = {"+", "-", "*", "/"}
recnik = dict()
stek = LinkedList()
print("Meni:\n1. unos izraza\n2. unos vrednosti operanada\n3. promena vrednosti nekog od operanada\n4. izracunavanje izraza\n0. prekid programa")
while 1:
    print("Odaberite opciju iz menija ", end='')
    s = input()
    try:
        s = int(s)
    except ValueError:
        print("Niste uneli ceo broj")
        continue
    if s == 1:
        izraz = input("Unesite izraz: ")
        broj_operatora = 0
        broj_operanada = 0
        nije_validan = False
        operandi = set()
        for znak in izraz:
            if znak.isupper():
                operandi.add(znak)
                broj_operanada += 1
            elif znak in skup:
                broj_operatora += 1
            else:
                nije_validan = True
            if not(broj_operanada >= broj_operatora + 1):
                nije_validan = True
        if not(izraz[0].isupper()) or not(izraz[1].isupper()) or not(izraz[-1] in skup):
            nije_validan = True
        if nije_validan:
            print("Izraz nije validan!")
            continue
    elif s == 2:
        recnik = dict()
        if not operandi:
            print("Izraz nije unet")
            continue
        for operand in operandi:
            print("Unesite vrednost za promenljivu", operand)
            try:
                t = int(input())
            except ValueError:
                print("Niste uneli ceo broj")
                continue
            recnik[operand] = t
    elif s == 3:
        if not recnik:
            print("Izraz ili promenljive nisu unete")
            continue
        promenljiva = input("Unesite simbol za promenljivu koju zelite da promenite ")
        if promenljiva not in operandi:
            print("U izrazu ne postiji ta promenljiva")
            continue
        vrednost = int(input("Unesite novu vrednost "))
        recnik[promenljiva] = vrednost
    elif s == 4:
        try:
            for znak in izraz:
                if znak.isupper():
                    stek.push(recnik[znak])
                elif znak in skup:
                    drugi = stek.pop()
                    prvi = stek.pop()
                    if znak == '+':
                        stek.push(prvi + drugi)
                    elif znak == '-':
                        stek.push(prvi - drugi)
                    elif znak == '*':
                        stek.push(prvi * drugi)
                    elif znak == '/':
                        try:
                            stek.push(prvi / drugi)
                        except ZeroDivisionError:
                            print("Deljenje nulom nije dozvoljeno")
                            continue
            rezultat = stek.pop()
            if stek.pop() != None:
                print("Izraz nije validan!")
                continue
            print("Rezultat izraza je", rezultat)
        except NameError:
            print("Izraz ili promenljive nisu unete, pokusaj opet")
            continue
    elif s == 0:
        print("Kraj!")
        break
    else:
        print("Izabrana nepostojeca stavka, pokusaj opet")