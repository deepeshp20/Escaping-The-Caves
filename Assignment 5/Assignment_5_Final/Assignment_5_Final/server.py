import pexpect

robot = pexpect.spawn('ssh student@172.27.26.188')
robot.expect('student@172.27.26.188\'s password:')
robot.sendline('cs641')
robot.expect('Enter your group name: ') 
robot.sendline("team_9")

robot.expect('Enter password: ')
robot.sendline("team9")

#robot.expect('\r\n\r\n\r\nYou have solved 4 levels so far.\r\nLevel you want to start at: ', timeout=50)

robot.expect('at: ', timeout=50)

robot.sendline("5")
robot.expect('.*')
robot.sendline("go")
robot.expect('.*')
robot.sendline("wave")
robot.expect('.*')
robot.sendline("dive")
robot.expect('.*')
robot.sendline("go")
robot.expect('.*')
robot.sendline("read")
robot.expect('.*')


f = open("plaintexts.txt", 'r')
f1= open("ciphertexts.txt",'w')

text = []

for i in f.readlines():
	s = list(i.split())
	text = text + s

c = 0
for line in text:
	robot.sendline(line)
	robot.expect("Slowly, a new text starts.*")
	#print(robot.before)
	#print('=======================================')
	#print(robot.after)
	dummy = str(robot.after)[73:89]
	print(str(c) + " " + dummy)
	c+=1
	f1.writelines(dummy +"\n")
	robot.sendline("c")
	robot.expect('The text in the screen vanishes!')

robot.close()
f.close()
f1.close()

