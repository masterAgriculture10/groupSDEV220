"""
Course Manager GUI App

This program allows users to view and enroll in college courses.

GUI includes: 
- Login window that authenticates users
- Course tab that allows the user to view and select courses to enroll in
- Schedule tab that allows the user to view the courses they are enrolled in
"""

import tkinter as tk
from tkinter import Frame, ttk, font, ANCHOR


database = {"yahya": "1111", "gunnar": "2222", "alvin": "3333", "shanika": "4444"}
print(f'account details: {database}')


class CourseApp(tk.Tk):
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                # the container is where we'll stack a bunch of frames
                # on top of each other, then the one we want visible
                # will be raised above the others
                self.shared_data = {'StartPage':tk.StringVar()}
                container=tk.Frame(self)
                container.pack(side="top", fill="both", expand=True)
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                self.frames = {}
                for Frame in (StartPage, CoursesPage, Sdev153Page, Sdev140Page, Sdev220Page):
                        page_name = Frame.__name__
                        frame = Frame(parent=container, controller=self)
                        self.frames[page_name] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
                        self.show_frame("StartPage")
        

        def show_frame(self, page_name):
                '''Show a frame for the given page name'''
                frame=self.frames[page_name]
                frame.tkraise()

#+++++++++++++++++++++++++
# the StartPage class which hold the login screen
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
# the Frame that control everything we add th the page
        tk.Frame.__init__(self, parent, background='#003366')
        self.controller=controller
        
        self.controller.title('SDEV Courses Registration')
# options for the screen size normal, iconic, withdrawn, or zoomed
        self.controller.state('normal')

# Creat a function to clear the entries Widget conten
        def clear_text():
            user_entry_Box.delete(0, tk.END)
            pin_entry_Box.delete(0, tk.END)


#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the login page
        header_label1 = tk.Label(self, text="SDEV Courses Registration", foreground='White', background='#336699', font=('bold', 50))
        header_label1.pack()

        header_label2 = tk.Label(self, text="Login to Your Account", foreground='White', background='#336699', font=('bold', 50))
        header_label2.pack(pady=30)
# Creat a space lable 003366
        space_label = tk.Label(self, height=5, background='#003366')
        space_label.pack()

# ++++++++++++++++++++++++++++
# Creat a pin Label to ask the user to enter the pin
        user_label = tk.Label(self, text='Enter your Username:', font=15, background='#003366')
        user_label.place(x=8,y=180)


# Creat a entery box, to put the pin
        user = tk.StringVar()      
        user_entry_Box = tk.Entry(self, textvariable=user)
        user_entry_Box.focus_set()
        user_entry_Box.place(x=170, y=180)


#++++++++++++++++++++++++++++ #336699
# Creat a pin Label to ask the user to enter the pin 
        pin_label = tk.Label(self, text='Enter your PIN number:', font=15, background='#003366')
        pin_label.place(x=8,y=210) 

# Creat a entery box, to put the pin
        pin = tk.StringVar()      
        pin_entry_Box = tk.Entry(self, textvariable=pin)
        pin_entry_Box.place(x=170,y=210)

# Creat a login function to check the user validate the user login

        def login_check():
            global database
            if user.get() in database :
                if database[user.get()] == pin.get() :
                        pin.set('')  
                        user.set('')
                        incorrect_login_label['text']=''
                        controller.show_frame('CoursesPage')
                else:
                        incorrect_login_label['text']='Incorrect User or PIN'
            elif pin.get() == '' and user.get() == '':
                    incorrect_login_label['text']=' Login please'
            else:
                incorrect_login_label['text']='Incorrect User or PIN'

        
# creat a Enter Button
        enter_button = tk.Button(self, text='Enter', command=login_check, relief='flat', width=10, )
        enter_button.place(x=10, y=250)

# creat a Exit Button to quit the program
        button_quit = tk.Button(self, text="Exit", command=self.quit,relief='flat', width=10,)
        button_quit.place(x=180, y=250)
# creat a Clear Button to Clear the login text
        button_clear = tk.Button(self, text="Clear", command=clear_text,relief='flat', width=10,)
        button_clear.place(x=350, y=250)


