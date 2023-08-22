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

robot.sendline("4")
robot.expect('.*')
robot.sendline("go")
robot.expect('.*')
robot.sendline("dive")
robot.expect('.*')
robot.sendline("dive")
robot.expect('.*')
robot.sendline("back")
robot.expect('.*')
robot.sendline("pull")
robot.expect('.*')
robot.sendline("back")
robot.expect('.*')
robot.sendline("back")
robot.expect('.*')
robot.sendline("go")
robot.expect('.*')
robot.sendline("wave")
robot.expect('.*')
robot.sendline("back")
robot.expect('.*')
robot.sendline("back")
robot.expect('.*')
robot.sendline("thrnxxtzy")
robot.expect('.*')
robot.sendline("read")
robot.expect('.*')
robot.sendline("the_magic_of_wand")
robot.expect('.*')
robot.sendline("c")
robot.expect('.*')
robot.sendline("read")
robot.expect('.*')

'''
go
dive
dive
back
pull
back
back
go
wave
bacl
back
thrnxxtzy
read
the_magic_of_wand
c
read

'''

f = open("plaintexts1.txt", 'r')
f1= open("ciphertextsmajor1.txt",'w')

cnt = 0;

for line in f.readlines():
	robot.sendline(line)
	robot.expect("Slowly, a new text starts.*")
	#print(robot.before)
	print('=======================================')
	#print(robot.after)
	f1.writelines(str(robot.after)[73:89]+"\n")
	robot.sendline("c")
	robot.expect('The text in the screen vanishes!')
	cnt+=1;
	print(cnt);
f.close()
f1.close()

f = open("plaintexts2.txt", 'r')
f1= open("ciphertextsmajor2.txt",'w')


for line in f.readlines():
	robot.sendline(line)
	robot.expect("Slowly, a new text starts.*")
	#print(robot.before)
	print('=======================================')
	#print(robot.after)
	f1.writelines(str(robot.after)[73:89]+"\n")
	robot.sendline("c")
	robot.expect('The text in the screen vanishes!')
	cnt+=1;
	print(cnt);
robot.close()
f.close()
f1.close()
