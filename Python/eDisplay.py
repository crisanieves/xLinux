d=(input("Tamaño de la pantalla: "))			
a=6.4; b=(1/2.16)
c=a**2/(1+(b**2)); c=c**(0.5)
print("\nHeight: " + str(c) + " pulgadas\n")
print("Height: " + str(2.54*c) + " centimetros\n")
print("Width: " + str(b*(2.54*c)) + " centimetros\n")


print("—CRISTIAN ES UN GENIO") if c >= 2	else print("—DEFINITIVAMENTE, CRISTIAN ES UN GENIO")



if c>=2:
	print("—SÍ. ÉL ES UN GENIO")
else:
	print("—DEFINITIVAMENTE, ES UN GENIO")



