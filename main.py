
from tkinter import * 
import tkinter as tk  
from tkinter import messagebox
from fpdf import FPDF
master = Tk()  
def add(value):
    
    pdf = FPDF()
    pdf.add_page()

    for i in range(len(all_details)):
        if i==0:
            pdf.set_text_color(0,181,226)
            pdf.set_font("Arial","B",size=20) # For title text
            pdf.cell(w=0,h=0,txt=all_details[i],ln=1,align="L")
        
        elif i==1:
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=0,txt=all_details[i],align="R")
        else:

            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=10,txt=all_details[i],align="R") 
            
    if len(all_edu)>0:
        pdf.cell(w=0,h=4,txt='',ln=1,align="L")
        text="Education :"
        pdf.set_text_color(0,181,226)
        pdf.set_font("Arial","B",size=15) # For title text
        pdf.cell(w=0,h=10,txt=text,ln=1,align="L")  
        #pdf.ln(0.15)      
        for i in range(len(all_edu)):
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial","B",size=14) # For title text
            pdf.multi_cell(w=0,h=5,txt=all_edu[i][0]+" :",align="L")
            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=5,txt=all_edu[i][1],align="L")
    
    if len(all_exp)>0 and all_exp[0][1]!='NA' and value!=2:
        pdf.cell(w=0,h=4,txt='',ln=1,align="L")
        text="Experience :"
        pdf.set_text_color(0,181,226)
        pdf.set_font("Arial","B",size=15) # For title text
        pdf.cell(w=0,h=10,txt=text,ln=1,align="L")        
        for i in range(len(all_exp)):
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial","B",size=14) # For title text
            pdf.multi_cell(w=0,h=5,txt=all_exp[i][0]+" :",align="L")
            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=5,txt=all_exp[i][1],align="L")
            
    if len(all_pro)>0:
        pdf.cell(w=0,h=4,txt='',ln=1,align="L")
        text="Projects :"
        pdf.set_text_color(0,181,226)
        pdf.set_font("Arial","B",size=15) # For title text
        pdf.cell(w=0,h=10,txt=text,ln=1,align="L")        
        for i in range(len(all_pro)):
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial","B",size=14) # For title text
            pdf.multi_cell(w=0,h=5,txt=all_pro[i][0]+" :",align="L")
            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=5,txt=all_pro[i][1],align="L")
            
    if len(all_certi)>0:
        pdf.cell(w=0,h=4,txt='',ln=1,align="L")
        text="Certificates :"
        pdf.set_text_color(0,181,226)
        pdf.set_font("Arial","B",size=15) # For title text
        pdf.cell(w=0,h=10,txt=text,ln=1,align="L")        
        for i in range(len(all_certi)):
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial","B",size=14) # For title text
            pdf.multi_cell(w=0,h=5,txt=all_certi[i][0]+" :",align="L")
            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=5,txt=all_certi[i][1],align="L")

    if len(all_acheive)>0 and all_acheive[0]!='NA':
        pdf.cell(w=0,h=4,txt='',ln=1,align="L")
        text="Acheivements/Rewards :"
        pdf.set_text_color(0,181,226)
        pdf.set_font("Arial","B",size=15) # For title text
        pdf.cell(w=0,h=10,txt=text,ln=1,align="L")        
        for i in range(len(all_acheive)):
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=5,txt=all_acheive[i],align="L")
            
    if len(all_tech)>0:
        pdf.cell(w=0,h=4,txt='',ln=1,align="L")
        text="Technologies/Skills :"
        pdf.set_text_color(0,181,226)
        pdf.set_font("Arial","B",size=15) # For title text
        pdf.cell(w=0,h=10,txt=text,ln=1,align="L")        
        for i in range(len(all_tech)):
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=5,txt=all_tech[i],align="L")

    if len(all_profile)>0:
        pdf.cell(w=0,h=4,txt='',ln=1,align="L")
        text="Socials profiles :"
        pdf.set_text_color(0,181,226)
        pdf.set_font("Arial","B",size=15) # For title text
        pdf.cell(w=0,h=10,txt=text,ln=1,align="L")        
        for i in range(len(all_profile)):
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial",size=13) # For paragraph text
            pdf.multi_cell(w=0,h=5,txt=all_profile[i],align="L")
    save=all_details[0]+"_resume.pdf"
    pdf.output(save)
    messagebox.showinfo( "Done","Successfuuly created")


