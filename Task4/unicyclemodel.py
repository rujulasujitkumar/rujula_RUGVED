import math
import matplotlib.pyplot as plt
x=0
y=0
theta=0
dt=0.1
n=int(input("enter no. of commands"))
commands=[]
for i in range(n):
    cmd=input("Enter command like (vel omega duration):")
    commands.append(cmd)

x_list=[x]
y_list=[y]

for command in commands:
    parts=command.split()
    v=float(parts[0])
    omega=float(parts[1])
    duration=float(parts[2])

    steps=int(duration/dt)

    for i in range(steps):
        x=x+v*math.cos(theta)*dt
        y=y+v*math.sin(theta)*dt
        theta=theta+omega*dt
        
        x_list.append(x)
        y_list.append(y)

plt.plot(x_list, y_list)
plt.title("Robot Curved Path Tracker")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()