import math
import tkinter as tk
win = tk.Tk()

frame1 = tk.Frame(win).grid(row = 0,column = 0)
t = tk.Entry(frame1,width=33,borderwidth = 5,fg = 'blue',bg = '#90ffff',font = ('Helvetica',12,'bold'))
t.grid(row = 1,column = 0)
t1 = tk.Entry(frame1,width=50,fg = 'black',font = ('Helvetica',8,'bold'))
t1.grid(row = 0,column = 0)
t1.insert(0,'                                                                                           deg')
special_func =['sin','cos','tan','cot','sec','cosec','asi','aco','ata','sih','coh','tah','sqrt','fact','log']

def find_special_func(exp):
    exp = list(exp)
    i = 0
    while(i < len(exp) - 3):
        if (exp[i].isalpha()):
            while(exp[i + 1] != ')'):
                exp[i] += exp[i + 1]
                exp.remove(exp[i+ 1])
            exp[i] += exp[i + 1]
            exp.remove(exp[i+ 1])
            x = exp.index(exp[i])
            e = exp[x]
            s = special_func.index(e[:3])
            j = 4
            num = 0
            while (e[j] != ')'):
                num = num * 10 + float(e[j])
                j += 1
            if(s >= 0 and s < 6):
                num = math.radians(num)
                if (s == 0):
                    exp.remove(e)
                    exp.insert(x, round(math.sin(num), 2))
                elif (s == 1):
                    exp.remove(e)
                    exp.insert(x, round(math.cos(num), 2))    
                elif (s == 2):
                    exp.remove(e)
                    exp.insert(x, round(math.tan(num), 2))
                elif (s == 3):
                    exp.remove(e)
                    exp.insert(x, round(math.cot(num), 2))
                elif (s == 4):
                    exp.remove(e)
                    exp.insert(x, round(math.sec(num), 2))
                elif (s == 5):
                    exp.remove(e)
                    exp.insert(x, round(math.cosec(num), 2))
            elif(s > 5 and s < 9):
                if (s == 6):
                    exp.remove(e)
                    num = math.asin(num)
                    num = math.degrees()
                    exp.insert(x, round(num, 2))
                elif (s == 7):
                    exp.remove(e)
                    num = math.acos(num)
                    num = math.degrees()
                    exp.insert(x, round(num, 2))
                elif (s == 8):
                    exp.remove(e)
                    num = math.atan(num)
                    num = math.degrees()
                    exp.insert(x, round(num, 2))
            elif(s > 8 and s < 12):
                if (s == 9):
                    exp.remove(e)
                    exp.insert(x, round(math.sinh(num), 2))
                elif (s == 10):
                    exp.remove(e)
                    exp.insert(x, round(math.cosh(num), 2))
                elif (s == 11):
                    exp.remove(e)
                    exp.insert(x, round(math.tanh(num), 2))
            else:
                if (s == 12):
                    exp.remove(e)
                    exp.insert(x, round(math.sqrt(num), 2))
                elif (s == 13):
                    exp.remove(e)
                    exp.insert(x, round(math.factorial(num), 2))
                elif (s == 14):
                    exp.remove(e)
                    print(num)
                    exp.insert(x, round(math.log(num), 2))
        i += 1
    return exp

def disdegrad():
    x = t1.get()
    l = len(x)
    if (x[l-3:] == 'deg'):
        t1.delete(l - 3,tk.END)
        t1.insert(l - 3,'rad')
    elif (x[l-3:] == 'rad'):
        t1.delete(l - 3,tk.END)
        t1.insert(l - 3,'deg')

