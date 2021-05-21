""" 
* Crossbar one bit

simulator lang=spice

.include '45nm_LP.pm'
.include 'MTJT.spi'


*pra escrever precisa de uma ddp de 0.9 e pra ler -0.36
.param cap = 55.5f

.param Vb = 1.6
.param Vnb = 0
.param Vhb = Vb/2

.param Vread = 1.6

.param Tpwl = 0.7n
.param Tpbl = 0.7n
.param TpRead = 1.7n
.param TpWrite= 2.7n

Vwl1 WL1 Gnd PWL 0 'Vhb'
Vwl2 WL2 Gnd PWL 0 'Vhb' '(Tpwl-1p)' 'Vhb' 'Tpwl' 'Vb' '(Tpwl+0.3n-1p)' 'Vb' '(Tpwl+0.3n)' 'Vhb' 'TpRead' 'Vhb' '(TpRead+1p)' 'Vread' '(TpRead+0.3n-1p)' 'Vread' '(TpRead+0.3n)' 'Vhb' '(TpWrite-1p)' 'Vhb' '(TpWrite)' 'Vnb' '(TpWrite+0.5n-1p)' 'Vnb' '(TpWrite+0.5n)' 'Vhb' '(3n+Tpwl)' 'Vhb' '(3n+Tpwl+1p)' 'Vread' '(3n+Tpwl+0.3n-1p)' 'Vread' '(3n+Tpwl+0.3n)' 'Vhb'
Vwl3 WL3 Gnd PWL 0 'Vhb' 

Vbl1 BL1 Gnd PWL 0 'Vhb' 
Vbl2 BL2 Gnd PWL 0 'Vhb' '(Tpbl-1p)' 'Vhb' 'Tpbl' 'Vnb' '(Tpbl+0.3n-1p)' 'Vnb' '(Tpbl+0.3n)' 'Vhb' '(TpWrite-1p)' 'Vhb' '(TpWrite)' 'Vb' '(TpWrite+0.5n-1p)' 'Vb' '(TpWrite+0.5n)' 'Vhb'
Vbl3 BL3 Gnd PWL 0 'Vhb'

Vgnd Gnd 0 0

* Bitcell
Vtest1 WL1 NM1 0
X1 NM1 BL1 MTJT

Vtest2 WL1 NM2 0
X2 NM2 BL2 MTJT

Vtest3 WL1 NM3 0
X3 NM3 BL3 MTJT

Vtest4 WL2 NM4 0
X4 NM4 BL1 MTJT

Vtest5 WL2 NM5 0
X5 NM5 BL2 MTJT

Vtest6 WL2 NM6 0
X6 NM6 BL3 MTJT

Vtest7 WL3 NM7 0
X7 NM7 BL1 MTJT

Vtest8 WL3 NM8 0
X8 NM8 BL2 MTJT

Vtest9 WL3 NM9 0
X9 NM9 BL3 MTJT

*Bitlines Capacitance
Cbl1 BL1 Gnd 'cap'
Cbl2 BL2 Gnd 'cap'
Cbl3 BL3 Gnd 'cap'

.TRAN 10p 5n

.option rawfmt="psfbin"

 """


file = "C:/Users/Bruno/Desktop/IC-2021/Python/1MTJ-HF.txt"
f = open(file, "w")

#ElementosMatriz = int(input("Quantos elementos vai ter a matriz?"))
ElementosMatriz = 256

print("* Crossbar one bit\n\nsimulator lang=spice\n\n.include '45nm_LP.pm'\n.include 'MTJT.spi'\n\n", file=open(file, "a"))
print(".param cap = 51f\n\n.param Vb = 1.6\n\n.param Vnb = 0\n\n.param Vvdd = Vb\n\n.param res = 10k\n\n.param Vhb = Vb/2\n\n.param Vread = Vb\n\n.param Tpwl = 0.7n\n.param Tpbl = 0.7n\n.param TpRead = 1.7n\n.param TpWrite = 2.7n\n\n", file=open(file, "a"))

