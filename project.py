
#-------------------import-------------------
from tkinter import*

import time  

from tkinter import ttk

from tkinter import messagebox

#----------window----------

win = Tk()

win.title("CAFE REX")

win.geometry("1900x830")

b = 'gainsboro'

list = []

sum = 0

code=StringVar()  
                  
#------------------time--------------

localtime = time.asctime(time.localtime(time.time()))

#---------------function----------------

def clear_orders():
    
    list_orders.delete(0,END)
    
def add_orders():
    
    a = number1.get()
    
    a = int(a)
    
    if('33'==code1.get()):
        
        list_orders.insert(END," 33                     Turk cafe                         {0}                     56T".format(a))
        
        list.append(56*a)
        
    elif('34'==code1.get()):
        
        list_orders.insert(END," 34                     Espresso                         {0}                     40T".format(a))
        
        list.append(40*a)
        
    elif('40'==code1.get()):
        
        list_orders.insert(END," 40                     Espresso duble                {0}                     45T".format(a))
        
        list.append(45*a)
        
    elif('44'==code1.get()):
        
        list_orders.insert(END," 44                     Espresso Macchiato         {0}                     55T".format(a))
        
        list.append(55*a)
        
    elif('42'==code1.get()):
        
        list_orders.insert(END," 42                     Late Cafe                         {0}                     60T".format(a))
        
        list.append(60*a)
        
    elif('46'==code1.get()):
        
        list_orders.insert(END," 46                     Cafe Americano                {0}                     43T".format(a))
        
        list.append(43*a)
        
    elif('49'==code1.get()):
        
        list_orders.insert(END," 49                     Water                              {0}                     5T".format(a))
        
        list.append(5*a)
        
    elif('45'==code1.get()):
        
        list_orders.insert(END," 45                     Orange juice                     {0}                     20T".format(a))
        
        list.append(20*a)
        
    elif('32'==code1.get()):
        
        list_orders.insert(END," 32                     Soft drink                         {0}                     15T".format(a))
        
        list.append(15*a)
        
    elif('31'==code1.get()):
        
        list_orders.insert(END," 31                     Dough                              {0}                     22T".format(a))
        
        list.append(22*a)
        
    elif('30'==code1.get()):
        
        list_orders.insert(END," 30                     Pomegranate juice             {0}                     19T".format(a))
        
        list.append(19*a)
        
    elif('50'==code1.get()):
        
        list_orders.insert(END," 50                     Pizza                                {0}                     190T".format(a))
        
        list.append(190*a)
        
    elif('55'==code1.get()):
        
        list_orders.insert(END," 55                     Sushi                                {0}                     250T".format(a))
        
        list.append(250*a)
        
    elif('52'==code1.get()):
        
        list_orders.insert(END," 52                     Pasta                                {0}                     213T".format(a))
        
        list.append(213*a)
        
    elif('53'==code1.get()):
        
        list_orders.insert(END," 53                     Hamburger                         {0}                     150T".format(a))
        
        list.append(150*a)
        
    elif('60'==code1.get()):
        
        list_orders.insert(END," 60                     Hotdog                              {0}                     210T".format(a))
        
        list.append(210*a)
        
    else:
        
        list_orders.insert(END,"-----error-----")
        
def exit():
    
    error = messagebox.askyesno("Warning","Close the program.",)
    
    if(error == True):
        
        win.destroy()
        
def reset():
    
    code1.set("")
    
    number1.set("")
    
    tax1.set("")
    
    cost1.set("")
    
    subtotal1.set("")
    
    total1.set("")
    
    list_orders.delete(1,END)
    
    number1.set(1)
    
    service1.set("")
    
def tooo():
    
    sum = 0
    
    for item in list:
        
        sum+=item
        
        list.remove(item)
        
    costofmeal_t = "T.",str('%.2f'% sum)
    
    PayTax_t=(sum*0.33)
    
    Totalcost_t=sum
    
    Ser_Charge_t=(sum/99)
    
    Service_t="T.",str('%.2f'% Ser_Charge_t)
    
    OverAllCost_t="T.",str( PayTax_t + Totalcost_t + Ser_Charge_t)
    
    PaidTax_t="T.",str('%.2f'% PayTax_t)
    

    tax1.set(PaidTax_t)
    
    cost1.set(costofmeal_t)
    
    subtotal1.set(costofmeal_t)
    
    total1.set(OverAllCost_t)
    
    service1.set(Service_t)
    
    list_orders.insert(END,"--------------------------------------------")
    
    list_orders.insert(END,OverAllCost_t)
    
    sum = 0
    
    print(list,sum)
    
