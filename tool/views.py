from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

urlsize=18  
# toolsize={'size':urlsize} 

def main(request):
    item=[
        {
            'id':1,
            'img':'https://onlinetools.com/images/ascii/illustrations/default.png',
            'title':'ASCII',
            'desc':"ASCII is a character encoding system that converts text into numerical values for computers and electronic devices. It uses a seven-bit binary system to represent 128 characters, including letters, numbers, punctuation, and control codes. The first 33 codes handle non-printing functions like tab and line feed, while the rest are readable characters. Often, it’s expanded to an eight-bit system, allowing for 256 characters, including symbols from other languages. ASCII has been a key part of computing and data communication for decades. ",
            'history':"ASCII was developed in the 1960s for teleprinters and became the foundation for modern computer character sets, HTML, and the Internet. Unicode extends ASCII to support millions of characters, with UTF-8 becoming the web standard in 2007.",
        },
        {
            'id':2,
            # 'img':'https://render.fineartamerica.com/images/images-profile-flow/400/images/artworkimages/mediumlarge/3/3-droste-effect-background-with-infinite-clock-spiral-abstract-de-paolo-gallo-modena.jpg',
            'img':'https://i.gifer.com/g09P.gif', 
            'title':'Roman numerals',
            'desc':'Roman numerals are read based on addition and subtraction rules. Repeating a letter adds its value (II = 2), while placing a smaller letter before a larger one means subtraction (IV = 4). If a larger letter comes first, the values are added (CX = 110). The letters V, L, and D can’t be repeated, and only I, X, and C are used for subtraction. Their exact origin is unclear, but they may have been created for trade.',
            'history':'Roman numerals originated in ancient Rome and were used across Europe until the Late Middle Ages. They represent numbers using Latin letters, each with a fixed value. This system remained the standard for writing numbers for centuries.'
        },
        {
            'id':3,
            # 'img':'https://cdn2.vectorstock.com/i/1000x1000/40/06/binary-code-globe-symbol-icon-design-vector-22314006.jpg',
            'img':'https://i.gifer.com/3cth.gif', 
            'title':'Binary Numbers',
            'desc':"Binary numbers are the foundation of computing, using only the digits 0 and 1, known as bits. Each bit represents a power of two, and converting binary to decimal involves multiplying each bit by its corresponding power and adding the results. This system, called base-2, represents numbers using only two symbols: '0' (zero) and '1' (one). Some rational numbers can also be expressed in binary as the quotient of an integer by a power of two. Binary is essential in digital technology and computing.",
            'history':'The modern binary number system was studied in Europe in the 16th and 17th centuries by Thomas Harriot, and Gottfried Leibniz. However, systems related to binary numbers have appeared earlier in multiple cultures including ancient Egypt, China, Europe and India.'
        },
        {
            'id':4,
            'img':'https://upload.wikimedia.org/wikipedia/commons/c/cc/Digital_rain_animation_medium_letters_shine.gif',
            'title':'Characters',
            # 'desc':'''In programming, characters represent letters, numbers, symbols, and control codes. They are typically assigned using single quotes and represented as 'char' or 'chr' in code. A character string is a sequence of characters enclosed in double quotes, including letters (a, b..., A, B...), digits (0...9), spaces, and special symbols (+, <, $, &, |, !, ^, ~, :, '," and more). Control characters, like newlines and tabs, perform specific functions rather than displaying visible symbols. These characters are essential for coding, formatting, and device communication.''',
            'desc':"In programming, characters represent letters, numbers, symbols, and control codes. They are assigned using single quotes and represented as 'char' or 'chr' in code. Character strings, enclosed in double quotes, include letters, digits, spaces, and special symbols. Control characters like newlines and tabs perform specific functions rather than displaying visible symbols. These characters play a crucial role in coding, formatting, and device communication.",
            'history':"Characters in programming languages have evolved alongside computing. Early languages like FORTRAN (1957) and COBOL (1959) used basic character sets, while ASCII (1963) standardized text representation. Later, Unicode (1991) expanded character support to include global languages and symbols."
        },
        {
            'id':5,
            'img':'https://media.istockphoto.com/id/115814295/photo/green-lcd-2.jpg?s=612x612&w=0&k=20&c=AZrEi3L1NhrU70ALV3PUEdc5aFtaqe_M56mvIKFqF5Q=',
            'title':'Octal Numbers',
            'desc':'Octal is a number system that uses only eight digits: 0 to 7. It’s like a shortcut for writing long binary numbers since each octal digit represents a group of three binary digits. Back in the day, programmers and engineers used it a lot in coding and machine language. You can still see octal in UNIX file permissions, where numbers like 755 or 644 control access to files. While it’s not as common today, it remains a cool and useful way to handle numbers in computing!',
            'history':'Octal, or base-8, has been around since the early days of computing. It was a handy way for engineers to work with binary in a more readable format. While it was widely used in older computers, it later took a backseat to hexadecimal.'
        },
        {
            'id':6,
            'img':'https://techieloops.com/wp-content/uploads/2021/12/hexadecimal-numbers.png',
            'title':'Hexadecimal Numbers',
            'desc':'Hexadecimal uses 16 symbols: the digits 0-9 and the letters A-F. It’s a shorthand for binary, where each hex digit represents four binary digits, making it easier to read and write long binary numbers. You’ve probably seen hex in HTML color codes, like #FF5733, which defines colors on websites. It’s also essential in programming, helping computers store and process data efficiently. While we don’t use it in everyday math, it’s a must-know for tech and coding!',
            'history':'Hexadecimal, or base-16, became popular in computing as a more efficient way to represent binary numbers. It was widely adopted in the 1960s when computers started using 8-bit bytes, making hex a perfect fit. Today, it’s still used in programming, memory addresses, and color codes.'
        }
    ]
    return render(request, 'main.html',{'item':item,'size':urlsize})

