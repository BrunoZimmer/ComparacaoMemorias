
""" 
*Power

alias measurement PowerRd{
	run tran (stop = 10n)

	real chargeIRd = avg(integ(sig=I(Vtest6), from=8.1n, to=8.4n ))

	export real EnergyRead = chargeIRd*Vvdd

}

alias measurement LeakRd{
	run tran (stop = 10n)

	real chargeIRd1 = avg(integ(sig=I(Vtest1), from=8.1n, to=8.4n ))
	real chargeIRd2 = avg(integ(sig=I(Vtest2), from=8.1n, to=8.4n ))
	real chargeIRd3 = avg(integ(sig=I(Vtest3), from=8.1n, to=8.4n ))
	real chargeIRd4 = avg(integ(sig=I(Vtest4), from=8.1n, to=8.4n ))
	real chargeIRd5 = avg(integ(sig=I(Vtest5), from=8.1n, to=8.4n ))
	real chargeIRd7 = avg(integ(sig=I(Vtest7), from=8.1n, to=8.4n ))
	real chargeIRd8 = avg(integ(sig=I(Vtest8), from=8.1n, to=8.4n ))
	real chargeIRd9 = avg(integ(sig=I(Vtest9), from=8.1n, to=8.4n ))
	real chargeIRd10 = avg(integ(sig=I(Vtest10), from=8.1n, to=8.4n ))
	real chargeIRd11 = avg(integ(sig=I(Vtest11), from=8.1n, to=8.4n ))
	real chargeIRd12 = avg(integ(sig=I(Vtest12), from=8.1n, to=8.4n ))
	real chargeIRd13 = avg(integ(sig=I(Vtest13), from=8.1n, to=8.4n ))
	real chargeIRd14 = avg(integ(sig=I(Vtest14), from=8.1n, to=8.4n ))
	real chargeIRd15 = avg(integ(sig=I(Vtest15), from=8.1n, to=8.4n ))
	real chargeIRd16 = avg(integ(sig=I(Vtest16), from=8.1n, to=8.4n ))

	export real EnergyLeakRead = (chargeIRd2 + chargeIRd3 + chargeIRd4 + chargeIRd5 + chargeIRd1 + chargeIRd7 + chargeIRd8 + chargeIRd9 + chargeIRd10 + chargeIRd11 + chargeIRd12 + chargeIRd13 + chargeIRd14 + chargeIRd15 + chargeIRd16)*Vvdd

}

alias measurement PowerWrt{
	run tran (stop = 10n)

	real chargeIWr = avg(integ(sig=I(Vtest6), from=5.9n, to=6.1n ))

	export real EnergyWrite = chargeIWr*Vvdd
}
alias measurement LeakWrt{
	run tran (stop = 10n)

	real chargeIWrt1 = avg(integ(sig=I(Vtest1), from=5.9n, to=6.1n ))
	real chargeIWrt2 = avg(integ(sig=I(Vtest2), from=5.9n, to=6.1n ))
	real chargeIWrt3 = avg(integ(sig=I(Vtest3), from=5.9n, to=6.1n ))
	real chargeIWrt4 = avg(integ(sig=I(Vtest4), from=5.9n, to=6.1n ))
	real chargeIWrt5 = avg(integ(sig=I(Vtest5), from=5.9n, to=6.1n ))
	real chargeIWrt7 = avg(integ(sig=I(Vtest7), from=5.9n, to=6.1n ))
	real chargeIWrt8 = avg(integ(sig=I(Vtest8), from=5.9n, to=6.1n ))
	real chargeIWrt9 = avg(integ(sig=I(Vtest9), from=5.9n, to=6.1n ))
	real chargeIWrt10 = avg(integ(sig=I(Vtest10), from=5.9n, to=6.1n ))
	real chargeIWrt11 = avg(integ(sig=I(Vtest11), from=5.9n, to=6.1n ))
	real chargeIWrt12 = avg(integ(sig=I(Vtest12), from=5.9n, to=6.1n ))
	real chargeIWrt13 = avg(integ(sig=I(Vtest13), from=5.9n, to=6.1n ))
	real chargeIWrt14 = avg(integ(sig=I(Vtest14), from=5.9n, to=6.1n ))
	real chargeIWrt15 = avg(integ(sig=I(Vtest15), from=5.9n, to=6.1n ))
	real chargeIWrt16 = avg(integ(sig=I(Vtest16), from=5.9n, to=6.1n ))

	export real EnergyLeakWrite = (chargeIWrt2 + chargeIWrt3 + chargeIWrt4 + chargeIWrt5 + chargeIWrt1 + chargeIWrt7 + chargeIWrt8 + chargeIWrt9 + chargeIWrt10 + chargeIWrt11 + chargeIWrt12 + chargeIWrt13 + chargeIWrt14 + chargeIWrt15 + chargeIWrt16)*Vvdd
}
#########################################################################################

alias measurement TmpRead{
	run tran (stop = 10n)
	export real CurBL = abs(I(Vtest6)@8.3n)

	export real TpRd = 0.3n - TpRead

}
search TpRead from binary(start=0.1n, stop=0.3n, tol=1f){
	run TmpRead
}while (TmpRead->CurBL > 0.00042)

alias measurement TmpRead{
	run tran (stop = 10n)
	export real CurBL = abs(I(Vtest6)@8.3n)

	export real TpRd = 0.3n - TpRead

}
search TpRead from binary(start=0.1n, stop=0.3n, tol=1f){
	run TmpRead
}while (TmpRead->CurBL > 0.00042)


alias measurement TmpWrite{
	run tran (stop = 8n)
	export real CurX = abs(I(Vtest6)@6n)

	export real TpWrt = 1n - TpWrite

}
search TpWrite from binary(start=0.7n, stop=0.9n, tol=1f){
	run TmpWrite
}while (TmpWrite->CurX < 0.00265 && TmpWrite->CurX > 0.0025)

run PowerRd
run LeakRd

run PowerWrt
run LeakWrt

print fmt ("\n****Results of 16Bits:****\n\n") to="Results.csv"
print fmt("Read Latency/%-15e\n", TmpRead->TpRd) addto="Results.csv"
print fmt("Write Latency/%-15e\n", TmpWrite->TpWrt) addto="Results.csv"
print fmt("Read Energy/%-15e\n", PowerRd->EnergyRead) addto="Results.csv"
print fmt("Write Energy/%-15e\n", PowerWrt->EnergyWrite) addto="Results.csv"
print fmt("Leakage Energy Read/%-15e\n", LeakRd->EnergyLeakRead) addto="Results.csv"
print fmt("Leakage Energy Write/%-15e\n", LeakWrt->EnergyLeakWrite) addto="Results.csv"
 """