def menu():
    
    menu =Tk()
    
    menu.geometry("1400x600")
    
    menu.title("Menu")

#-----------lable frame--------------

    coffee = LabelFrame(menu,text="Coffee")
    
    Breverages = LabelFrame(menu,text="Breverages")
    
    food = LabelFrame(menu,text="Food")
    
# ----------config-------------

    coffee.config(background='white',fg='red',border=10,width=13000,height=100)
    
    Breverages.config(background='white',fg='red',bd=10,width=13000,height=100)
    
    food.config(background='white',fg='red',bd=10,width=13000,height=100)
    
#-------------------------------------------lable----------------------------

# --------------Label coffee------------

    Label(coffee,text="item",bg='white',font=( 'aria' ,15, 'bold' ),fg='blue').grid(padx=100,row=0,column=1)
    
    Label(coffee,bg='white',fg='white',font=( 'aria' ,15, 'bold' ),text="-----------------------------------------------------------------------------------------------------").grid(row=0,column=2)
    
    Label(coffee,text="Price",bg='white',font=( 'aria' ,15, 'bold' ),fg='blue').grid(padx=100,row=0,column=3)
    
# -------------------------------------------

    Label(coffee,text="Turk coffee",bg='white',).grid(padx=100,row=1,column=1)
    
    Label(coffee,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=1,column=2)
    
    Label(coffee,text="56 T",bg='white',).grid(padx=100,row=1,column=3)
    
# ---------------------------------------

    Label(coffee,text="Espresso",bg='white',).grid(padx=100,row=2,column=1)
    
    Label(coffee,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=2,column=2)
    
    Label(coffee,text="40 T",bg='white',).grid(padx=100,row=2,column=3)
    
# -----------------------------------------

    Label(coffee,text="Espresso double",bg='white',).grid(padx=100,row=3,column=1)
    
    Label(coffee,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=3,column=2)
    
    Label(coffee,text="45 T",bg='white',).grid(padx=100,row=3,column=3)
    
# ---------------------------------------------

    Label(coffee,text="Espresso Macchiato",bg='white',).grid(padx=100,row=4,column=1)
    
    Label(coffee,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=4,column=2)
    
    Label(coffee,text="55 T",bg='white',).grid(padx=100,row=4,column=3)
    
# -------------------------------------------

    Label(coffee,text="Late cafe",bg='white',).grid(padx=100,row=6,column=1)
    
    Label(coffee,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=6,column=2)
    
    Label(coffee,text="60 T",bg='white',).grid(padx=100,row=6,column=3)
    
# --------------------------------------------------

    Label(coffee,text="Cafe Americano",bg='white',).grid(padx=100,row=7,column=1)
    
    Label(coffee,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=7,column=2)
    
    Label(coffee,text="43 T",bg='white',).grid(padx=100,row=7,column=3)
    
# ---------------------------Label Breverages-------------------------

    Label(Breverages,text="item",bg='white',font=( 'aria' ,15, 'bold' ),fg='blue').grid(padx=100,row=0,column=1)
    
    Label(Breverages,bg='white',fg='white',font=( 'aria' ,15, 'bold' ),text="------------------------------------------------------------------------------------------------------").grid(row=0,column=2)
    
    Label(Breverages,text="Price",bg='white',font=( 'aria' ,15, 'bold' ),fg='blue').grid(padx=100,row=0,column=3)
    
# ----------------------------------

    Label(Breverages,text="Water",bg='white',).grid(padx=100,row=1,column=1)
    
    Label(Breverages,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=1,column=2)
    
    Label(Breverages,text="5 T",bg='white',).grid(padx=100,row=1,column=3)
    
# ---------------------------------------

    Label(Breverages,text="Orange juice",bg='white',).grid(padx=100,row=2,column=1)
    
    Label(Breverages,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=2,column=2)
    
    Label(Breverages,text="20 T",bg='white',).grid(padx=100,row=2,column=3)
    
