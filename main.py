from tkinter import *
from tkinter import messagebox as msgbx
from tkinter import simpledialog
from tkinter.ttk import *
from tkcalendar import DateEntry
import tkinter as tk
import ttk

 
#---------------- colors ---------------------
bg_col = '#504746' #brown
fg_col = "white"
txt_col= "black"

# ------------- initiate window, set size and color --------
main_menu = Tk()
main_menu.title('TO DO:')
main_menu.geometry('650x440')
main_menu['bg']= bg_col

#------------------------ functions  for the buttons --------------------------------
def add_item(entry: Entry, desc: Entry, imp: Entry, date: DateEntry):
  new_task = entry.get()
  new_desc = desc.get()
  new_imp = imp.get()
  new_time = date.get()
  if new_task != "":
    tv.insert(parent='', index=i, iid=i, text='', values= (new_task, new_desc, new_imp, new_time))
    with open('tasks.txt', 'a') as tasks_list:
        tasks_list.write(f'\n{new_task},{new_desc},{new_imp},{new_time}')    
    entry.delete(0, END)
    desc.delete(0, END)
    imp.delete(0, END)
  else:
    tk.messagebox.showwarning(title="Warning!!", message="Please enter a task.")
    
def open_addnew():
  add_new_win  = Toplevel(main_menu)
  add_new_win.title("Add a new task:")
  add_new_win.geometry("400x250")
  add_new_win.config(bg= '#D9D9D9') #grey
  frame_nw=Frame(add_new_win) #frame for the new window (nw)
  frame_nw.pack()
  title_txt = tk.Label(frame_nw, text="Title:", fg="grey")
  title_txt.pack()
  title_entry = Entry(frame_nw, width=40)
  title_entry.pack()
  desc_txt = tk.Label(frame_nw, text="Description:", fg="grey")
  desc_txt.pack()
  desc_entry = Entry(frame_nw, width=40)
  desc_entry.pack()
  imp_txt = tk.Label(frame_nw, text="Importance of the task (/10):", fg="grey")
  imp_txt.pack()
  imp_entry = Entry(frame_nw, width=40)
  imp_entry.pack()
  date_txt = tk.Label(frame_nw, text="Day (m/d/y):", fg="grey")
  date_txt.pack()
  date_entry=DateEntry(frame_nw,selectmode='day')
  date_entry.pack()
  save_button= Button(frame_nw,text="Save", width=20, command=lambda: add_item(title_entry, desc_entry, imp_entry, date_entry))
  save_button.pack(pady=3)
  
def update_item(title: Entry, desc: Entry,imp: Entry, date: DateEntry):
  selected = tv.focus()
  temp = tv.item(selected, 'values') 
  n_title = title.get()
  n_desc = desc.get()
  n_imp = imp.get()
  n_time = date.get()
  val='{new_task},{new_desc},{new_imp},{new_time}'
  tv.item(selected, values=(n_title, n_desc, n_imp, n_time))
  title.delete(0, END)
  desc.delete(0, END)
  imp.delete(0, END)

def open_update():
  add_up_win  = Toplevel(main_menu)
  add_up_win.title("Add a new task:")
  add_up_win.geometry("400x250")
  add_up_win.config(bg= '#D9D9D9') #grey
  frame_uw=Frame(add_up_win) #frame for the update window (up)
  frame_uw.pack()
  title_txt = tk.Label(frame_uw, text="New title:", fg="grey")
  title_txt.pack()
  title_entry = Entry(frame_uw, width=40)
  title_entry.pack()
  desc_txt = tk.Label(frame_uw, text="New description:", fg="grey")
  desc_txt.pack()
  desc_entry = Entry(frame_uw, width=40)
  desc_entry.pack()
  imp_txt = tk.Label(frame_uw, text="New importance of the task (/10):", fg="grey")
  imp_txt.pack()
  imp_entry = Entry(frame_uw, width=40)
  imp_entry.pack()
  date_txt = tk.Label(frame_uw, text="New due day (m/d/y):", fg="grey")
  date_txt.pack()
  date_entry=DateEntry(frame_uw,selectmode='day')
  date_entry.pack()
  update_button= Button(frame_uw,text="Update", width=20, command=lambda: update_item(title_entry, desc_entry, imp_entry, date_entry))
  update_button.pack(pady=3)



def delete_item():
  with open('tasks.txt', 'r+') as tasks_list:
    lines = tasks_list.readlines()
    tasks_list.truncate()
    for line in lines:
        if line.strip("\n") == tv.selection()[0]:
          lines.remove(line)
    tasks_list.close()
      
  selected_item = tv.selection()[0] ## get selected item
  tv.delete(selected_item)

def completed_item():
  with open('tasks.txt', 'r+') as tasks_list:
    lines = tasks_list.readlines()
    for line in lines:
        if line.strip("\n") == tv.selection():
          line.truncate()
    tasks_list.close()
      
  selected_item = tv.selection()[0] ## get selected item
  tv.delete(selected_item)
frame_user=Frame(main_menu) # ------------------- frame for the user ---------------------------
frame_user.pack()
greeting = tk.Label(frame_user, text="Welcome back my favortite human!", bg= bg_col, fg=fg_col)
greeting.pack()

encouragement = tk.Label(text="You can do it~ ☆", bg= bg_col, fg=fg_col)
encouragement.pack()

#-----------------frame: buttons-----------------------------
frame_button=Frame(main_menu) 
add_button=Button(frame_button,text="Add new", width=20, command=open_addnew)
add_button.pack(pady=3, padx=8, side = LEFT)
update_button=Button(frame_button,text="Update Task ",width=20, command=open_update)
update_button.pack(pady=3, padx=8, side = LEFT)
mark_button=Button(frame_button,text="Task completed ",width=20, command=lambda: completed_item())
mark_button.pack(pady=3, padx=8, side = LEFT)
frame_button.pack()

#-----tree----
tv = ttk.Treeview(main_menu)
tv['columns']=('Title', 'Description', 'Importance', 'Date')
tv.column('#0', width=0, stretch=NO)
tv.column('Title', anchor=CENTER, width=140)
tv.column('Description', anchor=CENTER, width=300)
tv.column('Importance', anchor=CENTER, width=40)
tv.column('Date', anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('Title', text='TITLE', anchor=CENTER)
tv.heading('Description', text='DESCRIPTION', anchor=CENTER)
tv.heading('Importance', text='/10', anchor=CENTER)
tv.heading('Date', text='M/D/Y', anchor=CENTER)
tv.pack()

delete_button=Button(main_menu,text="Delete task",width=20, command=lambda: delete_item())
delete_button.pack(pady=10)

tasks = Listbox(main_menu,bg="light grey",fg="black",height=15,width=50)

#---------- Put tasks from the txt into the Treeview-------
with open('tasks.txt', 'r+') as tasks_list:
  i=0
  for task in tasks_list:
    task = task.strip('\n').strip(',').strip()
    fields = task.split(',')
    tv.insert(parent='', index=i, iid=i, text='', values= fields)
    i = i+1
    
  tasks_list.close()


main_menu.mainloop()