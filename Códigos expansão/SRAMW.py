# *Memoria de uma bitcell

# simulator lang=spice

# .include 'TRISTATE.spi'
# .include '6TBitCell.spi'
# .include 'PreCharge.spi'
# .include 'PassTransistor.spi'
# .include '45nm_LP.pm'

# .param VPre = 1

# .param TpEn = 0.5n
# .param TpWl = 1n

# .param cap = 15f

# Vwl1 WL1 Gnd PWL 0 0
# Vwl2 WL2 Gnd PWL 0 0 '(TpWl)' 0 '(TpWl+1p)' 1 (1.5n+2p) 1 (1.5n+3p) 0
# Vwl3 WL3 Gnd PWL 0 0

# Vwdb1 WDB1 Gnd 1
# Vwd1 WD1 Gnd 0
# Vwdb2 WDB2 Gnd 1
# Vwd2 WD2 Gnd 0
# Vwdb3 WDB3 Gnd 1
# Vwd3 WD3 Gnd 0

# *En liga em 1  ENB em 0
# Venb1 ENB1 Gnd PWL 0 1
# Ven1 EN1 Gnd PWL 0 0 
# Venb2 ENB2 Gnd PWL 0 1 '(TpEn-1p)' 1 'TpEn' 0 1.5n 0 (1.5n+1p) 1 
# Ven2 EN2 Gnd PWL 0 0 '(TpEn-1p)' 0 'TpEn' 1 1.5n 1 (1.5n+1p) 0 
# Venb3 ENB3 Gnd PWL 0 1
# Ven3 EN3 Gnd PWL 0 0

# Vpre1 PRE1 Gnd PWL 0 1
# Vpre2 PRE2 Gnd PWL 0 1 
# Vpre3 PRE3 Gnd PWL 0 1 

# Vvdd Vvdd Gnd 'VPre'

# Vdd1 Vdd1 Gnd 1
# Vdd2 Vdd2 Gnd 1
# Vdd3 Vdd3 Gnd 1
# Vdd4 Vdd4 Gnd 1
# Vdd5 Vdd5 Gnd 1
# Vdd6 Vdd6 Gnd 1
# Vdd7 Vdd7 Gnd 1
# Vdd8 Vdd8 Gnd 1
# Vdd9 Vdd9 Gnd 1

# Vgnd Gnd 0 0

# *Bitcell BC BL BLB WL Gnd Vdd
# X1 BL1 BLB1 WL1 Vdd1 Gnd BC
# X2 BL2 BLB2 WL1 Vdd2 Gnd BC
# X3 BL3 BLB3 WL1 Vdd3 Gnd BC
# X4 BL1 BLB1 WL2 Vdd4 Gnd BC
# X5 BL2 BLB2 WL2 Vdd5 Gnd BC
# X6 BL3 BLB3 WL2 Vdd6 Gnd BC
# X7 BL1 BLB1 WL3 Vdd7 Gnd BC
# X8 BL2 BLB2 WL3 Vdd8 Gnd BC
# X9 BL3 BLB3 WL3 Vdd9 Gnd BC

# *Write Driver
# X11 WD1 BL1 EN1 ENB1 Vdd1 Gnd TI
# X12 WDB1 BLB1 EN1 ENB1 Vdd1 Gnd TI
# X13 WD2 BL2 EN2 ENB2 Vdd2 Gnd TI
# X14 WDB2 BLB2 EN2 ENB2 Vdd2 Gnd TI
# X15 WD3 BL3 EN3 ENB3 Vdd3 Gnd TI
# X16 WDB3 BLB3 EN3 ENB3 Vdd3 Gnd TI

# *Pre Charge
# X21 BL1 BLB1 PRE1 Vdd1 PC
# X22 BL2 BLB2 PRE2 Vdd2 PC
# X23 BL3 BLB3 PRE3 Vdd3 PC

# *Bitlines Capacitance
# Cbl1 BL1 Gnd 'cap'
# Cblb1 BLB1 Gnd 'cap'
# Cbl2 BL2 Gnd 'cap'
# Cblb2 BLB2 Gnd 'cap'
# Cbl3 BL3 Gnd 'cap'
# Cblb3 BLB3 Gnd 'cap'
# .TRAN 100p 4n

# .option method=trap
# .option rawfmt="psfbin"
# .IC V(X5.Q)=0 V(X5.QB)=1 V(BL1)=0 V(BLB1)=1 V(BL2)=0 V(BLB2)=1 V(BL3)=0 V(BLB3)=1




file = "C:/Users/Bruno/Desktop/IC-2021/Python/SRAMW.txt"
f = open(file, "w")

#ElementosMatriz = int(input("Quantos elementos vai ter a matriz?"))
ElementosMatriz = 256