# -----------------------------------------

    Label(Breverages,text="Soft drinks",bg='white',).grid(padx=100,row=3,column=1)
    
    Label(Breverages,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=3,column=2)
    
    Label(Breverages,text="15 T",bg='white',).grid(padx=100,row=3,column=3)
    
# ---------------------------------------------

    Label(Breverages,text="Dough",bg='white',).grid(padx=100,row=4,column=1)
    
    Label(Breverages,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=4,column=2)
    
    Label(Breverages,text="22 T",bg='white',).grid(padx=100,row=4,column=3)
    
# -------------------------------------------

    Label(Breverages,text="Pomegranate juice",bg='white',).grid(padx=100,row=6,column=1)
    
    Label(Breverages,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=6,column=2)
    
    Label(Breverages,text="19 T",bg='white',).grid(padx=100,row=6,column=3)
    
# ------------------------Lable food--------------------------

    Label(food,text="item",bg='white',font=( 'aria' ,15, 'bold' ),fg='blue').grid(padx=100,row=0,column=1)
    
    Label(food,bg='white',fg='white',font=( 'aria' ,15, 'bold' ),text="-----------------------------------------------------------------------------------------------------------").grid(row=0,column=2)
    
    Label(food,text="Price",bg='white',font=( 'aria' ,15, 'bold' ),fg='blue').grid(padx=100,row=0,column=3)
    
# ------------------------------

    Label(food,text="Pizza",bg='white',).grid(padx=100,row=1,column=1)
    
    Label(food,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=1,column=2)
    
    Label(food,text="190 T",bg='white',).grid(padx=100,row=1,column=3)
    
# ---------------------------------

    Label(food,text="Sushi",bg='white',).grid(padx=100,row=2,column=1)
    
    Label(food,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=2,column=2)
    
    Label(food,text="250 T",bg='white',).grid(padx=100,row=2,column=3)
    
# ---------------------------------

    Label(food,text="Pasta",bg='white',).grid(padx=100,row=3,column=1)
    
    Label(food,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=3,column=2)
    
    Label(food,text="213 T",bg='white',).grid(padx=100,row=3,column=3)
    
# -------------------------------------

    Label(food,text="hamburger",bg='white',).grid(padx=100,row=4,column=1)
    
    Label(food,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=4,column=2)
    
    Label(food,text="150 T",bg='white',).grid(padx=100,row=4,column=3)
    
# -------------------------

    Label(food,text="Hotdog",bg='white',).grid(padx=100,row=5,column=1)
    
    Label(food,bg='white',fg='gray',text="----------------------------------------------------------------------------------------------------------------------").grid(row=5,column=2)
    
    Label(food,text="210 T",bg='white',).grid(padx=100,row=5,column=3)
    
#-----------pack-------------

    coffee.pack(fill=X)
    
    Breverages.pack(fill=X)
    
    food.pack(fill=X)
    
# ------------------

    menu.mainloop()

# ?????????????????????????????????????????????????????

code1 = StringVar()

number1 = IntVar()

number1.set(1)

tax1 = StringVar()

cost1 = StringVar()

subtotal1 = StringVar()

total1 = StringVar()

service1 = StringVar()

# ----------------Frame---------------

code_item = LabelFrame(win,text="Code Item")

header = Frame(win)

orders = LabelFrame(win,text="orders")

scroll =Scrollbar(orders,)

order = LabelFrame(win,text="order")

box1 = LabelFrame(win,text="cost")

box2 = Frame(win,bg='gainsboro')

#--------------------Lable----------------

name = Label(header,text="  CAFE   REX")

time = Label(header,text=localtime)

list_orders = Listbox(orders)

list_orders.insert(1,"CODE                NAME ITEM                 NUMBER                    ")

Label(code_item,bg='white',text="Turk cofe:33").pack()

Label(code_item,bg='white',text="")# .pack()  :)

Label(code_item,bg='white',text="espresso:").pack()

Label(code_item,bg='white',text="34").pack()

Label(code_item,bg='white',text="espresso duble:").pack()

Label(code_item,bg='white',text="40").pack()

Label(code_item,bg='white',text="espresso macchiato:").pack()

Label(code_item,bg='white',text="44").pack()

Label(code_item,bg='white',text="late cafe:").pack()

Label(code_item,bg='white',text="42").pack()

Label(code_item,bg='white',text="cafe americano:").pack()

Label(code_item,bg='white',text="46").pack()

Label(code_item,bg='white',text="water").pack()