def infix_to_postfix(exp):
    i = 0
    while(i < len(exp)):
        if (type(exp[i]) == str):
            if(exp[i].isdigit()):
                exp[i] = float(exp[i])
        i += 1

    i = 0
    while(i < (len(exp) - 2)):
        if(exp[i + 1] == '.'):
            j = i + 2
            count = 1
            while(type(exp[j]) == float):
                exp[i] += exp[j] / (10 ** count)
                exp.remove(exp[j])
                exp[i] = float(exp[i])
                count += 1
            exp[i] = round(exp[i],count - 1)
            exp.remove(exp[i + 1])
        i += 1

    pre = {'^':4,'(':3,')':3,'*':2,'/':2,'+':1,'-':1}
    oper = []
    def cal(res):
        val = []
        for i in res:
            if(type(i) is float):
                val.append(i)
            elif(i in ['+','-','*','/']):
                y = val.pop()
                x = val.pop()
                if(i == '+'):
                    val.append(x + y)
                if(i == '-'):
                    val.append(x - y)
                if(i == '*'):
                    val.append(x * y)
                if(i == '/'):
                    val.append(x / y)
        if(val[0] % 1 == 0):
            val = int(val[0])
        else:
            val = val[0]
        return val
    res = []

    for i in exp:
        if(type(i) is float):
            res.append(i)
        else:
            if(len(oper) == 0):
                oper.append(i)
            elif(oper[-1] == '('):
                oper.append(i)
            elif(i == ')'):
                while(oper[-1] != '('):
                    o = oper.pop()
                    res.append(o)
                oper.pop()
            elif(i == '('):
                oper.append(i)
            elif(pre[i] > pre[oper[-1]]):
                oper.append(i)
            elif(pre[i] == pre[oper[-1]]):
                o = oper.pop()
                res.append(o)
                oper.append(i)
            elif(pre[i] < pre[oper[-1]]):
                while(pre[i] <= pre[oper[-1]]):
                    o = oper.pop()
                    res.append(o)
                    if(len(oper) == 0):
                        break
                oper.append(i)
    while(len(oper) > 0):
        o = oper.pop()
        res.append(o)
    result = cal(res)
    return result

def dis(x):
    t.insert(tk.END,x)

def clear():
    t.delete(0,tk.END)

def back():
    x = t.get()
    L = len(x) - 1
    t.delete(L)

def equal():
    exp = find_special_func(t.get())
    result = infix_to_postfix(exp)
    t.insert(tk.END,' = ')
    s = "" + str(result)
    t.insert(tk.END,s)

def basic(x):
    global frame2 
    frame2 = tk.Frame(win,bg = 'black')
    b_basic = tk.Button(frame2,text = 'BASIC',width = 23,bg = 'brown',fg = 'white',font =('Helvetica',7,'bold'),command =lambda: basic(0)).grid(row = 2,column = 0,columnspan=2)
    b_special = tk.Button(frame2,text = 'SPECIAL',width = 23,bg = 'brown',fg = 'white',font =('Helvetica',7,'bold'),command =lambda: special(0)).grid(row = 2,column = 2,columnspan=2)

    b_opar = tk.Button(frame2,text = '(',width = 5,height = 1,border = 5,bg = '#dddddd',fg = 'blue',font =('Helvetica',15,'bold'),command = lambda : dis('(')).grid(row = 3,column = 0)
    b_cpar = tk.Button(frame2,text = ')',width = 5,height = 1,border = 5,bg = '#dddddd',fg = 'blue',font =('Helvetica',15,'bold'),command = lambda : dis(')')).grid(row = 3,column = 1)

    b7 = tk.Button(frame2,text = '7',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(7)).grid(row = 4,column = 0)
    b8 = tk.Button(frame2,text = '8',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(8)).grid(row = 4,column = 1)
    b9 = tk.Button(frame2,text = '9',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(9)).grid(row = 4,column = 2)

    b6 = tk.Button(frame2,text = '6',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(6)).grid(row = 5,column = 0)
    b5 = tk.Button(frame2,text = '5',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(5)).grid(row = 5,column = 1)
    b4 = tk.Button(frame2,text = '4',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(4)).grid(row = 5,column = 2)

    b1 = tk.Button(frame2,text = '1',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(1)).grid(row = 6,column = 0)
    b2 = tk.Button(frame2,text = '2',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(2)).grid(row = 6,column = 1)
    b3 = tk.Button(frame2,text = '3',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(3)).grid(row = 6,column = 2)

    b0 = tk.Button(frame2,text = '0',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis(0)).grid(row = 7,column = 1)

    b_dot = tk.Button(frame2,text = '.',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda : dis('.')).grid(row = 3,column = 2)
    b_plus = tk.Button(frame2,text = '+',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: dis('+')).grid(row = 3,column = 3)
    b_minus = tk.Button(frame2,text = '-',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: dis('-')).grid(row = 4,column = 3)
    b_mul = tk.Button(frame2,text = '*',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: dis('*')).grid(row = 5,column = 3)
    b_div = tk.Button(frame2,text = '/',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: dis('/')).grid(row = 6,column = 3)
    b_equal = tk.Button(frame2,text = '=',width = 5,height = 1,border = 5,bg = '#00ff00',fg = 'black',font =('Helvetica',15,'bold'),command = equal).grid(row = 7,column = 3)

    b_clear = tk.Button(frame2,text = 'CLEAR',width = 5,height = 1,fg = '#ffffff',bg = '#ff0000',border = 5,font =('Helvetica',15,'bold'),command = clear).grid(row = 7,column = 0)
    b_back = tk.Button(frame2,text = 'BACK',width = 5,height = 1,fg = '#000000',bg = '#fff000',border = 5,font =('Helvetica',15,'bold'),command = back).grid(row = 7,column = 2)
    
    if(x == 0):
        pass
    else:
        frame3.grid_forget()
    frame2.grid(row = 2,column = 0)