all_details=[]
def add_details(mess):
    s=""
    result=mess.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s=s+i
    all_details.append(s)
    mess.delete('1.0', END)
    print('all_details',all_details)
    return 

def clear_details(mess):
    all_details.clear()
    mess.delete('1.0', END)
    print(all_details)
    
def stop_adding_details(mess):
    s=""
    result=mess.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s=s+i
    all_details.append(s)
    print(all_details)

all_exp=[]
def add_exp(title_exp,explain_exp):
    s1=""
    result=title_exp.get(1.0, tk.END+"-1c")
    print('res',result)
    for i in result:
        if i!='\n':
            s1=s1+i
    s2=""
    result=explain_exp.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s2=s2+i
    all_exp.append([s1,s2])
    title_exp.delete('1.0',END)
    explain_exp.delete('1.0',END)
    print('all_exp',all_exp)
    return 

def clear_exp(title_exp,explain_exp):
    all_exp.clear()
    print(all_exp)
    title_exp.delete('1.0',END)
    explain_exp.delete('1.0',END)
    return

def stop_adding_exp(title_exp,explain_exp):
    s1=""
    result=title_exp.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s1=s1+i
    s2=""
    result=explain_exp.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s2=s2+i
    all_exp.append([s1,s2])
    print(all_exp)

all_certi=[]
def add_certi(title_certi,explain_certi):
    s1=""
    result=title_certi.get(1.0, tk.END+"-1c")
    print('res',result)
    for i in result:
        if i!='\n':
            s1=s1+i
    s2=""
    result=explain_certi.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s2=s2+i
    all_certi.append([s1,s2])
    title_certi.delete('1.0',END)
    explain_certi.delete('1.0',END)
    print('all_certi',all_certi)
    return 

def clear_certi(title_certi,explain_certi):
    all_certi.clear()
    title_certi.delete('1.0',END)
    explain_certi.delete('1.0',END)
    print(all_certi)
    return

def stop_adding_certi(title_certi,explain_certi):
    s1=""
    result=title_certi.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s1=s1+i
    s2=""
    result=explain_certi.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s2=s2+i
    all_certi.append([s1,s2])
    print(all_certi)

all_edu=[]
def add_edu(title_education,explain_edu):
    s1=""
    result=title_education.get(1.0, tk.END+"-1c")
    print('res',result)
    for i in result:
        if i!='\n':
            s1=s1+i
    s2=""
    result=explain_edu.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s2=s2+i
    all_edu.append([s1,s2])
    title_education.delete('1.0',END)
    explain_edu.delete('1.0',END)
    print('all_edu',all_edu)
    return 

def clear_edu(title_education,explain_edu):
    all_edu.clear()
    title_education.delete('1.0',END)
    explain_edu.delete('1.0',END)
    print(all_edu)
    return

def stop_adding_edu(title,explain):
    s1=""
    result=title.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s1=s1+i
    s2=""
    result=explain.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s2=s2+i
    all_edu.append([s1,s2])
    print(all_edu)

all_pro=[]
def add_pro(title_pro,explain_pro):
    s1=""
    result=title_pro.get(1.0, tk.END+"-1c")
    print('res',result)
    for i in result:
        if i!='\n':
            s1=s1+i
    s2=""
    result=explain_pro.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s2=s2+i
    all_pro.append([s1,s2])
    title_pro.delete('1.0',END)
    explain_pro.delete('1.0',END)
    print('all_pro',all_pro)
    return 

def clear_pro(title_pro,explain_pro):
    all_pro.clear()
    title_pro.delete('1.0',END)
    explain_pro.delete('1.0',END)
    print(all_pro)
    return

