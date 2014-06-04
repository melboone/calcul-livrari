print "Calculeza cati bani pe zile sau pe saptamani"

def alege():
	bani = 7	
	alegere = int(raw_input("alege 1 pentru calcul pe zile si 2 pentru luni: "))

	if alegere == 1:
	    zile = int(raw_input("numar zile: "))
	    livrari = int(raw_input("Numarul livrarilor in medie pe zi: "))
	    print "\n%s zile x %s livrari/zi = $%s" % (zile, livrari, bani*zile*livrari)
	    exit("\n Spor")

	elif alegere == 2:
	    luni = int(raw_input("numar luni: "))
	    livrari = int(raw_input("Numarul livrarilor in medie pe zi: "))
	    print "\n%s luni x %s livrari/zi = $%s" % (luni, livrari, 21.65*luni*bani*livrari) 
	    exit("\n Bafta")

	else:
	    print "nu ai ales nici 1 nici 2"
	    exit("am inchis programul")

alege()