Label(code_item,bg='white',text="49").pack()

Label(code_item,bg='white',text="orange juice:").pack()

Label(code_item,bg='white',text="45").pack()

Label(code_item,bg='white',text="soft drinks:").pack()

Label(code_item,bg='white',text="32").pack()

Label(code_item,bg='white',text="dough:").pack()

Label(code_item,bg='white',text="31").pack()

Label(code_item,bg='white',text="pomegranate juice:").pack()

Label(code_item,bg='white',text="30").pack()

Label(code_item,bg='white',text="pizza:").pack()

Label(code_item,bg='white',text="50").pack()

Label(code_item,bg='white',text="sushi:").pack()

Label(code_item,bg='white',text="55").pack()

Label(code_item,bg='white',text="pasta:").pack()

Label(code_item,bg='white',text="52").pack()

Label(code_item,bg='white',text="hamburger:").pack()

Label(code_item,bg='white',text="53").pack()

Label(code_item,bg='white',text="hotdog:").pack()

Label(code_item,bg='white',text="60").pack()

#-----------

Label(order,text="code :",bg='white',fg='black').grid(column=0,row=0)

code = Entry(order,bg='gainsboro',textvariable=code1).grid(column=1,row=1,padx=10,ipadx=50)

Label(order,text="number :",bg='white',fg='black').grid(column=0,row=3)

number = Entry(order,bg='gainsboro',textvariable=number1).grid(column=1,row=4,padx=10,ipadx=50,pady=5)

b123 = ttk.Button(order,text="save",command=add_orders).place(x=650,y=30,height=50,width=80)    

#------------------------------------

Label(box1,text="tax",bg='white').grid(column=1,row=1)

tax = Entry(box1,bg='gainsboro',textvariable=tax1).grid(column=2,row=2,padx=30,ipadx=50,pady=8)

Label(box1,text="cost",bg='white').grid(column=3,row=3)

cost = Entry(box1,bg='gainsboro',textvariable=cost1).grid(column=4,row=4,padx=30,ipadx=50,pady=8)

Label(box1,text="subtotal",bg='white').grid(column=1,row=5)

subtotal = Entry(box1,bg='gainsboro',textvariable=subtotal1).grid(column=2,row=6,padx=30,ipadx=50,pady=8)

Label(box1,text="total",bg='white').grid(column=3,row=7)

total = Entry(box1,bg='gainsboro',textvariable=total1).grid(column=4,row=8,padx=30,ipadx=50,pady=8)

Label(box1,text="Service",bg='white',fg='black').grid(column=1,row=9,padx=30,ipadx=50)

service = Entry(box1,bg='gainsboro',textvariable=service1).grid(column=2,row=10,padx=30,ipadx=50,pady=8)

#----------------

ttk.Button(box2,text="Menu",command=menu).grid(column=1,row=1,ipadx=60,ipady=5,padx=85,pady=15)

ttk.Button(box2,text="Total",command=tooo).grid(column=2,row=1,ipadx=66,ipady=5,padx=80,pady=15)

ttk.Button(box2,text="Reset",command=reset).grid(column=3,row=1,ipadx=63,ipady=5,padx=80,pady=15)

ttk.Button(box2,text="Exit",command=exit).grid(column=4,row=1,ipadx=20,ipady=5,padx=85,pady=15)

#-------------------config------------------

code_item.config(height=790,width=150,bg='white')

header.config(width=450,height=80,bg='white')

name.config(bg='white',fg='black',font=( 'aria' ,20, ))

time.config(bg='white',fg='blue',font=( 'aria' ,10, ))

orders.config(bg='white',fg='red',width=450)

list_orders.config(bg='white',fg='black',font=( 'aria' ,10, ))

scroll.config(command=list_orders.yview,bg='white')

order.config(width=450,height=200,bg='white')

box1.config(width=790,height=200,bg='white')

# -----------------Pack-------------

code_item.pack(side="right")

header.pack(side="top",fill=X)

name.grid(column=0,row=0)

time.grid(column=0,row=1)

orders.pack(side='top',fill=X)

scroll.pack(side='right',fill='both')

list_orders.pack(fill=X)

order.pack(side='top',fill='x')

box1.pack(side='top',fill=X)

box2.pack(side='top',fill='both')

#-------------mainloop-----------

win.mainloop()
