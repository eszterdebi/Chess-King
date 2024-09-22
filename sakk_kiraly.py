# Debreceni Eszter, H8766E
# 2022. 11. 16.
# Felhasznált források:
# órai munka

def tablaRajzol(tabla, terkoz, tablaSor, tablaCella):
    print(40*'\n')
    for sor in range(tabla):
        print(((1 + terkoz + 1 + terkoz) * tabla + 1)*"-")
        for cella in range(tabla):
            print("|", end="")
            if tablaSor == sor and tablaCella == cella:
                babu = 'K'
            else:
                babu = ' '
            print(terkoz * " " + babu + terkoz * " ", end="")
        print("|\n", end="")
    print(((1 + terkoz + 1 + terkoz) * tabla + 1)*"-")

def lepesBekeres():
    while 1:
        lep = input("Merre lépjen a király? (AWSD / X)\n")
        lep = lep.upper()
        if(lep == 'A' or lep == 'S' or lep == 'D' or lep == 'W' or lep == 'X'):
            return lep
            break
        else:
            print("Az AWSD gombokkal tudja irányítani a királyt!")

def lepes(tabla, terkoz, tablaSor, tablaCella):
    lep = lepesBekeres()
    while lep != 'X':
        if lep == 'W':
            if tablaSor > 0:
                tablaSor -= 1
            tablaRajzol(tabla, terkoz, tablaSor, tablaCella)
        elif lep == 'S':
            if tablaSor < tabla - 1:
                tablaSor += 1
            tablaRajzol(tabla, terkoz, tablaSor, tablaCella)
        elif lep == 'A':
            if tablaCella > 0:
                tablaCella -= 1
            tablaRajzol(tabla, terkoz, tablaSor, tablaCella)
        elif lep == 'D':
            if tablaCella < tabla - 1:
                tablaCella += 1
            tablaRajzol(tabla, terkoz, tablaSor, tablaCella)

        lep = lepesBekeres()
    print("JÁTÉK VÉGE")


def main():
    tabla = 8
    terkoz = 1
    tablaSor = 7
    tablaCella =4
    tablaRajzol(tabla, terkoz, tablaSor, tablaCella)
    lepes(tabla, terkoz, tablaSor, tablaCella)

main()