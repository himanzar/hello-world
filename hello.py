
name = input("what is your name? ")
print (f""" \n \n# hello, {name} 
# welcom to python! \n""")
res = input("Do you know Python? ")
while True:
 if res.lower()=="yes":
  print("it's ok")
  break
 elif res.lower()=="no":
  print("you can't use!")
  break
 else:
  print("you can enter 'yse' or 'no only!!")
  res=input("Do you know Python?")
  # Coded by Mr.Manzar
  # github.com/himanzar/hello-world
