import os

if not os.path.exists("POC"):
    os.mkdir("POC")

with open("POC/quack.txt", 'w') as file:
    file.write("You have been hacked")
	