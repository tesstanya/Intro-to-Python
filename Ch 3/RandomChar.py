import time

rand = time.time()

hour = int((rand // 3600) % 24) #Finds the current minute

uppercase = chr(hour+65)

print("Random uppercase letter from the current hour is:", uppercase)