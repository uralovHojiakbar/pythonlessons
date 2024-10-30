# counts=dict()
# names=['csev','cwen','csev','zqian','cwen']
# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name]=counts[name]+1
# print(counts)
# text=input('input your text ')
# text2=text.split()
# mid= len (text2)//2
# if len (text2)%2==1:
#     print(f"first element is {len (text2[0])} and middle is {mid } and second is {len (text2[-1])}")
# else:
#     print()
# counts=dict()
# line=input('enter the line of text: ')
# words=line.split()
# print('words',words)
# print('counting...')
# for  word in words:
#     counts[word]=counts.get(word,0)+1
# print('counts', counts)
# keys=['ten','twenty','thirty']
# values=[10,20,30]
# diction={}
# for i in range(len(keys)):
#     diction[keys[i]]=values[i]
# print(diction)
# dict1={'ten':10,'twenty':20,'thirty':30}
# dict2={'thirty':30,'fourty':40,'fifty':50}
# dict3={**dict1,**dict2}
# print(dict3)
# sample_dict={
#     'class':{'student':'Mike','marks':{'physics':70,'history':80}}}
# print(sample_dict['class']['marks']['history'])
dic={'x':25,'y':18,'z':45}
res=0
for x, in zip(dic.values()):
    res+=x
print(res)



