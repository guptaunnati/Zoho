import sys

# print("My name is ", sys.argv[1])

# try:
#     print("My name is ", sys.argv[1])
# except IndexError:
#     print("No argument")

if len(sys.argv)<2:
    print("not enough arguments")
elif len(sys.argv)>2:
    print("more arguments")
else :
    print("My name is", sys.argv[1])