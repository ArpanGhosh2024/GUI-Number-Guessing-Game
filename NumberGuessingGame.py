from tkinter import *
from tkinter import messagebox
import random
window=Tk()
window.title("Number Guessing Game by Arpan Ghosh")
window.configure(bg="light blue")
window.geometry('700x700')
inc=IntVar() 
inc.set(1) #By default it generates numbers in the range inclusive of start and end
a=IntVar()
a.set(None)
b=IntVar()
b.set(None)
guess=IntVar()
guess.set(None)
def re_play(): #invoked when "Play Again" button is clicked
    try:
        label_user.destroy() #if the game is played again, destroy the widgets(here all Labels) that contained information about the previous play
    except NameError:
        pass
    
    try:
        label_random.destroy()
    except NameError:
        pass
    
    try:
        lb.destroy()
    except NameError:
        pass

    b1['state']=NORMAL #to again set the "Play" button to active state
    b2['state']=DISABLED #to disable or gray-out the "Play Again" button

def fun(): #function to be invoked when the "Play" is clicked
    b1['state']=DISABLED  #to disable or gray-out the "Play" button
    b2['state']=NORMAL #to set the "Play Again" button to active state
    global label_user
    global label_random
    global lb
    if(not e1.get() or not e2.get()): #if either of the limits are not entered then not(False) will evaluate to True and the whole if condition is True
        messagebox.showerror("Limit Error","Both the limits must be entered.")
    a=e1.get()
    b=e2.get()
    if(int(a)>int(b)): #if start limit is greater than end limit raise an error
        messagebox.showerror("Limit Error","Start cannot be greater than end.")     
    guess=e3.get() #user guess
    if(inc.get()==1): #if user chooses to include both start and end values of the range.(By default it is included)
        rn=random.randint(int(a),int(b))
    else: #if inc==0 then it is exclusive of start and end values
        if(int(b)-int(a)>=2): #in case the end points are excluded there must be atleast one value in between otherwise raise error
            rn=random.randint(int(a)+1,int(b)-1)
        else:
            messagebox.showerror("Limit Error","For range exclusive of start and end,start and end values must alteast have a difference of 2.")
    label_user=Label(window,text="User's Guess : "+guess,font=("Helvetica",10,"bold"),bg="light blue")
    label_user.pack(pady=5)
    label_random=Label(window,text="Actual Random Number Generated : "+str(rn),font=("Helvetica",10,"bold"),bg="light blue")
    label_random.pack(pady=5)
    if(not guess): #if user has not guessed anything
        messagebox.showerror("Missing User Guess","No user guess given.")
    else: #user has made some guess irrespective of whether it is right or wrong  
        if(rn==int(guess)):
            lb=Label(window,text="Congratulations!!!You guessed the number correctly.",font=("Helvetica",10,"bold"),bg="light green")
            lb.pack(pady=5)
        else:
            lb=Label(window,text="Hard Luck, Your guess was not right.",font=("Helvetica",10,"bold"),bg="red")
            lb.pack(pady=5)


l1=Label(window,text="Number Guessing Game",font=("Bookman Old Style",18,"bold"),bg="light blue")
l1.pack(pady=10)
l2=Label(window,text="Enter the range that you want the numbers to be generated within:-",font=("Helvetica",15,"bold"),bg="light blue")
l2.pack(pady=15)
l3=Label(window,text="Enter the start value of the range:-",font=("Helvetica",10,"bold"),bg="light blue")
l3.pack()
e1=Entry(window)
e1.pack()
le=Label(window,bg="light blue").pack(pady=10)
l4=Label(window,text="Enter the end value of the range:-",font=("Helvetica",10,"bold"),bg="light blue")
l4.pack()
e2=Entry(window)
e2.pack()
le=Label(window,bg="light blue").pack(pady=10)
r1=Radiobutton(window,text="Include the start and end values of the range",font=("Helvetica",10,"bold"),variable=inc,value=1,bg="light blue")
r1.pack()
r2=Radiobutton(window,text="Exclude the start and end values of the range (start and end must atleast have a difference of 2)",font=("Helvetica",10,"bold"),variable=inc,value=0,bg="light blue")
r2.pack()
le=Label(window,bg="light blue").pack(pady=10)
l5=Label(window,text="Enter your Guess...",font=("Helvetica",10,"bold"),bg="light blue").pack()
e3=Entry(window)
e3.pack()
b1=Button(window,text="Play",command=fun,font=("Helvetica",10,"bold"),bg="light green",activebackground="black",activeforeground="light green")
b1.pack(pady=10)
b2=Button(window,text="Play Again",command=re_play,state=DISABLED,font=("Helvetica",10,"bold"),bg="orange",activebackground="black",activeforeground="orange")
b2.pack(pady=10)
b3=Button(window,text="Quit",command=window.destroy,font=("Helvetica",10,"bold"),bg="red",activebackground="black",activeforeground="red")
b3.pack(pady=10)
window.mainloop()