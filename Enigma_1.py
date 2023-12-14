#!/usr/bin/env python3


Rotors = '''
INPUT 	A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W	X 	Y 	Z
Rotor I 	E 	K 	M 	F 	L 	G 	D 	Q 	V 	Z 	N 	T	O 	W 	Y 	H 	X 	U 	S 	P 	A 	I 	B	R 	C 	J
Rotor II 	A 	J 	D 	K 	S 	I 	R 	U 	X 	B 	L 	H	W 	T 	M 	C 	Q 	G 	Z 	N 	P 	Y 	F	V 	O 	E
Rotor III 	B 	D 	F 	H 	J 	L 	C 	P 	R 	T 	X 	V	Z 	N 	Y 	E 	I 	W 	G 	A 	K 	M 	U	S 	Q 	O
Rotor IV 	E 	S 	O 	V 	P 	Z 	J 	A 	Y 	Q 	U 	I	R 	H 	X 	L 	N 	F 	T 	G 	K 	D 	C	M 	W 	B
Rotor V 	V 	Z 	B 	R 	G 	I 	T 	Y 	U 	P 	S 	D	N 	H 	L 	X 	A 	W 	M 	J 	Q 	O 	F	E 	C 	K
Rotor VI 	J 	P 	G 	V 	O 	U 	M 	F 	Y 	Q 	B 	E	N 	H 	Z 	R 	D 	K 	A 	S 	X 	L 	I	C 	T 	W
Rotor VII 	N 	Z 	J 	H 	G 	R 	C 	X 	M 	Y 	S 	W	B 	O 	U 	F 	A 	I 	V 	L 	P 	E 	K	Q 	D 	T
Rotor VIII 	F 	K 	Q 	H 	T 	L 	X 	O 	C 	B 	J 	S	P 	D 	Z 	R 	A 	M 	E 	W 	N 	I 	U	Y 	G 	V
Beta rotor 	L 	E 	Y 	J 	V 	C 	N 	I 	X 	W 	P 	B	Q 	M 	D 	R 	T 	A 	K 	Z 	G 	F 	U	H 	O 	S
Gamma rotor 	F 	S 	O 	K 	A 	N 	U 	E 	R 	H 	M 	B	T 	I 	Y 	C 	W 	L 	Q 	P 	Z 	X 	V	G 	J 	D
'''


Rotors_list = []
for i in range(0, len(Rotors.split('\n'))):
    if (Rotors.split('\n')[i] != ''):
        Rotors_list.append(Rotors.split('\n')[i].replace(' ','').split('\t'))
        
Rotors_dict_indexed = {}
for i in range (0,len(Rotors_list)):
    res = {Rotors_list[0][1:][j]: Rotors_list[i][1:][j] for j in range(len(Rotors_list[0][1:]))}
    Rotors_dict_indexed[i] = res

def rotor(symbol, n, reverse=False):
    line = ''
    if (reverse):
        for letter in symbol.replace(' ',''):
            line += {v:k  for k,v in Rotors_dict_indexed[n].items()}[letter]
    else:
        for letter in symbol.replace(' ',''):
            line += Rotors_dict_indexed[n][letter]
    return line