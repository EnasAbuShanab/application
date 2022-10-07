print ("hello")
#this is a counting system
import webbrowser
import time
xx= 0
while (xx<9):
  print (" the count is:\n",xx) # \n is to start a new line before it
  xx=xx+1
print ("Good luck")

print("\n")

e,f,g= 1,3.5, "abc"
print(e,f,g)

print("wael \n al \t qawasmi")

print("\n")

var1=100
var2=200
if var1 < var2:
    print (str(var1)+" is smaller than " + str(var2))

print("\n")

if var1 < var2:
    print (str(var1)+" is smaller than " + str(var2))
else:
    print (str(var1)+" is greater than " + str(var2))
print("\n")

if 2 > 3:
  x=5
elif 5>4:
  x=2
print (x)

print("\n")
try:
  fh= open ("testfile","w")
  fh.write("this is my test file for you")
except IOError:
  print("Error: can\'t open file")
else:
  print(" written content in the file successfully")
  fh.close()
  
print("\n")

#sit
x={1,3,6}
x.add (9)
print (x)

print("\n")

#list
y=[2,4,6]
y[0]=12
print (y)

print("\n")

#dict
z= {"enas":7,"wael":9}
print(z)

print("\n")

u=4
o=(u/3)
print(o)

print("\n")

f=4
n=5
print (f>n)
print (f<=n)
print (not(f>n))


print("\n")

t="hello world"
print (t)

first_name= input("enter first name: ")
second_name= input("enter second name: ")
print(first_name+" " +second_name) 



start_time= time.ctime()
print (start_time)

start= 1
target= 10
while start<= target:
  webbrowser.open("https://rb.gy/iwbeqn")
  time.sleep(60)
start= start+1


