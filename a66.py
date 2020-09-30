import sys

sys.stdin=open('66.txt')
sys.stdout=open('666.txt','w')

a=input()
b=input()
print(a+b)



sys.stdout.close()
