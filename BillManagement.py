from tkinter import *
import emoji
root=Tk()
root.geometry('1000x550')
root.title('Bill Management')
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_Noodles.delete(0,END)
    entry_Idly.delete(0,END)
    entry_Tea.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Juice.delete(0,END)
    entry_Poori.delete(0,END)
    Print_Bill()

def Total():
    try:a1=int(dosa.get())
    except: a1=0

    try:a2=int(Noodles.get())
    except: a2=0

    try:a3=int(Idly.get())
    except: a3=0

    try:a4=int(Tea.get())
    except: a4=0

    try:a5=int(Coffee.get())
    except: a5=0

    try:a6=int(Juice.get())
    except: a6=0

    try:a7=int(Poori.get())
    except: a7=0

    #define cost of each item per quantity
    c1=60*a1
    c2=30*a2
    c3=40*a3
    c4=20*a4
    c5=30*a5
    c6=50*a6
    c7=45*a7

    lbl_total=Label(f2,font=("aria",20,'bold'),text='Total',width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)

def Print_Bill():
    items = [("Dosa", dosa.get(), 60), ("Noodles", Noodles.get(), 30), ("Idly", Idly.get(), 40),
             ("Tea", Tea.get(), 20), ("Coffee", Coffee.get(), 30), ("Juice", Juice.get(), 50), ("Poori", Poori.get(), 45)]
    bill_output = "\nItem Name,\tQty\tPrice\n-------------------------------------------------\n"
    total_price = 0
    for item, qty, price in items:
        if qty:
            try:
                qty = int(qty)
                if qty > 0:
                    cost = qty * price
                    total_price += cost
                    bill_output += f"{item}\t\t{qty}\tRs.{cost}/-\n"
            except:
                pass
    bill_output += f"\nTotal:  Rs. {total_price}/-\n\n"+emoji.emojize(':grinning_face_with_big_eyes:')+"Thank You and Visit Again "+emoji.emojize(':grinning_face_with_big_eyes:')
    bill_text.set(bill_output)



Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33), width="300",height="2").pack()

#MENU CARD
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)
Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa........Rs.60/plate",fg='black',bg='lightgreen').place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Noodles........Rs.30/plate",fg='black',bg='lightgreen').place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Idly........Rs.40/plate",fg='black',bg='lightgreen').place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Tea........Rs.20/glass",fg='black',bg='lightgreen').place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Coffee........Rs.30/glass",fg='black',bg='lightgreen').place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Juice........Rs.50/glass",fg='black',bg='lightgreen').place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Poori........Rs.45/plate",fg='black',bg='lightgreen').place(x=10,y=260)


#BILL
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)
Bill=Label(f2,text="BILL",font=('calibri',20,'bold'),bg="lightyellow")
Bill.place(x=120,y=10)

bill_text = StringVar()
bill_display = Label(f2, textvariable=bill_text, bg="lightyellow", font=('calibri', 12), justify=LEFT, anchor='w')
bill_display.place(x=10, y=50)




#ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

dosa=StringVar()
Noodles=StringVar()
Idly=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
Poori=StringVar()
Total_bill=StringVar()


#Label
lbl_dosa=Label(f1,font=('aria',20,'bold'),text="Dosa",width=12,fg='blue4')
lbl_Noodles=Label(f1,font=('aria',20,'bold'),text="Noodles",width=12,fg='blue4')
lbl_Idly=Label(f1,font=('aria',20,'bold'),text="Idly",width=12,fg='blue4')
lbl_Tea=Label(f1,font=('aria',20,'bold'),text="Tea",width=12,fg='blue4')
lbl_Coffee=Label(f1,font=('aria',20,'bold'),text="Coffee",width=12,fg='blue4')
lbl_Juice=Label(f1,font=('aria',20,'bold'),text="Juice",width=12,fg='blue4')
lbl_Poori=Label(f1,font=('aria',20,'bold'),text="Poori",width=12,fg='blue4')
lbl_dosa.grid(row=1,column=0)
lbl_Noodles.grid(row=2,column=0)
lbl_Idly.grid(row=3,column=0)
lbl_Tea.grid(row=4,column=0)
lbl_Coffee.grid(row=5,column=0)
lbl_Juice.grid(row=6,column=0)
lbl_Poori.grid(row=7,column=0)

#Entry
entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=dosa,bd=6,width=8,bg='lightpink')
entry_Noodles=Entry(f1,font=("aria",20,'bold'),textvariable=Noodles,bd=6,width=8,bg='lightpink')
entry_Idly=Entry(f1,font=("aria",20,'bold'),textvariable=Idly,bd=6,width=8,bg='lightpink')
entry_Tea=Entry(f1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg='lightpink')
entry_Coffee=Entry(f1,font=("aria",20,'bold'),textvariable=Coffee,bd=6,width=8,bg='lightpink')
entry_Juice=Entry(f1,font=("aria",20,'bold'),textvariable=Juice,bd=6,width=8,bg='lightpink')
entry_Poori=Entry(f1,font=("aria",20,'bold'),textvariable=Poori,bd=6,width=8,bg='lightpink')

entry_dosa.grid(row=1,column=1)
entry_Noodles.grid(row=2,column=1)
entry_Idly.grid(row=3,column=1)
entry_Tea.grid(row=4,column=1)
entry_Coffee.grid(row=5,column=1)
entry_Juice.grid(row=6,column=1)
entry_Poori.grid(row=7,column=1)

#Buttons
btn_reset=Button(f1,bd=5,fg="black",bg="red",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

#btn_total=Button(f1,bd=5,fg="black",bg="darkgreen",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
#btn_total.grid(row=8,column=1)

btn_print_bill = Button(f1, bd=5, fg="black", bg="blue", font=("ariel", 16, 'bold'), width=10, text="Print Bill", command=Print_Bill)
btn_print_bill.grid(row=8, column=1, columnspan=2)

Print_Bill()

root.mainloop()