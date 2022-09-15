import random


class Kort:
    def __init__(self, färg, valör):
        self.färg = färg
        self.valör = valör
    
    def __str__(self):
        return f'{self.färg}{self.valör}'
      

class Kortlek:
    def __init__(self):
        self.kortlek = []
        self.skapa_kortlek()
        random.shuffle(self.kortlek)

    def skapa_kortlek(self):
        self.kortlek = []
        for färg in ['\u2665', '\u2660', '\u2666', '\u2663']:
          for valör in range(2,15):
              self.kortlek.append(Kort(färg, valör))
     
    def dra_kort(self):
        return self.kortlek.pop().__str__()
        
        
class Spelare():
    def __init__(self, i):
        self.namn = f'Spelare_{i+1}'
        self.kort = []
        self.hand = []
        self.hand_namn = ''
        self.hand_värderank = 0
      
    def tilldela_kort(self):
        for i in range(1,8):
            draget_kort = kortlek.dra_kort()
            spelare.kort.append(draget_kort)  


class Handens_värde():
    def __init__(self, spelare_kort):
        kort = spelare_kort
        self.hand = []
        self.hand_namn = ''
        self.hand_värderank = 0
      
        # Sorterar handen enligt valör och färg. fs = färgsorterad
        kort = sorted(kort, key=lambda x:int(x[1:]), reverse = True)
        fs_kort = sorted(kort, key=lambda x:x[0])
   
        # Kontrollerar vilken hand spelaren har och tilldelar värden till attribut
        if self.royal_färgstege_och_färgstege(kort):
            return
        elif self.fyrtal(kort):
            return
        elif self.kåk(kort):
            return
        elif self.färg(fs_kort):
            return
        elif self.stege(kort):
            return
        elif self.triss(kort):
            return
        elif self.tvåpar_och_par(kort):
            return
        else:
            self.högsta_kort(kort)
            return 
         
    def royal_färgstege_och_färgstege(self, kort):
        for i in range(0,3): 
            # Kontrollerar färg & valör för var kort i spelarens hand
            if (int(kort[i][1:]) == int(kort[i+1][1:])+1 == int(kort[i+2][1:])+2 
                == int(kort[i+3][1:])+3 == int(kort[i+4][1:])+4) and (kort[i][0] 
                == kort[i+1][0] == kort[i+2][0] == kort[i+3][0] == kort[i+4][0]):
                # Om första kortet är ett ess
                if int(kort[i][1:]) == 14:
                    # Värden tilldelas till egna attribut
                    self.hand_namn = 'Royal-färgstege'
                    self.hand = [kort[0], kort[1], kort[2], kort[3], kort[4]]
                    self.hand_värderrank = 1
                    return True
                else:
                    # Värden tilldelas till egna attribut
                    self.hand = [kort[i], kort[i+1], kort[i+2], kort[i+3], kort[i+4]]
                    self.hand_namn = 'Färgstege'
                    self.hand_värderank = 2
                    return True
        return False
          
    def fyrtal(self, kort):
        for i in range(0,4):
            if kort[i][1:] == kort[i+1][1:] == kort[i+2][1:] == kort[i+3][1:]:
                # Bestäm hand
                # Tilldela hand
                self.hand = [kort[i], kort[i+1], kort[i+2], kort[i+3]]
                x = 0
                while len(self.hand) < 5:
                    if kort[x] not in [kort[i], kort[i+1], kort[i+1], kort[i+1]]:
                        self.hand.append(kort[x])
                    x += 1
                # Tilldela övriga attribut
                self.hand_namn = 'Fyrtal'
                self.hand_värderank = 3
                return True
        return False
    
    def kåk(self, kort):
        for i in range(0,5):
            if kort[i][1:] == kort[i+1][1:] == kort[i+2][1:]:
                for j in range(0,6):
                    if kort[j][1:] not in kort[i][1:] and (kort[j][1:] == kort[j+1][1:]):
                        # Värden tilldelas egna attribut
                        self.hand = [kort[i], kort[i+1], kort[i+2], kort[j], kort[j+1]]
                        self.hand_namn = 'Kåk'
                        self.hand_värderank = 4
                        return True
        return False
    
    def stege(self, kort):
        for i in range(0, 3):
            if (int(kort[i][1:]) == int(kort[i+1][1:])+1 == int(kort[i+2][1:])+2 
                == int(kort[i+3][1:])+3 == int(kort[i+4][1:])+4):
                # Värden tilldelas till egna attribut
                self.hand = (kort[i], kort[i+1], kort[i+2], kort[i+3], kort[i+4])
                self.hand_namn = 'Stege'
                self.hand_värderank = 6
                return True
        return False

    def triss(self, kort):
        for i in range(0,5):
            if kort[i][1:] == kort[i+1][1:] == kort[i+2][1:]:
                # Värden tilldelas till egna attributn
                # Tilldela hand
                self.hand = [kort[i], kort[i+1], kort[i+2]]
                x = 0
                while len(self.hand) < 5:
                    if kort[x][1:] != kort[i][1:]:
                        self.hand.append(kort[x])
                    x += 1
                # Tilldela övriga attribut
                self.hand_namn = 'Triss'
                self.hand_värderank = 7
                return True
        return False
      
    def färg(self, fs_kort):
        for i in range(0,3):
            if (fs_kort[i][0] == fs_kort[i+1][0] == fs_kort[i+2][0] 
                           == fs_kort[i+3][0] == fs_kort[i+4][0]):
                # Värden tilldelas till egna attribut
                self.hand = [fs_kort[i]
                            , fs_kort[i+1]
                            , fs_kort[i+2]
                            , fs_kort[i+3]
                            , fs_kort[i+4]]
                self.hand_namn = 'Färg'
                self.hand_värderank = 5      
                return True
        return False
      
    def tvåpar_och_par(self, kort):
        for i in range(0,6):
            if kort[i][1:] == kort[i+1][1:]:
                for j in range(i+2,6):
                    if kort[j][1:] == kort[j+1][1:]:
                        # Värden tilldelas till egna attribut
                        # Tilldela hand
                        self.hand = [kort[i], kort[i+1], kort[j], kort[j+1]]
                        x = 0
                        while len(self.hand) < 5:
                            if kort[x][1:] not in [kort[i][1:], kort[j][1:]]:
                                self.hand.append(kort[x])
                            x += 1
                        # Tilldela övriga attribut
                        self.hand_namn = 'Två-par'
                        self.hand_värderank = 8                     
                        return True
                    else:
                        # Värden tilldelas till egna attribut
                        # Tilldela hand
                        self.hand = [kort[i], kort[i+1]]
                        x = 0
                        while len(self.hand) < 5:
                            if kort[x][1:] != kort[i][1:]:
                                self.hand.append(kort[x])
                            x += 1
                        # Tilldela övriga attribut
                        self.hand_namn = 'Par'
                        self.hand_värderank = 9
                        return True
        return False
      
    def högsta_kort(self, kort):
        # Värden tilldelas till egna attribut 
        self.hand = [kort[0], kort[1], kort[2], kort[3], kort[4]]
        self.hand_namn = 'Högsta kort'
        self.hand_värderank = 10


