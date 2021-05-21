# *MDL code

# alias measurement TmpWL{
# 	run tran (stop = 2.5n)
# 	export real Ten_Q = V(X5.Q)@1.5n
# 	export real Ten_QB = V(X5.QB)@1.5n

# 	export real Tp_wl = TpWl
# 	export real Tp_wrt_btl = 1.5n - TpWl
# }

# alias measurement TmpEn{
# 	run tran (stop = 2.5n)
# 	export real Ten_Q1 = V(BL2)@TmpWL->Tp_wl
# 	export real Ten_QB1 = V(BLB2)@TmpWL->Tp_wl

# 	export real Tp_En = TpEn
# 	export real Tp_contam = TpWl - TpEn

# 	export real Tp_Write_total = Tp_contam + 1.5n - TpWl

# }

# search TpWl from binary(start=1n, stop=1.5n, tol=0.000001n){
# 	run TmpWL
# }while (TmpWL->Ten_Q > 0.95 && TmpWL->Ten_QB < 0.05)

# search TpEn from binary(start=0.6n, stop=(TpWl-2p), tol=0.000001n){
# 	run TmpEn
# }while (TmpEn->Ten_Q1 > 0.95 && TmpEn->Ten_QB1 < 0.05)

################################# Write Results ##################################################

file = "C:/Users/Bruno/Desktop/IC-2021/Python/ResultsWriteSRAM.txt"
f = open(file, "w")

ElementosMatriz = 256


################################# Static Leakage ##################################################
print("\n\nalias measurement LeakStat{\nrun dc (oppoint='logfile)\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i != int((ElementosMatriz/16)*7):
        print("real Static" + str(i) + " = I(Vtest" + str(i) + ")", file=open(file, "a"))
        
print("\nexport real TotalStaticLeakage = (Static1", end = '', file=open(file, "a"))
for i in range( 2, ElementosMatriz + 1):
    if i != int(8*(ElementosMatriz/16-1)-24):
        print(" + Static" + str(i), end = '', file=open(file, "a"))

print(")\n}", file=open(file, "a"))

############### Write Latency #################################
print("\n\nalias measurement TmpWL{\nrun tran (stop = 5n)\n", file=open(file, "a"))

for i in range( 1, ElementosMatriz + 1):
    if i == int((ElementosMatriz/16)*7):
        print("export real Ten_Q = V(X" + str(i) + ".Q)@1.5n\n\n", file=open(file, "a"))
        print("export real Ten_QB = V(X" + str(i) + ".QB)@1.5n\n\n", file=open(file, "a"))

print("export real Tp_wl = TpWl", file=open(file, "a"))
print("export real Tp_wrt_btl = 1.5n - TpWl\n}\n", file=open(file, "a"))


print("\n\nalias measurement TmpEn{\nrun tran (stop = 5n)\n", file=open(file, "a"))

print("export real Ten_Q1 = V(BL4)@TmpWL->Tp_wl", file=open(file, "a"))
print("export real Ten_QB1 = V(BLB4)@TmpWL->Tp_wl", file=open(file, "a"))

print("export real Tp_En = TpEn", file=open(file, "a"))
print("export real Tp_contam = TpWl - TpEn", file=open(file, "a"))
print("export real Tp_Write_total = Tp_contam + 1.5n - TpWl\n}\n", file=open(file, "a"))

print("search TpWl from binary(start=1n, stop=1.5n, tol=1f){", file=open(file, "a"))
print("run TmpWL\n}while (TmpWL->Ten_Q > 0.95 && TmpWL->Ten_QB < 0.05)", file=open(file, "a"))

print("search TpEn from binary(start=0.6n, stop=(TpWl-2p), tol=1f){", file=open(file, "a"))
print("run TmpEn\n}while (TmpEn->Ten_Q1 > 0.95 && TmpEn->Ten_QB1 < 0.05)", file=open(file, "a"))

########################## Results ###########################

print("\nrun LeakStat\n", file=open(file, "a"))


print("\nprint fmt(\"****Results of " + str(ElementosMatriz) + "Bits:****\\n\") to=\"Results.csv\"\n", file=open(file, "a"))
print("print fmt(\"%-15e\\n\", LeakStat->TotalStaticLeakage) addto=\"Results.csv\"", file=open(file, "a"))
print("print fmt(\"%-15e\\n\", TmpEn->Tp_Write_total) addto=\"Results.csv\"", file=open(file, "a"))
