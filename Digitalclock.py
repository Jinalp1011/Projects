from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')   # it will give only hour from the given time
    mi = time.strftime('%M')   #only counts min
    sec = time.strftime('%S')   #only seconds
    am = time.strftime("%p")
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')


    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_yr.config(text=year)
    lab_mon.config(text=month)
    lab_date.config(text=date)
    lab_day.config(text=day)

    lab_hr.after(200,date_time)    #it will recall the data means change the data


clock = Tk()
clock.title('    Digital Clock')
clock.geometry('1000x500')  #size of box
clock.config(bg = 'black')

#time

lab_hr = Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='white',fg="black")
lab_hr.place(x = 120 , y = 50 ,height =110,width=100)
lab_hr_txt = Label(clock,text="Hour",font=('Times New Roman',20,"bold"),bg='white',fg="black")
lab_hr_txt.place(x = 120 , y = 190 ,height =40,width=100)

lab_min = Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='white',fg="black")
lab_min.place(x = 340 , y = 50 ,height =110,width=110)
lab_min_txt = Label(clock,text="Min",font=('Times New Roman',20,"bold"),bg='white',fg="black")
lab_min_txt.place(x = 340 , y = 190 ,height =40,width=100)

lab_sec = Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='white',fg="black")
lab_sec.place(x = 560 , y = 50 ,height =110,width=110)
lab_sec_txt = Label(clock,text="Sec",font=('Times New Roman',20,"bold"),bg='white',fg="black")
lab_sec_txt.place(x = 560 , y = 190 ,height =40,width=100)

lab_am = Label(clock,text="00",font=('Times New Roman',60,"bold"),bg='white',fg="black")
lab_am.place(x = 780 , y = 50 ,height =110,width=110)
lab_am_txt = Label(clock,text="AM.PM",font=('Times New Roman',20,"bold"),bg='white',fg="black")
lab_am_txt.place(x = 780 , y = 190 ,height =40,width=100)


# date

lab_date = Label(clock,text="00",font=('Times New Roman',40,"bold"),bg='white',fg="black")
lab_date.place(x = 120 , y = 270 ,height =110,width=100)
lab_date_txt = Label(clock,text="Date",font=('Times New Roman',20,"bold"),bg='white',fg="black")
lab_date_txt.place(x = 120 , y = 410 ,height =40,width=100)

lab_mon = Label(clock,text="00",font=('Times New Roman',40,"bold"),bg='white',fg="black")
lab_mon.place(x = 340 , y = 270 ,height =110,width=100)
lab_mon_txt = Label(clock,text="Month",font=('Times New Roman',20,"bold"),bg='white',fg="black")
lab_mon_txt.place(x = 340 , y = 410 ,height =40,width=100)

lab_yr = Label(clock,text="00",font=('Times New Roman',40,"bold"),bg='white',fg="black")
lab_yr.place(x = 560 , y = 270 ,height =110,width=100)
lab_yr_txt = Label(clock,text="Year",font=('Times New Roman',20,"bold"),bg='white',fg="black")
lab_yr_txt.place(x = 560 , y = 410 ,height =40,width=100)

lab_day = Label(clock,text="00",font=('Times New Roman',40,"bold"),bg='white',fg="black")
lab_day.place(x = 780 , y = 270 ,height =110,width=110)
lab_day_txt = Label(clock,text="DAY",font=('Times New Roman',20,"bold"),bg='white',fg="black")
lab_day_txt.place(x = 780 , y = 410 ,height =40,width=100)

date_time()

clock.mainloop()  #continuous loop that will always be on