print("* SRAM memory core\n\nsimulator lang=spice\n\n.include '45nm_LP.pm'\n.include '6TBitCell.spi'\n.include 'TRISTATE.spi'\n.include 'PreCharge.spi'\n.include 'PassTransistor.spi'\n\n", file=open(file, "a"))
print(".param VPre = 1\n.param TpEn = 0.5n\n.param TpWl = 1n\n.param cap = 15f\n", file=open(file, "a"))

##################### PARA CORES COM WORDS DE 8 BITS #####################

########################## FONTES #########################################

for i in range( 1, int(ElementosMatriz/8)+1):
    if i != int((int(ElementosMatriz/8)+1)/2):
        print("Vwl" + str(i) + " WL" + str(i) + " Gnd PWL 0 0", file=open(file, "a"))
    else:
        print("Vwl" + str(i) + " WL" + str(i) + " Gnd PWL 0 0 '(TpWl)' 0 '(TpWl+1p)' 1 (1.5n+2p) 1 (1.5n+3p) 0", file=open(file, "a"))
    
print("\n", file=open(file, "a"))

for i in range( 1,8+1):
    print("Vwd" + str(i) + " WD" + str(i) + " Gnd 0", file=open(file, "a"))

print("\n", file=open(file, "a"))

for i in range( 1,8+1):
    print("Vwdb" + str(i) + " WDB" + str(i) + " Gnd 1", file=open(file, "a"))

print("\n", file=open(file, "a"))

for i in range( 1,8+1):
    if i != 4:
        print("Ven" + str(i) + " EN" + str(i) + " Gnd 0", file=open(file, "a"))
    else:
        print("Ven" + str(i) + " EN" + str(i) + " Gnd PWL 0 0 '(TpEn-1p)' 0 'TpEn' 1 1.5n 1 (1.5n+1p) 0", file=open(file, "a"))

print("\n", file=open(file, "a"))

for i in range( 1,8+1):
    if i != 4:
        print("Venb" + str(i) + " ENB" + str(i) + " Gnd 1", file=open(file, "a"))
    else:
        print("Venb" + str(i) + " ENB" + str(i) + " Gnd  PWL 0 1 '(TpEn-1p)' 1 'TpEn' 0 1.5n 0 (1.5n+1p) 1", file=open(file, "a"))
 
print("\n", file=open(file, "a"))

for i in range( 1,8+1):
    print("Vpre" + str(i) + " PRE" + str(i) + " Gnd 1", file=open(file, "a"))

print("\n", file=open(file, "a"))

print("Vvdd Vvdd Gnd 1", file=open(file, "a"))
print("Vdd Vdd Gnd 1", file=open(file, "a"))
print("Vgnd Gnd 0 0", file=open(file, "a"))

########################## BITCELL #########################################
print("* Bitcell\n", file=open(file, "a"))
k=1
for i in range( 1, 8+1):
    for j in range( 1, int(ElementosMatriz/8)+1):
        print("X" + str(k) + " NM" + str(k) + " BLB" + str(i) + " WL" + str(j) + " Vdd Gnd BC", file=open(file, "a"))
        print("Vtest" + str(k) + " BL" + str(i) + " NM" + str(k) + " 0\n", file=open(file, "a"))
        k += 1

print("\n\n* Write Driver\n", file=open(file, "a"))

for i in range( 1,8+1):
    print("X" + str(i + ElementosMatriz) + " WD" + str(i) + " BL" + str(i) + " EN" + str(i) + " ENB" + str(i) + " Vdd Gnd TI" , file=open(file, "a"))

print("\n", file=open(file, "a"))

for i in range( 1,8+1):
    print("X" + str(int(i + ElementosMatriz+ElementosMatriz/8)) + " WDB" + str(i) + " BLB" + str(i) + " EN" + str(i) + " ENB" + str(i) + " Vdd Gnd TI" , file=open(file, "a"))

print("\n\n* Pre charge\n", file=open(file, "a"))

for i in range( 1, 8+1):
    print("X" + str(int(i + ElementosMatriz+ElementosMatriz/4)) + " BL" + str(i) + " BLB" + str(i) + " PRE" + str(i) + " Vdd PC" , file=open(file, "a"))


print("\n\n* Bitlines Capacitance\n", file=open(file, "a"))

for i in range( 1,8+1):
    print("Cbl" + str(i) + " BL" + str(i) + " Gnd 'cap'" , file=open(file, "a"))
for i in range( 1,8+1):
    print("Cblb" + str(i) + " BLB" + str(i) + " Gnd 'cap'" , file=open(file, "a"))

print("\n\n.TRAN 1p 10n\n\n.option rawfmt=\"psfbin\" ", file=open(file, "a"))

print("\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i == int((ElementosMatriz/16)*7):
        print(".IC V(X" + str(i) + ".Q)=0 V(X" + str(i) + ".QB)=1 V(BL" + str(4) + ")=1 V(BLB"+ str(4) + ")=1", file=open(file, "a"))