def about(request):
    return render(request, 'about.html',{'size':urlsize}) 

def redirect(request, idpath):
    return redirect(f'/{idpath}') 

def tools(request):  
    # global urlsize 
    urlss=[
        {'id': 1, 'url': 'ronum', 'name1': 'Roman', 'name2': 'to', 'name3': 'Numericals'},
        {'id': 2, 'url': 'nurom', 'name1': 'Numericals', 'name2': 'to', 'name3': 'Roman'},
        {'id': 3, 'url': 'asciichar', 'name1': 'ASCII', 'name2': 'to', 'name3': 'Character'},
        {'id': 4, 'url': 'charascii', 'name1': 'Character', 'name2': 'to', 'name3': 'ASCII'},
        {'id': 5, 'url': 'charbin', 'name1': 'Character', 'name2': 'to', 'name3': 'Binary'},
        {'id': 6, 'url': 'binchar', 'name1': 'Binary', 'name2': 'to', 'name3': 'Character'},
        {'id': 7, 'url': 'binnum', 'name1': 'Binary', 'name2': 'to', 'name3': 'Number'},
        {'id': 8, 'url': 'binoct', 'name1': 'Binary', 'name2': 'to', 'name3': 'Octal'},
        {'id': 9, 'url': 'binhex', 'name1': 'Binary', 'name2': 'to', 'name3': 'Hexadecimal'},
        {'id': 10, 'url': 'numbin', 'name1': 'Number', 'name2': 'to', 'name3': 'Binary'},
        {'id': 11, 'url': 'decoct', 'name1': 'Decimal', 'name2': 'to', 'name3': 'Octal'},
        {'id': 12, 'url': 'dechex', 'name1': 'Decimal', 'name2': 'to', 'name3': 'Hexadecimal'},
        {'id': 13, 'url': 'octdec', 'name1': 'Octal', 'name2': 'to', 'name3': 'Decimal'},
        {'id': 14, 'url': 'octbin', 'name1': 'Octal', 'name2': 'to', 'name3': 'Binary'},
        {'id': 15, 'url': 'octhex', 'name1': 'Octal', 'name2': 'to', 'name3': 'Hexadecimal'},
        {'id': 16, 'url': 'hexoct', 'name1': 'Hexadecimal', 'name2': 'to', 'name3': 'Octal'},
        {'id': 17, 'url': 'hexbin', 'name1': 'Hexadecimal', 'name2': 'to', 'name3': 'Binary'},
        {'id': 18, 'url': 'hexdec', 'name1': 'Hexadecimal', 'name2': 'to', 'name3': 'Decimal'}, 
    ]
    urlsize=len(urlss)
    # print(len(urlss),'number')  
    return render(request, 'tools.html',{'items':urlss}) 

