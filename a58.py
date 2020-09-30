import os
for i in range(1,58):
    try:
        a=open('a'+str(i)+'.py','r')
        s=a.read()
        a.close()
        print(s)
        x=input('\nY/N')
        if x=='y':
            os.remove('a'+str(i)+'.py')
    except:
        pass