if(pow(ElementosMatriz, 0.5) < 8):
    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        if i != int(pow(ElementosMatriz,0.5)/2):
            print("Vwl" + str(i) + " WL" + str(i) + " Gnd PWL 0 'Vhb'", file=open(file, "a"))
        else:
            print("Vwl" + str(i) + " WL" + str(i) + " Gnd PWL 0 'Vhb' '(Tpwl-1p)' 'Vhb' 'Tpwl' 'Vb' '(Tpwl+0.3n-1p)' 'Vb' '(Tpwl+0.3n)' 'Vhb' 'TpRead' 'Vhb' '(TpRead+1p)' 'Vread' '(TpRead+0.3n-1p)' 'Vread' '(TpRead+0.3n)' 'Vhb' '(TpWrite-1p)' 'Vhb' '(TpWrite)' 'Vnb' '(TpWrite+0.5n-1p)' 'Vnb' '(TpWrite+0.5n)' 'Vhb' '(3n+Tpwl)' 'Vhb' '(3n+Tpwl+1p)' 'Vread' '(3n+Tpwl+0.3n-1p)' 'Vread' '(3n+Tpwl+0.3n)' 'Vhb'", file=open(file, "a"))
    
    print("\n", file=open(file, "a"))

    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        if i != int(pow(ElementosMatriz,0.5)/2):
            print("Vbl" + str(i) + " BL" + str(i) + " Gnd PWL 0 'Vgnd'", file=open(file, "a"))
        else:
            print("Vbl" + str(i) + " BL" + str(i) + " Gnd PWL 0 'Vhb' '(Tpbl-1p)' 'Vhb' 'Tpbl' 'Vnb' '(Tpbl+0.3n-1p)' 'Vnb' '(Tpbl+0.3n)' 'Vhb' '(TpWrite-1p)' 'Vhb' '(TpWrite)' 'Vb' '(TpWrite+0.5n-1p)' 'Vb' '(TpWrite+0.5n)' 'Vhb'", file=open(file, "a"))
    
    print("\n\nVvdd Vdd Gnd 'Vvdd'\n\n", file=open(file, "a"))


    print("* Bitcell\n", file=open(file, "a"))
    k=1
    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        for j in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
            print("X" + str(k) + " WL" + str(i) + " NM" + str(k) + " MTJT", file=open(file, "a"))
            print("Vtest" + str(k) + " BL" + str(j) + " NM" + str(k) + " 0", file=open(file, "a"))
            k += 1
    
    print("\n\n* Bitlines Capacitance\n", file=open(file, "a"))
    
    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        print("Cbl" + str(i + ElementosMatriz + (2*int(pow(ElementosMatriz,0.5))) +1) + " BL" + str(i) + " Gnd 'cap'" , file=open(file, "a"))
    
    print("\n\n.TRAN 1p 10n\n\n.option rawfmt=\"psfbin\" ", file=open(file, "a"))
############################################################# WORDS DE  8  BITS ######################################################################   
else:
    for i in range( 1, int(ElementosMatriz/8)+1):
        if i != int((int(ElementosMatriz/8)+1)/2):
            print("Vwl" + str(i) + " WL" + str(i) + " Gnd PWL 0 'Vhb'", file=open(file, "a"))
        else:
            print("Vwl" + str(i) + " WL" + str(i) + " Gnd PWL 0 'Vhb' '(Tpwl-1p)' 'Vhb' 'Tpwl' 'Vb' '(Tpwl+0.3n-1p)' 'Vb' '(Tpwl+0.3n)' 'Vhb' 'TpRead' 'Vhb' '(TpRead+1p)' 'Vread' '(TpRead+0.3n-1p)' 'Vread' '(TpRead+0.3n)' 'Vhb' '(TpWrite-1p)' 'Vhb' '(TpWrite)' 'Vnb' '(TpWrite+0.5n-1p)' 'Vnb' '(TpWrite+0.5n)' 'Vhb' '(3n+Tpwl)' 'Vhb' '(3n+Tpwl+1p)' 'Vread' '(3n+Tpwl+0.3n-1p)' 'Vread' '(3n+Tpwl+0.3n)' 'Vhb'", file=open(file, "a"))
    
    print("\n", file=open(file, "a"))

    for i in range( 1,8+1):
        if i != int(8/2):
            print("Vbl" + str(i) + " BL" + str(i) + " Gnd PWL 0 'Vhb'", file=open(file, "a"))
        else:
            print("Vbl" + str(i) + " BL" + str(i) + " Gnd PWL 0 'Vhb' '(Tpbl-1p)' 'Vhb' 'Tpbl' 'Vnb' '(Tpbl+0.3n-1p)' 'Vnb' '(Tpbl+0.3n)' 'Vhb' '(TpWrite-1p)' 'Vhb' '(TpWrite)' 'Vb' '(TpWrite+0.5n-1p)' 'Vb' '(TpWrite+0.5n)' 'Vhb'", file=open(file, "a"))
    
    print("\n\nVvdd Vdd Gnd 'Vvdd'\n\n", file=open(file, "a"))


    print("* Bitcell\n", file=open(file, "a"))
    k=1
    for i in range( 1, 8+1):
        for j in range( 1, int(ElementosMatriz/8)+1):
            print("X" + str(k) + " WL" + str(j) + " NM" + str(k) + " MTJT", file=open(file, "a"))
            print("Vtest" + str(k) + " BL" + str(i) + " NM" + str(k) + " 0", file=open(file, "a"))
            k += 1
    
    print("\n\n* Bitlines Capacitance\n", file=open(file, "a"))
    
    for i in range( 1,8+1):
        print("Cbl" + str(i) + " BL" + str(i) + " Gnd 'cap'" , file=open(file, "a"))

    for i in range( 1,8+1):
        print("R" + str(i) + " BL" + str(i) + " Gnd 'res'" , file=open(file, "a"))
    
    print("\n", file=open(file, "a"))
    for i in range( 1, int(ElementosMatriz/8)+1):
        print("Cbl" + str(i+10) + " WL" + str(i) + " Gnd 'cap'" , file=open(file, "a"))

    print("\n\n.TRAN 1p 10n\n\n.option rawfmt=\"psfbin\" cmin=5f", file=open(file, "a"))
