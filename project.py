import aiml

#print("enter LOAD for basic chat")
#print("GUESSNAME for game which includes guessing enter start to start")
#print("MONTHLYDIARY to store and retrieve your experiences in a month enter start to start");
#print("JOKEPLEASE to listen to a joke enter start to start")
#print("BATTLEDOME to play battle enter start to start")

message = input("enter value>>>")
kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("RESPOND")

while True:
    message = input("enter>>")
    if message == "quit":
        exit()
    else:
        print(kernel.respond(message))