# Creat a display message when the user enter the incorrect login 
        incorrect_login_label = tk.Label(self, text="", background='#336699', foreground='#990033', font=('bold', 22), anchor='n')
        incorrect_login_label.pack(fill='both', expand=True)

#+++++++++++++++++++++++++++++++++
# Creat a Bottom frame to display the time and the user pin.
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

#++++++++++++++++++++++++++++++++
    ##    card_photo = tk.PhotoImage(file='creditcard1.png')
     # #  card_label = tk.Label(bottom_frame,image=card_photo)
      ##  card_label.pack(side='left')
      ##  card_label.image = card_photo



class CoursesPage(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, background='#660066')
            self.controller=controller

# Creat a Notebook(tabs) for the CoursesPage.
            global my_frame2
            my_notebook = ttk.Notebook(self)
            my_notebook.pack(fill="both",expand=1)

# Creat a frames inside the notebook
            my_frame1 = Frame(my_notebook, bg="#003366")
            my_frame1.pack(fill="both",expand=1)

            my_frame2 = Frame(my_notebook, bg="green")
            my_frame2.pack(fill="both", expand=1)
            my_frame2.destroy

            my_frame3 = Frame(my_notebook,bg="blue")
            my_frame3.pack(fill="both", expand=1)

            my_notebook.add(my_frame1, text="Courses")
            my_notebook.add(my_frame2, text="Schedule")
            my_notebook.add(my_frame3, text= "Logout")
            
            
 #+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the TransactionPage page
            header_label3 = tk.Label(my_frame1, text="IVY SDVE Courses", foreground='White', background='#043927', font=('bold', 50))
            header_label3.pack(fill="both", expand=1)

# Header Labels for the  Header title of the TransactionPage page
            header_label4 = tk.Label(my_frame1, text="Courses", foreground='White', background='#043927', font=('bold', 30))
            header_label4.pack(fill="both", expand=1)

            selection_label= tk.Label(my_frame1, text="Select a course to enroll", fg='white', background='#003366' ,anchor='w')
            selection_label.pack(fill='x')





# ++++++++++++++++++++++++++++
# Creat a Withdraw function
            def sdev_153():
                controller.show_frame('Sdev153Page')
# Creat a withdraw button
            withdraw_button = tk.Button(my_frame1, text="SDEV153", command=sdev_153, relief='raised', borderwidth=3, width=25, height=5,)
            withdraw_button.pack(side="left")

# ++++++++++++++++++++++++++++
# Creat a deposit function
            def sdev_140():
                controller.show_frame('Sdev140Page')
# Creat a deposit button
            deposit_button = tk.Button(my_frame1, text="SDEV140", command=sdev_140, relief='raised', borderwidth=3, width=25, height=5)
            deposit_button.pack(side="right")

# ++++++++++++++++++++++++++++
# Creat a balance function
            def sdev_220():
                controller.show_frame('Sdev220Page')
# Creat a balance button
            balance_button = tk.Button(my_frame1, text="SDEV100", command=sdev_220, relief='raised', borderwidth=3, width=25, height=5)
            balance_button.pack(side="left", fill='x', expand=0)


# ++++++++++++++++++++++++++++
# Creat a exit function
            def exit():
                controller.show_frame('StartPage')
# Creat a exit button
            exit_button = tk.Button(my_frame1, text="LogOut", command=exit, relief='raised', borderwidth=3,width=25, height=5)
            exit_button.pack(side="bottom")




