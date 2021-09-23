#Writing and Appending  to a file
f = open("Aman2.txt", "a")  #open in append mode
a = f.write("Aman goes to collage\n")
print(a)
f.close()

f = open("Aman3.txt", "a")
a = f.write("Aman goes to collage everyday\n")
print(a)
f.close()

# Handle read and write both
f = open("Aman3.txt", "r+")
print(f.read())
f.write("Thankyou")