def special(x):
    global frame3
    frame3 = tk.Frame(win,bg = 'black')
    b_basic = tk.Button(frame3,text = 'BASIC',width = 23,bg = 'brown',fg = 'white',font =('Helvetica',7,'bold'),command =lambda: basic(1)).grid(row = 2,column = 0,columnspan=2)
    b_special = tk.Button(frame3,text = 'SPECIAL',width = 23,bg = 'brown',fg = 'white',font =('Helvetica',7,'bold'),command =lambda: special(1)).grid(row = 2,column = 2,columnspan=2)

    b_sin = tk.Button(frame3,text = 'sin',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda : dis('sin(')).grid(row = 3,column = 0)
    b_cos = tk.Button(frame3,text = 'cos',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda : dis('cos(')).grid(row = 3,column = 1)
    b_tan = tk.Button(frame3,text = 'tan',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda : dis('tan(')).grid(row = 3,column = 2)

    b_pow = tk.Button(frame3,text = '^',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: dis('^')).grid(row = 3,column = 3)

    b_cot = tk.Button(frame3,text = 'cot',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis('cot(')).grid(row = 4,column = 0)
    b_sec = tk.Button(frame3,text = 'sec',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis('sec(')).grid(row = 4,column = 1)
    b_cosec = tk.Button(frame3,text = 'cesec',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis('cosec(')).grid(row = 4,column = 2)

    b_fact = tk.Button(frame3,text = 'fact',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: dis('fact(')).grid(row = 4,column = 3)

    b_sinINV = tk.Button(frame3,text = 'sin-1',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis('sin-1(')).grid(row = 5,column = 0)
    b_cosINV = tk.Button(frame3,text = 'cos-1',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis('cos-1(')).grid(row = 5,column = 1)
    b_tanINV = tk.Button(frame3,text = 'tan-1',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis('tan-1(')).grid(row = 5,column = 2)
    
    b_log = tk.Button(frame3,text = 'log',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: dis('log(')).grid(row = 5,column = 3)
    
    b_sinh = tk.Button(frame3,text = 'sinh',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis('sinh(')).grid(row = 6,column = 0)
    b_cosh = tk.Button(frame3,text = 'cosh',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda : dis('cosh(')).grid(row = 6,column = 1)
    b_tanh = tk.Button(frame3,text = 'tanh',width = 5,height = 1,border = 5,bg = '#666666',fg = 'white',font =('Helvetica',15,'bold'),command = lambda: dis('tanh(')).grid(row = 6,column = 2)
    global b_de_ra
    b_de_ra = tk.Button(frame3,text = 'deg/rad',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: disdegrad()).grid(row = 6,column = 3)
    
    b_clear = tk.Button(frame3,text = 'CLEAR',width = 5,height = 1,border = 5,bg = '#ff0000',fg = '#ffffff',font =('Helvetica',15,'bold'),command = clear).grid(row = 7,column = 0)
    b_sqrt = tk.Button(frame3,text = 'sqrt',width = 5,height = 1,border = 5,bg = '#dddddd',fg = '#0000ff',font =('Helvetica',15,'bold'),command = lambda: dis('sqrt(')).grid(row = 7,column = 1)
    b_back = tk.Button(frame3,text = 'BACK',width = 5,height = 1,border = 5,bg = '#fff000',fg = '#000000',font =('Helvetica',15,'bold'),command = back).grid(row = 7,column = 2)
    b_equal = tk.Button(frame3,text = '=',width = 5,height = 1,border = 5,bg = '#00ff00',fg = 'black',font =('Helvetica',15,'bold'),command = equal).grid(row = 7,column = 3)
    
    if(x == 0):
        frame2.grid_forget()
    else:
        pass
    frame3.grid(row = 2,column = 0)

basic(0)
win.mainloop()