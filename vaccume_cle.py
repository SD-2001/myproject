import time
class Room:
	Roomname = ""
	update = ""
	Robo = False
	def __init__(self, name):
		self.Roomname = name
	def room_con(self):
		print("[ Room "+self.Roomname +" , "+self.update + " ]")


def Execute(room1, room2):
	cost = 0
	while(True):

		if((room1.update == "clean") and (room2.update == "clean")):
			print("\n\n #-----------------------------#")
			print("Both the Rooms are clean")
			print("Total Cost = ", cost)
			print("\n #-----------------------------#\n\n")
			return
			
		elif(room1.Robo and room1.update == "dirty"):
			action = "Suck"
			room1.update = "clean"
			print("\n Action = " + action + "\t", end = "")
			room1.room_con()
			cost += 1
			
		elif(room1.Robo and room1.update == "clean"):
			action = "Right"
			room1.Robo = False
			room2.Robo = True
			cost += 1
			print("\n Action = " + action + "\t", end = "")
			room1.room_con()

		elif(room2.Robo and room2.update == "clean"):
			action = "left"
			room2.Robo = False
			room1.Robo = True
			cost += 1
			print("\n Action = " + action + "\t", end = "")
			room2.room_con()
			
			
		elif(room2.Robo and room2.update == "dirty"):
			action = "Suck"
			room2.update = "clean"
			#room.update = "clean"
			print("\n Action = " + action + "\t", end = "")
			room2.room_con()
			cost += 1




A = Room("A")
B = Room("B")

Ua = input("Please Enter Update A : ")
A.update = Ua

Ub = input("Enter update of Room B : ")
B.update = Ub

Robo = input("Enter In Which Room ROBOT is present : ")

if(Robo == "A" or Robo == "a"):
	A.Robo = True
elif(Robo == "B" or Robo == "b"):
	B.Robo = True

A.room_con()
B.room_con()



Execute(A, B)


A.room_con()
B.room_con()