@csrf_exempt
def rom2num(request):
    # c={'i':1,'ii':2,'iii':3,'iv':4,'v':5,'vi':6,'vii':7,'viii':8,'ix':9,'x':10,'xx':20,'xxx':30,'xl':40,'l':50,'lx':60,'lxx':70,'lxxx':80,'xc':90,'c':100,'cc':200,'ccc':300,'cd':400,'d':500,'dc':600,'dcc':700,'dccc':800,'cm':900,'m':1000,'mm':2000,'mmm':3000,'I̅V̅':4000,'V̅':5000,'V̅I̅':6000,'V̅I̅I̅':7000,'V̅I̅I̅I̅':8000,'I̅X̅':9000,'X̅':10000}
    c={'i':1,'ii':2,'iii':3,'iv':4,'v':5,'vi':6,'vii':7,'viii':8,'ix':9,'x':10,'xx':20,'xxx':30,'xl':40,'l':50,'lx':60,'lxx':70,'lxxx':80,'xc':90,'c':100,'cc':200,'ccc':300,'cd':400,'d':500,'dc':600,'dcc':700,'dccc':800,'cm':900,'m':1000,'mm':2000,'mmm':3000,'-iv':4000,'-v':5000,'-vi':6000,'-vii':7000,'-viii':8000,'-ix':9000,'-x':10000,'-x-x':20000,'-x-x-x':30000,'-x-l':40000,'-l':50000,'-l-x':60000,'-l-x-x':70000,'-l-x-x-x':80000,'-x-c':90000,'-c':100000}
    d=0 
    inp=''
    msg=''
    if request.method == 'POST':
        a=request.POST.get('data').lower().strip()       
        inp=a  
        i = 0
        while i < len(a):
            if a[i:i+4] in c:
                d += c.get(a[i:i+4])   
                i += 4
            elif a[i:i+3] in c:
                d += c.get(a[i:i+3])   
                i += 3
            elif a[i:i+2] in c:
                d += c.get(a[i:i+2])  
                i += 2
            elif a[i:i+1] in c:
                d += c.get(a[i:i+1])   
                i += 1
            else:
                msg= f"Invalid input: {a[i]}"  
                break  # Stop if an invalid character is found

        print(d)
    
    return render(request,'rom2num.html',{'d':d,'indata':inp.upper(),'msg':msg})

@csrf_exempt
def num2rom(request):
    d={'1':'i','2':'ii','3':'iii','4':'iv','5':'v','6':'vi','7':'vii','8':'viii','9':'ix','10':'x','20':'xx','30':'xxx','40':'xl','50':'l','60':'lx','70':'lxx','80':'lxxx','90':'xc','100':'c','200':'cc','300':'ccc','400':'cd','500':'d','600':'dc','700':'dcc','800':'dccc','900':'cm','1000':'m','2000':'mm','3000':'mmm','4000':'I̅V̅','5000':'V̅','6000':'V̅I̅','7000':'V̅I̅I̅','8000':'V̅I̅I̅I̅','9000':'I̅X̅','10000':'X̅','20000':'X̅X̅','30000':'X̅X̅X̅','40000':'L̅X̅','50000':'L̅','60000':'L̅X̅','70000':'L̅X̅X̅','80000':'L̅X̅X̅X̅','90000':'X̅C̅','100000':'C̅','200000':'C̅C̅','300000':'C̅C̅C̅'} 
    f=''
    inp=''
    msg=''
    if request.method == 'POST':
        b=request.POST.get('data')[::-1]
        inp=b
        # b=a[::-1]
        # d={'1':'i','2':'ii','3':'iii','4':'iv','5':'v','6':'vi','7':'vii','8':'viii','9':'ix','10':'x','20':'xx','30':'xxx','40':'xl','50':'l','60':'lx','70':'lxx','80':'lxxx','90':'xc','100':'c','200':'cc','300':'ccc','400':'cd','500':'d','600':'dc','700':'dcc','800':'dccc','900':'cm','1000':'m','2000':'mm','3000':'mmm','4000':'I̅V̅','5000':'V̅','6000':'V̅I̅','7000':'V̅I̅I̅','8000':'V̅I̅I̅I̅','9000':'I̅X̅','10000':'X̅'}
        # e=[]
        # for i in range(len(b)):
        #     e=[str(int(b[i])*(10**i))]+e
        try:
            e=[str(int(b[i])*(10**i)) for i in range(len(b))]
            print(e)
        
            for j in e[::-1]:
                if j in d:
                    f+=d.get(j)
        except ValueError:
            msg='Invalid number'   
        print(f)
    return render(request,'num2rom.html',{'d':f.upper(),'indata':inp[::-1],'msg':msg})
    
@csrf_exempt
def char2ascii(request):
    n=''
    inp=''
    if request.method == 'POST':
        b= request.POST.get('data')
        inp=b
        for i in b:
            n=str(ord(i))
       
    return render(request,'char2ascii.html',{'d':n,'indata':inp})

