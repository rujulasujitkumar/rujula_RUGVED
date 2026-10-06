import math
import matplotlib.pyplot as plt
x=0
y=0
theta=0
n=int(input("eter no. of commands"))
commands=[]
for i in range(n):
    cmd=input("Enter command in format forward <val>,left <val> and right <val>")
    commands.append(cmd)

x_list=[x]
y_list=[y]
theta_list=[theta] 

for command in commands:
    parts=command.split()
    move=parts[0]
    val=float(parts[1])

    if move=="forward":
        x=x+val*math.cos(math.radians(theta))
        y=y+val*math.sin(math.radians(theta))
        x_list.append(x)
        y_list.append(y)
        theta_list.append(theta) 
    elif move=="left":
        theta=theta+val
        theta_list[-1]=theta
    elif move=="right":
        theta=theta-val
        theta_list[-1]=theta
       


x2_list=[]
y2_list=[]
for t in range(len(theta_list)-1):
    x2_list.append(math.cos(math.radians(theta_list[t])))
    y2_list.append(math.sin(math.radians(theta_list[t])))  

plt.plot(x_list,y_list)
plt.quiver(x_list[:-1],y_list[:-1],x2_list,y2_list,color='gray') 
plt.title("Robot Path Tracker")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()