file = "C:/Users/Bruno/Desktop/IC-2021/Python/Results1T1M.txt"
f = open(file, "w")

ElementosMatriz =256

print("* Power - "+ str(pow(ElementosMatriz,0.5) + 1), file=open(file, "a"))

################################# Energy Read ##################################################
print("\n\nalias measurement PowerRd{\nrun tran (stop = 10n)\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i == int((ElementosMatriz/16)*7):
        print("real chargeIRd" + str(i) + " = avg(integ(sig=I(Vtest" + str(i) + "), from=8.1n, to=8.4n ))", file=open(file, "a"))
        print("\nexport real EnergyRead = (chargeIRd" + str(i) + "*Vvdd)\n}\n\n", end = '', file=open(file, "a"))

################################# Energy Write ##################################################
print("\n\nalias measurement PowerWrt{\nrun tran (stop = 10n)\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i == int((ElementosMatriz/16)*7):
        print("real chargeIWr" + str(i) + " = avg(integ(sig=I(Vtest" + str(i) + "), from=5.9n, to=6.1n ))", file=open(file, "a"))
        print("\nexport real EnergyWrite = (chargeIWr" + str(i) + "*Vvdd)\n}\n\n", end = '', file=open(file, "a"))


################################# Leakage Read ##################################################
print("\n\nalias measurement LeakRd{\nrun tran (stop = 10n)\n", file=open(file, "a"))
for i in range( 1, ElementosMatriz + 1):
    if i != int(8*(ElementosMatriz/16-1)-24):
        print("real chargeIRd" + str(i) + " = avg(integ(sig=I(Vtest" + str(i) + "), from=8.1n, to=8.4n ))", file=open(file, "a"))


print("\nexport real EnergyLeakRead = (chargeIRd1", end = '', file=open(file, "a"))
for i in range( 2, ElementosMatriz + 1):
    if i != int(8*(ElementosMatriz/16-1)-24):
        print(" + chargeIRd" + str(i), end = '', file=open(file, "a"))

print(")*Vvdd\n\n}", file=open(file, "a"))
################################# Leakage Write ##################################################
print("\n\nalias measurement LeakWrt{\nrun tran (stop = 10n)\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i != int(8*(ElementosMatriz/16-1)-24):
        print("real chargeIWrt" + str(i) + " = avg(integ(sig=I(Vtest" + str(i) + "), from=5.9n, to=6.1n ))", file=open(file, "a"))
        
print("\nexport real EnergyLeakWrite = (chargeIWrt1", end = '', file=open(file, "a"))
for i in range( 2, ElementosMatriz + 1):
    if i != int(8*(ElementosMatriz/16-1)-24):
        print(" + chargeIWrt" + str(i), end = '', file=open(file, "a"))

print(")*Vvdd\n}", file=open(file, "a"))

################################# Static Leakage ##################################################
print("\n\nalias measurement LeakStat{\nrun dc (oppoint='logfile)\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i != int(8*(ElementosMatriz/16-1)-24):
        print("real Static" + str(i) + " = I(Vtest" + str(i) + ")", file=open(file, "a"))
        
print("\nexport real TotalStaticLeakage = (Static1", end = '', file=open(file, "a"))
for i in range( 2, ElementosMatriz + 1):
    if i != int(8*(ElementosMatriz/16-1)-24):
        print(" + Static" + str(i), end = '', file=open(file, "a"))

print(")\n}", file=open(file, "a"))

############### Read Latency #################################
print("\n\nalias measurement TmpRead{\nrun tran (stop = 10n)\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i == int((ElementosMatriz/16)*7):
        print("export real CurBL = abs(I(Vtest" + str(i) + ")@8.3n)\n\n", end = '', file=open(file, "a"))

print("export real TpRd = 0.3n-TpRead\n}\n", file=open(file, "a"))


print("search TpRead from binary(start=0.05n, stop=0.2999n, tol=1f){\nrun TmpRead\n}while (TmpRead->CurBL > 0.0004)\n", file=open(file, "a"))


############### Write Latency #################################
print("\n\nalias measurement TmpWrite{\nrun tran (stop = 10n)\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i == int((ElementosMatriz/16)*7):
        print("export real CurX = abs(I(Vtest" + str(i) + ")@6n)\n\n", end = '', file=open(file, "a"))

print("export real TpWrt = 1n - TpWrite\n}\n", file=open(file, "a"))


print("search TpWrite from binary(start=0.7n, stop=0.9n, tol=1f){\nrun TmpWrite\n}while (TmpWrite->CurX < 0.0022 && TmpWrite->CurX > 0.0019)\n", file=open(file, "a"))


########################## Results ###########################

print("\nrun PowerRd\nrun LeakRd\nrun PowerWrt\nrun LeakWrt\nrun LeakStat\n", file=open(file, "a"))

print("\nprint fmt(\"****Results of " + str(ElementosMatriz) + "Bits:****\\n\") to=\"Results.csv\"\n", file=open(file, "a"))
print("print fmt(\"Read Latency/%-15e\\n\", TmpRead->TpRd) addto=\"Results.csv\"", file=open(file, "a"))
print("print fmt(\"Write Latency/%-15e\\n\", TmpWrite->TpWrt) addto=\"Results.csv\"", file=open(file, "a"))
print("print fmt(\"Read Energy/%-15e\\n\", PowerRd->EnergyRead) addto=\"Results.csv\"", file=open(file, "a"))
print("print fmt(\"Write Energy/%-15e\\n\", PowerWrt->EnergyWrite) addto=\"Results.csv\"", file=open(file, "a"))
print("print fmt(\"Leakage Energy Read/%-15e\\n\", LeakRd->EnergyLeakRead) addto=\"Results.csv\"", file=open(file, "a"))
print("print fmt(\"Leakage Energy Write/%-15e\\n\", LeakWrt->EnergyLeakWrite) addto=\"Results.csv\"", file=open(file, "a"))
print("print fmt(\"Static Leakage/%-15e\\n\", LeakStat->TotalStaticLeakage) addto=\"Results.csv\"", file=open(file, "a"))