class Sdev153Page (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the WithdrawPage page
        header_label5 = tk.Label(self, text="SDEV153", foreground='White', background='#660066', font=('bold', 50))
        header_label5.pack()

        selection_label2= tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366' ,anchor='w')
        selection_label2.pack(fill='x')

        button_frame = tk.Frame(self, background='#336699' )
        button_frame.pack(fill='both', expand=True)

         # +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_sdev153_listbox = tk.Listbox(button_frame,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_sdev153_listbox.grid(row=0,column=0)

# Add list of items
        my_sdev153_list = ["SDVE153 - Anywhere - Keneisha E - M,TH 9:00am-1:00pm - FortWayne - 16Wks - 3 credits", 
                   "SDVE153 - Online - Milford Hutsell - M,W 6:00pm-8:50pm - Columbus - 2nd 8Wks - 3credits", 
                   "SDVE153 - Traditional - Mike Gorsline - m,w 2:00pm-5:00pm - N Meridian - 1st 8Wks - 3credits"]
        
        for sdev153_itme in my_sdev153_list:
            my_sdev153_listbox.insert(tk.END, sdev153_itme)

  
# Creat an uneroll function
        def unenroll():
            my_sdev153_label.config(text='')
            sdev153_enroll_button['state']= tk.NORMAL
            sdev153_unenroll_button['state']= tk.DISABLED


# Creat an enroll function
        def enroll():
            my_sdev153_label.config(text=my_sdev153_listbox.get(ANCHOR))
            schedule_sdev153_label.config(text=my_sdev153_listbox.get(ANCHOR))
            sdev153_enroll_button['state']= tk.DISABLED
            sdev153_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        sdev153_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        sdev153_enroll_button.place(x=3, y=130)

# Creat a uneroll button
        sdev153_unenroll_button = tk.Button(button_frame, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        sdev153_unenroll_button.place(x=179, y=130)
        sdev153_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_sdev153_label
        my_sdev153_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=70,height=2,)
        my_sdev153_label.place(x=3, y=80)

# Creat a label to display the enrolled class in the Schedule notebbok

        global schedule_sdev153_label
        schedule_sdev153_label = tk.Label(my_frame2, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=70,height=2,)
        schedule_sdev153_label.place(x=3, y=80)


 # ++++++++++++++++++++++++++++
# Creat a Back functionr
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=355, y=130)
#++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')




class Sdev140Page (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#660066')
        self.controller=controller
#+++++++++++++++++++++++++++++
# Header Labels for the  Header title of the DepositPage page
        header_label7 = tk.Label(self, text="SDEV140", foreground='White', background='#660066', font=('bold', 50))
        header_label7.pack()

        selection_label3= tk.Label(self, text="Select a class to enroll in:", fg='white', background='#003366' ,anchor='w')
        selection_label3.pack(fill='x')

        button_frame = tk.Frame(self, background='#336699' )
        button_frame.pack(fill='both', expand=True)

 # +++++++++++++++++++++++++++++
# Listbox!
# SINGLE, BROWSE, MULTIPLE, EXTENDED

        bolded = font.Font(weight='bold')
        my_sdev140_listbox = tk.Listbox(button_frame,font=bolded, relief='raised', borderwidth=4, width=70,height=4, selectmode=tk.SINGLE)
        my_sdev140_listbox.grid(row=0,column=0)

# Add list of items
        my_sdev140_list = ["SDVE140 - Anywhere - Steve Carver - M,W 1:00pm-4:50pm - FortWayne - 16Wks - 3 credits", 
                   "SDVE140 - Online - Jon Jon - M,W 6:00pm-8:50pm - Columbus - 16Wks - 3credits", 
                   "SDVE140 - Virtual - Alf Sanford - F,M 1:00pm-4:00pm - N Meridian - 8Wks - 3credits"]
        
        for sdev140_itme in my_sdev140_list:
            my_sdev140_listbox.insert(tk.END, sdev140_itme)

  
# Creat an uneroll function
        def unenroll():
            my_sdev140_label.config(text='')
            sdev140_enroll_button['state']= tk.NORMAL
            sdev140_unenroll_button['state']= tk.DISABLED


# Creat an enroll function
        def enroll():
            my_sdev140_label.config(text=my_sdev140_listbox.get(ANCHOR))
            sdev140_enroll_button['state']= tk.DISABLED
            sdev140_unenroll_button['state']= tk.NORMAL

# Creat a enroll button
        sdev140_enroll_button = tk.Button(button_frame, text="Enroll", relief='raised',command=enroll, borderwidth=3,width=15, height=3)
        sdev140_enroll_button.place(x=3, y=130)

# Creat a uneroll button
        sdev140_unenroll_button = tk.Button(button_frame, text="Uneroll",relief='raised', command=unenroll,borderwidth=3,width=15, height=3,)
        sdev140_unenroll_button.place(x=179, y=130)
        sdev140_unenroll_button['state']= tk.DISABLED

# Creat a label to display the enrolled class
        global my_sdev140_label
        my_sdev140_label = tk.Label(button_frame, text='Enrolled class will appear here ', background='#333333', borderwidth=5,relief='raised',width=70,height=2,)
        my_sdev140_label.place(x=3, y=80)

 # ++++++++++++++++++++++++++++
# Creat a Back function
        def back():
            controller.show_frame('CoursesPage')
# Creat a Back button
        back_buttonn = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3,width=15, height=3)
        back_buttonn.place(x=355, y=130)