def stop_adding_pro(title_pro,explain_pro):
    s1=""
    result=title_pro.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s1=s1+i
    s2=""
    result=explain_pro.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s2=s2+i
    all_pro.append([s1,s2])
    
    print(all_pro)

all_web=[]
def add_web(title_Website):
    s1=""
    result=title_Website.get(1.0, tk.END+"-1c")
    print('res',result)
    for i in result:
        if i!='\n':
            s1=s1+i
    all_web.append(s1)
    title_Website.delete('1.0',END)
    print('all_web',all_web)
    return 

def clear_web(title_Website):
    all_web.clear()
    title_Website.delete('1.0',END)
    print(all_web)
    return
def stop_adding_web(title_Website):
    s1=""
    result=title_Website.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s1=s1+i
    all_web.append(s1)
    print(all_web)

all_acheive=[]
def add_acheive(title_acheive):
    s1=""
    result=title_acheive.get(1.0, tk.END+"-1c")
    print('res',result)
    for i in result:
        if i!='\n':
            s1=s1+i
    all_acheive.append(s1)
    title_acheive.delete('1.0',END)
    print('all_acheive',all_acheive)
    return 

def clear_acheive(title_acheive):
    all_acheive.clear()
    title_acheive.delete('1.0',END)
    print(all_acheive)
    return

def stop_adding_acheive(title_acheive):
    s1=""
    result=title_acheive.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s1=s1+i
    all_acheive.append(s1)
    print(all_acheive)
    return

all_tech=[]
def add_tech(title_tech):
    s1=""
    result=title_tech.get(1.0, tk.END+"-1c")
    print('res',result)
    for i in result:
        if i!='\n':
            s1=s1+i
    all_tech.append(s1)
    title_tech.delete('1.0',END)
    print('all_tech',all_tech)
    return 
def clear_tech(title_tech):
    all_tech.clear()
    title_tech.delete('1.0',END)
    print(all_tech)
    return
def stop_adding_tech(title_tech):
    s1=""
    result=title_tech.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s1=s1+i
    all_tech.append(s1)
    print(all_tech)
    return


all_profile=[]
def add_profile(title_profile):
    s1=""
    result=title_profile.get(1.0, tk.END+"-1c")
    print('res',result)
    for i in result:
        if i!='\n':
            s1=s1+i
    all_profile.append(s1)
    title_profile.delete('1.0',END)
    print('all_profile',all_profile)
    return 

def clear_profile(title_profile):
    all_profile.clear()
    title_profile.delete('1.0',END)
    print(all_profile)
    return
def stop_adding_profile(title_profile):
    s1=""
    result=title_profile.get(1.0, tk.END+"-1c")
    for i in result:
        if i!='\n':
            s1=s1+i
    all_profile.append(s1)
    print(all_profile)
    return

