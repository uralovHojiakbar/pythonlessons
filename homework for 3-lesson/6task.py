sum=0
first=input('what is  my name ').lower()
second=input('where do i study ').lower()
third=int(input('6**2='))
fourth=input('what is my laptop ').lower()
fifth=int(input('2**3='))
if first=='hojiakbar':
    sum+=1
if second=='pdp':
    sum+=1
if third==36:
    sum+=1
if fourth=='asus':
    sum+=1
if fifth==8:
    sum+=1
if sum==0:
    print('Next time ')
elif sum==1:
    print('OK')
elif sum==2:
    print('Oops')
elif sum==3:
    print('Almost got it  ')
elif sum==4:
    print('you did a great job ')
else:
    print('you won the prize ')