def utskrift(lista_med_spelare, antal_spelare):
    utskrift = ''
    for i in range(0, antal_spelare): 
        # Spelarnamn och handnamn
        utskrift += f'{lista_med_spelare[i].namn}: {lista_med_spelare[i].hand_namn} ('
        # Konverterar numeriska valörer till knekt, dam, kung, ess
        for j in range (0, 5):
            valör = int(lista_med_spelare[i].hand[j][1:])
            färg = lista_med_spelare[i].hand[j][0]
            if valör < 11:
              utskrift += f'{färg}{valör}'
            elif valör == 11:
              utskrift += f'{färg}Kn'
            elif valör == 12:
              utskrift += f'{färg}Q'
            elif valör == 13:
              utskrift += f'{färg}K'
            else:
              utskrift += f'{färg}A'
            # Inget kommatecken efter sista kortet
            if j < 4:
                utskrift += ', '
            else:
                utskrift += ')\n'
    return utskrift

antal_spelare =  int(input('Antal spelare (1-7)?: '))
kortlek = Kortlek()
lista_med_spelare = []

# Skapar spelare, tilldelar kort, bestämmer handens värde och lägger in spelare i en lista
for i in range(0, antal_spelare):
    # Skapa spelare och tilldela kort
    spelare = Spelare(i)
    spelare.tilldela_kort()
    # Bestäm handens värde och tilldela handen till spelaren
    handens_värde = Handens_värde(spelare.kort)  
    spelare.hand = handens_värde.hand
    spelare.hand_namn = handens_värde.hand_namn
    spelare.hand_värderank = handens_värde.hand_värderank
    # Lägger in spelare i en lista
    lista_med_spelare.append(spelare)

sorterad_lista = sorted(lista_med_spelare, key=lambda x: (-x.hand_värderank
                                                          , int(x.hand[0][1:])
                                                          , int(x.hand[1][1:])
                                                          , int(x.hand[2][1:])
                                                          , int(x.hand[3][1:])
                                                          , int(x.hand[4][1:])), reverse=True)

utskrift = utskrift(sorterad_lista, antal_spelare)
print(utskrift)