def Done_mess(value):
    child=Toplevel(master)
    child.geometry('1600x1000')
    s1=Label(child,text="Details",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=20,y=40)
    mess=Text(child,font=35)
    mess.place(x = 200, y = 40,width=300,height=50)
    Add1=Button(child, text ="Add", command = lambda :add_details(mess),font=20,bg='blue',fg='pink')
    Add1.place(x=530,y=50)
    Clear1=Button(child, text ="Clear", command = lambda :clear_details(mess),font=20,bg='blue',fg='pink')
    Clear1.place(x=580,y=50)
    stop1=Button(child, text ="Stop Adding", command = lambda :stop_adding_details(mess),font=20,bg='blue',fg='pink')
    stop1.place(x=650,y=50)
    

    s1=Label(child,text="Experience",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=20,y=160)
    title_exp=Text(child,font=35)
    title_exp.place(x = 200, y = 130,width=300,height=30)
    explain_exp=Text(child,font=35)
    explain_exp.place(x = 200, y = 170,width=300,height=100)

    Add2=Button(child, text ="Add", command = lambda : add_exp(title_exp,explain_exp),font=20,bg='blue',fg='pink')
    Add2.place(x=530,y=160)
    Clear2=Button(child, text ="Clear", command = lambda : clear_exp(title_exp,explain_exp),font=20,bg='blue',fg='pink')
    Clear2.place(x=580,y=160)
    stop2=Button(child, text ="Stop Adding", command = lambda :stop_adding_exp(title_exp,explain_exp),font=20,bg='blue',fg='pink')
    stop2.place(x=650,y=160)
    

    s1=Label(child,text="Certificates",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=900,y=160)
    title_certi=Text(child,font=35)
    title_certi.place(x = 1100, y = 130,width=300,height=30)
    explain_certi=Text(child,font=35)
    explain_certi.place(x = 1100, y = 170,width=300,height=100)
    Add3=Button(child, text ="Add", command = lambda : add_certi(title_certi,explain_certi),font=20,bg='blue',fg='pink')
    Add3.place(x=1420,y=130)
    Clear3=Button(child, text ="Clear", command = lambda :clear_certi(title_certi,explain_certi),font=20,bg='blue',fg='pink')
    Clear3.place(x=1420,y=180)
    stop3=Button(child, text ="Stop", command = lambda :stop_adding_certi(title_certi,explain_certi),font=20,bg='blue',fg='pink')
    stop3.place(x=1420,y=230)

    
    s1=Label(child,text="Education",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=20,y=350)
    title_education=Text(child,font=35)
    title_education.place(x = 200, y = 310,width=300,height=30)
    explain_edu=Text(child,font=35)
    explain_edu.place(x = 200, y = 350,width=300,height=100)
    Add4=Button(child, text ="Add", command = lambda : add_edu(title_education,explain_edu),font=20,bg='blue',fg='pink')
    Add4.place(x=530,y=333)
    Clear4=Button(child, text ="Clear", command = lambda :clear_edu(title_education,explain_edu),font=20,bg='blue',fg='pink')
    Clear4.place(x=590,y=333)
    stop4=Button(child, text ="Stop", command = lambda :stop_adding_edu(title_education,explain_edu),font=20,bg='blue',fg='pink')
    stop4.place(x=660,y=333)


    s1=Label(child,text="Acheivements/Rewards",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=870,y=350)
    title_acheive=Text(child,font=35)
    title_acheive.place(x = 1100, y = 350,width=300,height=100)
    Add6=Button(child, text ="Add", command = lambda : add_acheive(title_acheive),font=20,bg='blue',fg='pink')
    Add6.place(x=1420,y=330)
    Clear6=Button(child, text ="Clear", command =lambda : clear_acheive(title_acheive),font=20,bg='blue',fg='pink')
    Clear6.place(x=1420,y=373)
    stop6=Button(child, text ="Stop", command = lambda :stop_adding_acheive(title_acheive),font=20,bg='blue',fg='pink')
    stop6.place(x=1420,y=415)
    
    s1=Label(child,text="Projects",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=20,y=510)
    title_pro=Text(child,font=35)
    title_pro.place(x = 200, y = 480,width=300,height=30)
    explain_pro=Text(child,font=35)
    explain_pro.place(x = 200, y = 520,width=300,height=100)
    Add4=Button(child, text ="Add", command = lambda : add_pro(title_pro,explain_pro),font=20,bg='blue',fg='pink')
    Add4.place(x=530,y=533)
    Clear4=Button(child, text ="Clear", command =lambda :  clear_pro(title_pro,explain_pro),font=20,bg='blue',fg='pink')
    Clear4.place(x=590,y=533)
    stop4=Button(child, text ="Stop", command = lambda :stop_adding_pro(title_pro,explain_pro),font=20,bg='blue',fg='pink')
    stop4.place(x=660,y=533)


    s1=Label(child,text="Technologies/Skills",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=900,y=510)
    title_tech=Text(child,font=35)
    title_tech.place(x = 1100, y = 510,width=300,height=100)
    Add7=Button(child, text ="Add", command = lambda : add_tech(title_tech),font=20,bg='blue',fg='pink')
    Add7.place(x=1420,y=480)
    Clear7=Button(child, text ="Clear", command =lambda :  clear_tech(title_tech),font=20,bg='blue',fg='pink')
    Clear7.place(x=1420,y=523)
    stop7=Button(child, text ="Stop", command = lambda :stop_adding_tech(title_tech),font=20,bg='blue',fg='pink')
    stop7.place(x=1420,y=565)


    s1=Label(child,text="Any Website",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=20,y=650)
    title_Website=Text(child,font=35)
    title_Website.place(x = 200, y = 650,width=300,height=50)
    Add5=Button(child, text ="Add", command = lambda :add_web(title_Website),font=20,bg='blue',fg='pink')
    Add5.place(x=530,y=650)
    Clear5=Button(child, text ="Clear", command =  lambda :clear_web(title_Website),font=20,bg='blue',fg='pink')
    Clear5.place(x=584,y=650)
    stop5=Button(child, text ="Stop", command = lambda :stop_adding_web(title_Website),font=20,bg='blue',fg='pink')
    stop5.place(x=650,y=650)


    s1=Label(child,text="Social profiles",fg='red')
    s1.config(width=20,font=30)
    s1.place(x=900,y=650)
    title_profile=Text(child,font=35)
    title_profile.place(x = 1100, y = 650,width=300,height=50)
    Add8=Button(child, text ="Add", command = lambda : add_profile(title_profile),font=20,bg='blue',fg='pink')
    Add8.place(x=1420,y=650)
    Clear8=Button(child, text ="Clear", command = lambda : clear_profile(title_profile),font=20,bg='blue',fg='pink')
    Clear8.place(x=1420,y=693)
    stop8=Button(child, text ="Stop", command = lambda :stop_adding_profile(title_profile),font=20,bg='blue',fg='pink')
    stop8.place(x=1420,y=735)



    Add2=Button(child, text ="Generate Resume :-)",  command = lambda:add(value),font=20,bg='blue',fg='pink')
    Add2.place(x=700,y=740)
    mainloop()

        
