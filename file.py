  #python program to convert given algorithm to c-program
print('start')
    #creating a file to print c program
f=open("program.c","w")
f2=open("input.txt","r")
    #taking algorithm as input
print('enter the algorithm')
l=[]
d={ 'zero':0,
    '0':'0',
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10,
    'them':2,
    'ab':2,
    'abc':3,
    'abcd':4,
    'result':101,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '':1,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    '':0}
opr={'add':'+',
    'sum':'+',
    'addition':'+',
    'sub':'-',
    'subtraction':'-',
    'difference':'-',
    'sub':'-',
    'product':'*',
    'mul':'*',
    'multiply':'*',
   'div':'div',
   'divide':'div',
   'exit':'exit',
   'exit\n':'exit',
   'end':'exit',
   'end\n':'end',
   'stop':'exit',
   'print':'1',
   'display':'1',
   'result':'3',
   'result\n':'3',
   'r':'3',
   'scan':'2',
   'enter':'2', 
   'int':'11',
   'int\n':'11',
   'integer':'11',
   'integer\n':'11',
   'i':'11',
   'num':'11',
   'num\n':'11',
   'numbers':'11',
   'numbers\n':'11',
   'real number':'12',
   'real number\n':'12',
   'real':'12',
   'real\n':'12',
   'float':'12',
   'float\n':'12',
   'declare':'4',
   'initialize':'4',
   'comp':'5',
   'compare':'5'
   }
variable_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
variable_list2=["a2","b2","c2","d2","e2","f2","g2","h2","i2","j2","k2","l2","m2","n2",
"o2","p2","q2","r2","s2","t2","u2","v2","w2","x2","y2","z2"]
count1=0
print('#include<stdio.h>\n#include<math.h>\nmain()\n{\n',file=f)
print('int result;\nint i;',file=f)
che=1
num_s=0
num_t=0
num3=0
num_f=0
count_i=0
count_f=0
c='abcd'
while c :
    #c=input('')
    c=f2.readline()
    c=c+' num'
    
    l2=[]
    l2.append(c.split(' '))
    l3=l2[0]
    for x in range(len(l3)):
        if l3[x-1] == 'the':
            l3.remove('the')
        if l3[x-1] == 'The':
            l3.remove('The')

    l2[0]=l3
    operation=opr[l2[0][0]]
    #num3=int(d[l2[0][1]])
    
    if operation == '+':
        num3=int(d[l2[0][1]])

        print('result= ',end='',file=f)        
        for x in range(num3):
            print(variable_list[x],end='',file=f)
            if x < num3-1:
                print('+',end='',file=f)
            
        print(';',file=f)
    if operation == '-':
        num3=int(d[l2[0][1]])
        print('result= ',end='',file=f)        
        for x in range(num3):
            print(variable_list[x],end='',file=f)
            if x < num3-1:
                print('-',end='',file=f)
            
        print(';',file=f)
    if operation == '*':
        num3=int(d[l2[0][1]])
        print('result= ',end='',file=f)        
        for x in range(num3):
            print(variable_list[x],end='',file=f)
            if x < num3-1:
                print('*',end='',file=f)
            
        print(';',file=f)
    if operation == 'div':
        num3=int(d[l2[0][1]])
        print('result= ',end='',file=f)        
        for x in range(num3):
            print(variable_list[x],end='',file=f)
            if x < num3-1:
                print('/',end='',file=f)
            
        print(';',file=f)
    if operation == 'exit':
        break
        #printing part
    if operation == '1':
        num3=int(d[l2[0][1]])
        if num3 == 101:
            print('printf("%d",result);',file=f)
        else:
            print('printf("',end='',file=f)
            for x in range(num3):
                print('%d',end='',file=f)
            print('",',end='',file=f)
            count2=1
            for x in range(num3):
                print(variable_list[x],end='',file=f)
                if(x<num2-1):
                    print(',',end='',file=f)

            print(');',file=f)
        #scanning part
    if operation == '2': 
        num3=int(d[l2[0][1]]) 
        num_t=num3
        if num3 <= 5 :
            type=opr[l2[0][2]] 
            print('printf("enter ',end='',file=f)
            print(num3,end='',file=f)
            print(' numbers',end='',file=f)
            #print(l2[0][2],end='',file=f)
            print('");',file=f) 
            if type == '11':
                if num3>num_s:
                    print('int ',end='',file=f)
                    for x in range(num_s,num3):
                        print(variable_list[x],end='',file=f)
                        if x < num3-1:
                            print(',',end='',file=f)
                    print(';',file=f)
                num_s=num3        
                print('scanf("',end='',file=f)
                for x in range(num3):
                    print('%d',end='',file=f)
                print('",',end='',file=f)
                count2=1
                for x in range(num3):
                    print("&",end='',file=f)
                    print(variable_list[x],end='',file=f)
                    if(x<num3-1):
                        print(',',end='',file=f)
                print(');',file=f)
            if type == '12':
                if num3>num_f:
                    print('float ',end='',file=f)
                    for x in range(num_f,num3):
                        print(variable_list2[x],end='',file=f)
                        if x < num3-1:
                            print(',',end='',file=f)
                    print(';',file=f)
                num_f=num3      
                print('scanf("',end='',file=f)
                for x in range(num3):
                    print('%f',end='',file=f)
                print('",',end='',file=f)
                count2=1
                for x in range(num3):
                    print("&",end='',file=f)
                    print(variable_list2[x],end='',file=f)
                    if(x<num3-1):
                        print(',',end='',file=f)

                print(');',file=f)
        if num3 > 5:
            type=opr[l2[0][2]] 
            print('printf("enter ',end='',file=f)
            print(num3,end='',file=f)
            print(' numbers',end='',file=f)
            #print(l2[0][2],end='',file=f)
            print('");',file=f) 
            if type == '11':
                if count_i == 0:
                    print('int a_int[20];',file=f)
                    count_i=count_i+1
                print('for(i=0;i<',end='',file=f)
                print(num3,end='',file=f)
                print(';i++)\n{\n scanf("%d",&a_int[i];\n}\n',end='',file=f)
            if type == '12':
                if count_f == 0:
                    print('float a_float[20];',file=f)
                    count_f=count_f+1
                print('for(i=0;i<',end='',file=f)
                print(num3,end='',file=f)
                print(';i++)\n{\n scanf("%f",&a_float[i];\n}\n',end='',file=f)

    if operation =='3' :
        print('printf("result is %d",result);',file=f)
           
print('return;',file=f)
print('}',file=f)
