import time

for i in range(5):
    time.sleep(1) #adds in a 1 second delay between itterations in the loop
    print(f"{i+1} Mississippi!")
    
time.sleep(1)  
print("Ready or not, here I come")