master.geometry('1800x1800') 
l2 = Label (master, text="Resume Builder ",fg='Red',bg='Yellow',font=("Arial Bold", 20))
l2.config(width=20)
l2.place(x=600,y=0)
l1 = Label (master, text="Instruction : In Detail section please fill only  these three necessary things     \n 1) Your Full Name \n 2) Email address , Phone number \n 3) Job title or in which you are proficient \n Eg; I am proficient in python , coding enthusiastic and web developer \n In Skills Section fill all the Skills which you have acquired , in single with proper spacing \n  Eg; Web development , Android development , Python/C++ , Django , Html/Css , Dbms etc  \n In remaining section you can fill whatever you want in any order , Fill that section first \n which you want at the top and make it concise and simple eg; 3 Project and for each 1-2 \n line description , 4-5  Skills , 4-5 Certificates , 2-3 Acheivement/Rewards if you have , 2-3 \n Social Profiles and in Website Section do not fill any links/details leave it as Empty \n In Acheivement Section if you don't have anything to fill , Write in description 'NA' \n Smaller box/First box for Heading and Larger block/Second box for Description " ,bg='green',fg='pink',font=("Arial Bold", 20))
l1.config(width=90)
l1.place(x=0,y=34)

photo1 = PhotoImage(file = "resume.png")
photo2 = PhotoImage(file = "resume1.png")
# entry widgets, used to take entry from user 
e1 = Button(master,  command =lambda: Done_mess(1),image=photo1)
e2 = Button(master,  command =lambda: Done_mess(2),image=photo2)
# this will arrange entry widgets 
#e1.grid(row = 1, column = 0) 
e1.place(x=1,y=460)
l2 = Label (master, text="For Experienced",bg='green',fg='pink',font=("Arial Bold", 20))
l2.config(width=15)
l2.place(x=330,y=460)

l3 = Label (master, text="For Fresher",bg='green',fg='pink',font=("Arial Bold", 20))
l3.config(width=15)
l3.place(x=940,y=460)
e2.place(x=1220,y=455)
# adding image (remember image should be PNG and not JPG) 
# this will arrange entry widgets 
e1.config(width=300,height=321)
e2.config(width=300,height=319)

mainloop()


