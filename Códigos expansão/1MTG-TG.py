

file = "C:/Users/Bruno/Desktop/IC-2021/Python/1MTJ-TG.txt"
f = open(file, "w")

#ElementosMatriz = int(input("Quantos elementos vai ter a matriz?"))
ElementosMatriz = 512

print("* Crossbar one bit\n\nsimulator lang=spice\n\n.include '45nm_LP.pm'\n.include 'MTJT.spi'\n.include 'TRANSGATE.spi'\n\n", file=open(file, "a"))
print(".param cap = 1.5f\n\n.param Vvdd = 1.6\n\n.param Vgnd = 0\n\n.param Vread = 1\n\n.param TpWrite = 0.7n\n.param TpRead = 0.3n\n.param TpPulse = 0.9n\n\n", file=open(file, "a"))

if(pow(ElementosMatriz, 0.5) <= 8):
    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        if i != int(pow(ElementosMatriz,0.5)/2):
            print("Vwl" + str(i) + " WL" + str(i) + "T Gnd PWL 0 'Vgnd'", file=open(file, "a"))
        else:
            print("Vwl" + str(i) + " WL" + str(i) + "T Gnd PWL 0 'Vgnd' 'TpPulse-1p' 'Vgnd' 'TpPulse' 'Vvdd' '5n' 'Vvdd' '5n+1p' 'Vgnd' '8n+TpRead' 'Vgnd' '8n+TpRead+1p' 'Vread' '9n-1p' 'Vread' '9n' 'Vgnd'", file=open(file, "a"))
    
    print("\n", file=open(file, "a"))

    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        if i != int(pow(ElementosMatriz,0.5)/2):
            print("Vbl" + str(i) + " BL" + str(i) + "T Gnd PWL 0 'Vgnd'", file=open(file, "a"))
        else:
            print("Vbl" + str(i) + " BL" + str(i) + "T Gnd PWL 0 'Vgnd' '5n+TpWrite-1p' 'Vgnd' '5n+TpWrite' 'Vvdd' '7n-1p' 'Vvdd' '7n' 'Vgnd'", file=open(file, "a"))
    
    print("\n", file=open(file, "a"))

    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        if i != int(pow(ElementosMatriz,0.5)/2):
            print("Vbl" + str(i) + "en ENBl" + str(i) + " Gnd PWL 0 'Vgnd'", file=open(file, "a"))
        else:
            print("Vbl" + str(i) + "en ENBl" + str(i) + " Gnd PWL 0 'Vgnd' 'TpPulse-1p' 'Vgnd' 'TpPulse' 'Vvdd' '5n' 'Vvdd' '5n+1p' 'Vgnd' '5n+TpWrite-1p' 'Vgnd' '5n+TpWrite' 'Vvdd' '7n-1p' 'Vvdd' '7n' 'Vgnd' '8n+TpRead-1p' 'Vgnd' '8n+TpRead' 'Vvdd' '9n-1p' 'Vvdd' '9n' 'Vgnd'", file=open(file, "a"))
    
    print("\n\nVvdd Vdd Gnd 'Vvdd'\n\n", file=open(file, "a"))


    print("* Bitcell\n", file=open(file, "a"))
    k=1
    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        for j in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
            print("X" + str(k) + " WL" + str(i) + " NM" + str(k) + " MTJT", file=open(file, "a"))
            print("Vtest" + str(k) + " BL" + str(j) + " NM" + str(k) + " 0\n", file=open(file, "a"))
            k += 1
    
    print("\n\n* Tristate\n", file=open(file, "a"))

    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        print("X" + str(i + ElementosMatriz+1) + " WL" + str(i) + "T WL" + str(i) + " ENWl" + str(i) + " Vdd Gnd TG" , file=open(file, "a"))
        print("X" + str(i + ElementosMatriz+int(pow(ElementosMatriz,0.5))+1) + " BL" + str(i) + "T BL" + str(i) + " ENBl" + str(i) + " Vdd Gnd TG" , file=open(file, "a"))
    
    print("\n\n* Bitlines Capacitance\n", file=open(file, "a"))
    
    for i in range( 1, int(pow(ElementosMatriz,0.5)) + 1):
        print("Cbl" + str(i + ElementosMatriz + (2*int(pow(ElementosMatriz,0.5))) +1) + " BL" + str(i) + " Gnd 'cap'" , file=open(file, "a"))
    
    print("\n\n.TRAN 1p 10n\n\n.option rawfmt=\"psfbin\" ", file=open(file, "a"))