#++++++++++++++++++++++
        # Creat a Bottom frame to display the time.
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')


# hex color constants
BG_COLOR = '#660066'
COLOR_1 = '#003366'
COLOR_2 = '#333333'


class CourseFrame(tk.Frame):
        """Base class for creating course frames"""

        def __init__(self, parent, controller, course_name, course_list):
                tk.Frame.__init__(self, parent, background=BG_COLOR)
                self.controller=controller


                # header label
                header_lbl = tk.Label(self, text=course_name, foreground='white', background=BG_COLOR, font=('bold', 50))
                header_lbl.pack()

                select_lbl = tk.Label(self, text="Select a class to enroll in: ", foreground='white', background=COLOR_1, anchor='w')
                select_lbl.pack(fill='x')


                # put another color on the page using a frame
                button_frame = tk.Frame(self, background=COLOR_1)
                button_frame.pack(fill='both', expand=True)


                # listbox
                bold_font = font.Font(weight='bold')
                course_listbox = tk.Listbox(button_frame,font=bold_font, relief='raised', borderwidth=4, width=70, height=4, selectmode=tk.BROWSE)
                course_listbox.grid(row=0, column=0)
                
                for course in course_list:
                        # add all the courses to the list
                        course_listbox.insert(tk.END, course)


                # enroll & unenroll buttons
                def enroll():
                        enrolled_course_lbl.config(text=course_listbox.get(ANCHOR))
                        enroll_button['state'] = tk.DISABLED
                        unenroll_button['state'] = tk.NORMAL

                def unenroll():
                        enrolled_course_lbl.config(text='')
                        enroll_button['state'] = tk.NORMAL
                        unenroll_button['state'] = tk.DISABLED
                
                enroll_button = tk.Button(button_frame, text="Enroll", relief='raised', command=enroll, borderwidth=3, width=15, height=3)
                enroll_button.place(x=3, y=130)

                unenroll_button = tk.Button(button_frame, text="Unenroll", relief='raised', command=unenroll, borderwidth=3, width=15, height=3)
                unenroll_button.place(x=179, y=130)
                unenroll_button['state'] = tk.DISABLED


                # display the enrolled class
                global enrolled_course_lbl
                enrolled_course_lbl = tk.Label(button_frame, text='Enrolled class will appear here.', background=COLOR_2, 
                                               borderwidth=5, relief='raised', width=70, height=2)
                enrolled_course_lbl.place(x=3, y=80)


                # back button
                def back():
                        controller.show_frame('CoursesPage')

                back_button = tk.Button(button_frame, text="Back", command=back, relief='raised', borderwidth=3, width=15, height=3)
                back_button.place(x=355, y=130)


class Sdev220Page(CourseFrame):
        def __init__(self, parent, controller):
                course_list = ["SDEV220 - Virtual - Feihong Liu - M,W 3:00pm-5:50pm - FortWayne - 8Wks - 3 credits", 
                               "SDEV220 - Online - Tim Tim - TH,M 6:00pm-8:50pm - Columbus - 16Wks - 3 credits", 
                               "SDEV220 - Virtual - Tom Tom - TU,W 1:00pm-4:00pm - N Meridian - 8Wks - 3 credits"]

                super().__init__(parent, controller, course_name="SDEV 220", course_list=course_list)


# display everything
if __name__ == "__main__":
    CourseApp().mainloop()