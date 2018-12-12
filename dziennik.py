#Wirtualny Dziennik Ucznia/Klasy

klasa = {}

i = 0 #zmienna, która przyda mi się do tworzenia keys dla uczniów 

def printDziennik(): #drukowanie dziennika
	for key, value in klasa.items():
		print(key, value)

def addStudent(): #dodawanie ucznia

		flag = ""

		while flag != "n":

			i += 1 #przy każdym jednym przejściu przez pętlę numer rośnie...

			student = {}

			imie = input("Wpisz imię ucznia:\n")

			nazwisko = input("Wpisz nazwisko ucznia\n")

			student["oceny"] = []

			student["name"] = imie

			student["surname"] = nazwisko

			str(i) #...potem konwertuję go na string

			klasa["Nr.{}".format(i)] = student #...aby mógł utworzyć numerek w dzienniku <3 

			flag = input("Chcesz dodać kolejnego ucznia? [t/n]\n")
		printDziennik()

def ocena(): #dodawanie oceny
	dodajOcene = input("Któremu uczniowi chcesz wpisać oceny [Wpisz 'Nr.' + jego numer z dziennika]\n")
	flag = ""
	while flag != "n":
		klasa[dodajOcene]["oceny"].append(int(input("Wpisz ocenę z danego przedmiotu:\n"))) #A tak się używa metody typów danych zagnieżdżonych w słownikach. BARDZO INTUICYJNIE!!!
		flag = input("Dodać inną ocenę? [t/n]")
	printDziennik()

def sredniaU(): #średnia ucznia
	obliczSrednia = ""
	while obliczSrednia != "end":
		obliczSrednia = input("Wpisz 'Nr.' + numer z dziennika osoby, której chcesz obliczyć średnią: \n [jeśli chcesz zakończyć obliczanie średnich wpisz 'end']")
		sredniaUczen = sum(klasa[obliczSrednia]["oceny"]) / len(klasa[obliczSrednia]["oceny"])
		klasa[obliczSrednia]["avgrade"] = sredniaUczen
		print("Średnia ucznia/uczennicy {}: ".format(obliczSrednia) + str(sredniaUczen))
	printDziennik()

def sredniaK(): #średnia klasy
	sredniaKlasy = 0
	for uczniowie in klasa.values(): #pętla przez uczniów
		for oceny in uczniowie.values(): #pętla przez wartości w uczniach
			if type(oceny) is int or float: #sprawdza, czy wartość to int (np. 4.0) lub float (np. 3.5)
				sredniaKlasy = sum(oceny) / len(klasa)
				print(sredniaKlasy)
			else:
				None

def start():

	enterInput = input("Co chcesz zrobić?:\nDodaj ucznia [dodaj]\nWpisz oceny uczniom [oceny]\nOblicz średnią ucznia [srednia1]\nOblicz średnią klasy [srednia2]\n")

	while enterInput != "koniec psot":
		if enterInput == "dodaj":
			addStudent()
			start()
		if enterInput == "oceny":
			ocena()
			start()
		if enterInput == "srednia1":
			sredniaU()
			start()
		if enterInput == "srednia2":
			sredniaK()
			start() # Jak chcę obliczyć średnią klasy, to faktycznie ją wyrzuca, ale zaraz potem jest jakiś niezrozumiały typeerror właśnie w tych rejonach...
start()