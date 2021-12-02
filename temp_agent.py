class Room:
	room_name = ""
	temp = 0
	isrobo = False
	def __init__(self, name):
		self.room_name = name
	def room_info(self):
		print("\n[ Room "+self.room_name +" , ",self.temp, " ]")
	






def Run(room1, room2):
	cost = 0
	while(True):
		if((room1.temp <= 45) and (room2.temp <= 45)):
			print("\n\n #-----------------------------#")
			print("The Temp of both room are mainted")
			print("Total Cost = ", cost)
			print("\n #-----------------------------#\n\n")
			return
			
		elif(room1.isrobo and room1.temp > 45):
			action = "On"
			room1.temp = 45
			print("\n Action = " + action + "\t", end = "")
			room1.room_info()
			cost += 1
			
		elif(room1.isrobo and room1.temp <= 45):
			action = "Right"
			room1.isrobo = False
			room2.isrobo = True
			cost += 1
			print("\n Action = " + action + "\t", end = "")
			room1.room_info()

		elif(room2.isrobo and room2.temp <= 45):
			action = "left"
			room2.isrobo = False
			room1.isrobo = True
			cost += 1
			print("\n Action = " + action + "\t", end = "")
			room2.room_info()

		elif(room2.isrobo and room2.temp > 45):
			action = "on"
			room2.temp = 45
			print("\n Action = " + action + "\t", end = "")
			room2.room_info()
			cost += 1


A = Room("A")
B = Room("B")
sa = int(input("Enter temp of Room A : "))
A.temp = sa

sb = int(input("Enter temp of Room B : "))
B.temp = sb


robo = input("In Which Room ROBOT is present : ")
if(robo == "A" or robo == "a"):
	A.isrobo = True
elif(robo == "B" or robo == "b"):
	B.isrobo = True


A.room_info()
B.room_info()

Run(A, B)

A.room_info()
B.room_info()

