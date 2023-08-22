f = open("ciphertexts.txt", 'r')
f1 = open("cipher_clean.txt", 'w')
cnt = 0
s = ""
for i in f.readlines():
	x = i.split()
	if cnt == 128:
		s = s + "\n"
		f1.writelines(s)
		cnt = 0
		s = ""
		
	s = s + " " + x[0] 
	cnt += 1

	print(cnt)
	
s = s + "\n"
f1.writelines(s)
f.close()
f1.close()
	