@csrf_exempt
def ascii2char(request):
    n=''
    inp=''
    msg=''
    if request.method == 'POST':
        b= request.POST.get('data')
        inp=b
        # for i in int(b):
            # n=chr(i)
        try:
            if type(int(b))==int:   
                n=chr(int(b))      
        except ValueError:
            msg='Enter valid ASCII value (only numbers)' 
          
    return render(request,'ascii2char.html',{'d':n,'indata':inp,'msg':msg}) 

@csrf_exempt
def num2bin(request):
    b=[]
    o=''
    inp=''
    msg=''
    if request.method == 'POST':
        n= request.POST.get('data')
        inp=n
        try:
            n=int(n)
            for i in range(n):
                if n!=0:
                    r=n%2
                    b=[r]+b
                    o+=str(r)
                    n//=2
                else:
                    break
            # print(b)
            for i in range(len(b),9):
                if len(b)<8:
                    o='0'+o
                    b=[0]+b
            # o=''.join(str(b))
        except ValueError:
            msg='Invalid input'
       
    return render(request,'num2bin.html',{'d':b,'indata':inp,'o':o,'msg':msg})

@csrf_exempt
def bin2num(request):
    c=0
    inp=''
    msg=''
    if request.method == 'POST':
        b= request.POST.get('data')[::-1]
        inp=b[::-1]
        for i in range(len(b)):
            if b[i]=='0':
                continue
            elif b[i]=='1':
                c=c+2**i
            else:
                msg=f"Binary number must be only '0' or '1' not '{b[i]}'" 
                break 
                
    return render(request,'bin2num.html',{'d':c,'indata':inp,'msg':msg})

@csrf_exempt
def char2bin(request):
    # a=[]
    # o=''
    # if request.method == 'POST':
    #     s=request.POST.get('data')
    #     for i in s:
    #         n=ord(i)
    #         b=[]
    #         for j in range(n):
    #             if n!=0:
    #                 r=n%2
    #                 b=[r]+b
    #                 n//=2
    #             else:
    #                 break
    #         if len(b)<8:
    #             for k in range(len(b),8):
    #                     b=[0]+b
    #         b=[i]+b 
    #         # print(''.join(b))
    #         a+=[b]
    #     for j in a:
    #         for k in range(1,len(j)):
    #             o+=str(j[k])
    a={}
    inp=''
    o=''
    # out=[]
    if request.method == 'POST':
        s=request.POST.get('data')
        inp=s
        for i in s:
            n=ord(i)
            b=''
            for j in range(n):
                if n!=0:
                    r=n%2
                    b=str(r)+b
                    n//=2
                else:
                    break
            if len(b)<8:
                for k in range(len(b),8):
                        b='0'+b
            # b=[i]+b 
            # print(''.join(b))
            o+=b
            a[i]=b
            
        # for j in a:
        #     for k in range(1,len(j)):
        #         o+=str(j[k])
    # context={}
    return render(request,'char2bin.html',{'d':a,'out':o,'indata':inp})

@csrf_exempt
def bin2char(request):
    d=''
    inp=''
    msg=''
    if request.method == 'POST':
        a= request.POST.get('data')
        inp=a
        # b=[]
        # for i in range(0,len(a),8):
        #     b+=[a[i:i+8]]
        b=[a[i:i+8] for i in range(0,len(a),8)]
        for j in b:
            c=0
            j=j[::-1]
            for i in range(len(j)):
                if j[i]=='1':
                    c=c+2**i
                elif j[i]=='0':
                    continue
                else:
                    msg=f"Binary number must be only '0' or '1' not '{b[i]}'" 
                    break 
            d+=chr(c)
       
    return render(request,'bin2char.html',{'d':d,'indata':inp,'msg':msg}) 

@csrf_exempt
def oct2dec(request):
    b=0
    msg='' 
    inp=''
    if request.method == 'POST':
        a=request.POST.get('data')
        inp=a
        for i in range(len(a[::-1])):
            if a[::-1][i] in '01234567':
                b+=(8**i)*int(a[::-1][i])
            else:
                msg='Octal contains only 0-7 digits.'
    # return render(request,'oct2dec.html',{'d':b if not error else None,'indata':inp})
    return render(request,'oct2dec.html',{'d':b,'indata':inp,'msg':msg})

@csrf_exempt
def dec2oct(request):
    o=''
    # c=''
    inp=''
    msg=''
    if request.method == 'POST':
        a=request.POST.get('data')
        inp=a
        try:
            b=int(a)
            for i in range(b):
                if b!=0:
                    r=b%8
                    o=str(r)+o
                    b=b//8
                # else:
                    # c='Octal number system contains only 0-7 digits.'
        except ValueError:
            msg='Inalid input'
    return render(request,'dec2oct.html',{'d':o,'indata':inp,'msg':msg})

