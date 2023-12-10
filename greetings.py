def greeting(name): #name is in local scope, only usable in this function
    print('Hello', name)

#Main program
input_name = input("What's your name?\n") #input_name is in global scope, can be use anywhere

greeting(input_name)
#End program
