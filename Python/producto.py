q = 1
while q == 1:
	print("\nPRODUCTO\n")
	n=int(input("TABLA PARA EL NÚMERO: "))
	print(f"La tabla del número {n}\n")
	array = range(1,11)
	for i in range(10):
		print(str(n) + "×" + str(array[i]) + "=" + str(array[i]*n))
	print("\nFinal")
	answer=input("¿Continuar? (S/N) ")
	if answer == 'S' or answer == 's':
		{}
	elif answer == 'SI' or answer == 'Si' or answer == 'si':
		{}
	else:
		q=0