@csrf_exempt
def oct2bin(request):
    c=''
    inp=''
    msg=''
    if request.method == 'POST':
        a=request.POST.get('data')
        inp=a
        b={'0':'0','1':'1','2':'10','3':'11','4':'100','5':'101','6':'110','7':'111'}
        for i in a:
            if i in b:
                c+=b.get(i)
            else:
                msg='Octal contains only 0-7 digits'
    return render(request,'oct2bin.html',{'d':c,'indata':inp,'msg':msg})

@csrf_exempt
def oct2hex(request):
    c=''
    inp=''
    msg=''
    if request.method == 'POST':
        a=request.POST.get('data')
        inp=a
        b=0
        try:
            for i in range(len(a[::-1])):
                b+=(8**i)*int(a[::-1][i])
            print('oct-',b)
            for i in range(b):
                if b!=0:
                    r=b%16
                    if r in range(10):
                        c=str(r)+c
                    elif r in range(10,16):
                        c=chr(r+55)+c
                    b//=16
        except ValueError:
            msg='Octal contains only 0-7 digits'
    return render(request,'oct2hex.html',{'d':c,'indata':inp,'msg':msg})

@csrf_exempt
def bin2oct(request):
    c=0
    inp=''
    msg='' 
    if request.method == 'POST':
        a=request.POST.get('data')
        inp=a
        b=a[::-1]
        for i in range(0,len(b)):
            if b[i]=='1':
                c+=(2**i)*(int(b[i]))
            elif b[i]=='0':
                continue
            else:
                msg=f"Binary number must be only '0' or '1' not '{b[i]}'" 
                break
    return render(request,'bin2oct.html',{'d':oct(c)[2:],'indata':inp,'msg':msg})

@csrf_exempt
def bin2hex(request):
    c=0
    inp=''
    msg=''
    if request.method == 'POST':
        a=request.POST.get('data')
        inp=a
        b=a[::-1]
        for i in range(0,len(b)):
            if b[i]=='1':
                c+=(2**i)*(int(b[i]))
            elif b[i]=='0':
                continue
            else:
                msg=f"Binary number must be only '0' or '1' not '{b[i]}'" 
                break 
        # print('dec-',c)
        # print('oct-',hex(c)[2:].upper())
    return render(request,'bin2hex.html',{'d':hex(c)[2:].upper(),'indata':inp,'msg':msg})  

@csrf_exempt
def dec2hex(request):
    inp=''
    msg=''
    b=0
    if request.method == 'POST':
        a=request.POST.get('data')
        inp=a
        try:
            b=int(a)
        except ValueError:
            msg='Invalid input'
    return render(request,'dec2hex.html',{'d':hex(b)[2:].upper(),'indata':inp,'msg':msg})

@csrf_exempt
def hex2oct(request):
    inp=''
    msg=''
    c=0
    if request.method == 'POST':
        a=request.POST.get('data').upper().strip()
        inp=a
        a=a[::-1]
        b={'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
        for i in range(len(a)):
            if a[i] in b and a[i] in '0123456789ABCDEF':
                c+=((16**i)*int(b[a[i]]))
            else:
                msg="Hexadecimal contains only '0' to '9' & 'A' to 'F'"
        # print(c)
        # print(oct(c)[2:])
    return render(request,'hex2oct.html',{'d':oct(c)[2:],'indata':inp,'msg':msg})

@csrf_exempt
def hex2dec(request):
    inp=''
    c=0
    if request.method == 'POST':
        a=request.POST.get('data').upper()
        inp=a
        a=a[::-1]
        b={'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
        for i in range(len(a)):
            if a[i] in b and a[i] in '0123456789ABCDEF':
                c+=((16**i)*int(b[a[i]]))
            else:
                msg="Hexadecimal must be '0' to '9' & 'A' to 'F'"
                
    return render(request,'hex2dec.html',{'d':c,'indata':inp})

@csrf_exempt
def hex2bin(request):
    inp=''
    c=0
    if request.method == 'POST':
        a=request.POST.get('data').upper()
        inp=a
        a=a[::-1]
        b={'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
        for i in range(len(a)):
            if a[i] in b and a[i] in '0123456789ABCDEF':
                c+=((16**i)*int(b[a[i]]))
            else:
                msg="Hexadecimal must be '0' to '9' & 'A' to 'F'"
                
    return render(request,'hex2bin.html',{'d':bin(c)[2:],'indata':inp}) 