############################################################# WORDS DE  8  BITS ######################################################################   
else:
    for i in range( 1, int(ElementosMatriz/8)+1):
        if i != int((int(ElementosMatriz/8)+1)/2):
            print("Vwl" + str(i) + " WL" + str(i) + "T Gnd PWL 0 'Vgnd'", file=open(file, "a"))
        else:
            print("Vwl" + str(i) + " WL" + str(i) + "T Gnd PWL 0 'Vgnd' 'TpPulse-1p' 'Vgnd' 'TpPulse' 'Vvdd' '5n' 'Vvdd' '5n+1p' 'Vgnd' '8n+TpRead' 'Vgnd' '8n+TpRead+1p' 'Vread' '9n-1p' 'Vread' '9n' 'Vgnd'", file=open(file, "a"))
       
    print("\n", file=open(file, "a"))

    for i in range( 1,8+1):
        if i != int(8/2):
            print("Vbl" + str(i) + " BL" + str(i) + "T Gnd PWL 0 'Vgnd'", file=open(file, "a"))
        else:
            print("Vbl" + str(i) + " BL" + str(i) + "T Gnd PWL 0 'Vgnd' '5n+TpWrite-1p' 'Vgnd' '5n+TpWrite' 'Vvdd' '7n-1p' 'Vvdd' '7n' 'Vgnd'", file=open(file, "a"))
    
    print("\n", file=open(file, "a"))

    for i in range( 1, int(ElementosMatriz/8)+1):
        if i != int((int(ElementosMatriz/8)+1)/2):
            print("Vwl" + str(i) + "en ENWl" + str(i) + " Gnd PWL 0 'Vgnd'", file=open(file, "a"))
        else:
            print("Vwl" + str(i) + "en ENWl" + str(i) + " Gnd PWL 0 'Vgnd' 'TpPulse-1p' 'Vgnd' 'TpPulse' 'Vvdd' '5n' 'Vvdd' '5n+1p' 'Vgnd' '5n+TpWrite-1p' 'Vgnd' '5n+TpWrite' 'Vvdd' '7n-1p' 'Vvdd' '7n' 'Vgnd' '8n+TpRead-1p' 'Vgnd' '8n+TpRead' 'Vvdd' '9n-1p' 'Vvdd' '9n' 'Vgnd'", file=open(file, "a"))
      
    print("\n", file=open(file, "a"))

    for i in range( 1,8+1):
        if i != int(8/2):
            print("Vbl" + str(i) + "en ENBl" + str(i) + " Gnd PWL 0 'Vgnd'", file=open(file, "a"))
        else:
            print("Vbl" + str(i) + "en ENBl" + str(i) + " Gnd PWL 0 'Vgnd' 'TpPulse-1p' 'Vgnd' 'TpPulse' 'Vvdd' '5n' 'Vvdd' '5n+1p' 'Vgnd' '5n+TpWrite-1p' 'Vgnd' '5n+TpWrite' 'Vvdd' '7n-1p' 'Vvdd' '7n' 'Vgnd' '8n+TpRead-1p' 'Vgnd' '8n+TpRead' 'Vvdd' '9n-1p' 'Vvdd' '9n' 'Vgnd'", file=open(file, "a"))
    
    print("\n\nVvdd Vdd Gnd 'Vvdd'\n\n", file=open(file, "a"))


    print("* Bitcell\n", file=open(file, "a"))
    k=1
    for i in range( 1, 8+1):
        for j in range( 1, int(ElementosMatriz/8)+1):
            print("X" + str(k) + " WL" + str(j) + " NM" + str(k) + " MTJT", file=open(file, "a"))
            print("Vtest" + str(k) + " BL" + str(i) + " NM" + str(k) + " 0\n", file=open(file, "a"))
            k += 1
    
    print("\n\n* Tristate\n", file=open(file, "a"))

    for i in range( 1, int(ElementosMatriz/8)+1):
        print("X" + str(i + ElementosMatriz+1) + " WL" + str(i) + "T WL" + str(i) + " ENWl" + str(i) + " Vdd Gnd TG" , file=open(file, "a"))
        
    for i in range( 1, 8+1):
        print("X" + str(i + ElementosMatriz+65+1) + " BL" + str(i) + "T BL" + str(i) + " ENBl" + str(i) + " Vdd Gnd TG" , file=open(file, "a"))
    
    print("\n\n* Bitlines Capacitance\n", file=open(file, "a"))
    
    for i in range( 1, 8+1):
        print("Cbl" + str(i + ElementosMatriz + (2*int(ElementosMatriz/8)) +1) + " BL" + str(i) + " Gnd 'cap'" , file=open(file, "a"))
    
    print("\n\n.TRAN 1p 10n\n\n.option rawfmt=\"psfbin\" ", file=open(file, "a"))
