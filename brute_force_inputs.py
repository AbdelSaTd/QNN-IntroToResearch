
l = [(0,1),(1,0),(-1,0),(0,-1)]
for a, b in l:
	for c, d in l:
		i0 = a*c + a*d + b*c + b*d
		i1 = -a*c  + a*d - b*c + b*d
		i2 = a*c + a*d + - b*c + b*d
		i3 = a*c - a*d - b*c + b*d

		print('vector: ' + repr(i0) + ' ' + repr(i1) + ' ' + repr(i2) + ' ' + repr(i3))
		print(i0)
		print(i1)
		print(i2)
		print(i3)

		print('qubits: ' + repr(a) + ' ' + repr(b) + ' ' + repr(c) + ' ' + repr(d))
		print('a= ', a) 
		print('b= ', b)
		print('c= ', c)
		print('d= ', d)
		print(' ------------------------------------------------ ')
