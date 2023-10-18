import tkinter as tk 
from tkinter import ttk
import calendar 
#Calender 
def create_calendar_tab():
    calendar_tab = ttk.Frame(tab_control)
    tab_control.add(calendar_tab, text= 'Calendar')
    display_calendar(calendar_tab)

def display_calendar(tab):
    def show_calendar():
        selected_month = month_var.get()
        selected_year = year_var.get()
        cal_text= calendar.month(selected_year, selected_month)
        text_widget.config(state=tk.NORMAL)  # Enable editing
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, cal_text)
       
        text_widget.config(state=tk.DISABLED)
    
    label = tk.Label(tab, text='Calendar', bg='light green')
    label.pack()

    #frame for the month and year widgets
    selection_frame = tk.Frame(tab)
    selection_frame.pack()

    month_var =tk.IntVar()
    year_var =tk.IntVar()
                
    # Dropdown menu for selecting the month
    month_label = tk.Label(selection_frame, text='Month:', bg="light green")
    month_label.pack(side=tk.LEFT)
    month_menu = ttk.Combobox(selection_frame, textvariable=month_var, values=list(range(1, 13)))
    month_menu.pack(side=tk.LEFT)
    month_menu.set(10)  # Default to October

   # Dropdown menu for selecting the year
    year_label = tk.Label(selection_frame, text='Year:', bg='light green')
    year_label.pack(side=tk.LEFT)
    year_menu = ttk.Combobox(selection_frame, textvariable=year_var, values=list(range(2023, 2030)))
    year_menu.pack(side=tk.LEFT)
    year_menu.set(2023)  # Default to 2023 
                                
    show_buttton = tk.Button(selection_frame, text='Show calendar', command=show_calendar)
    show_buttton.pack(side=tk.LEFT)

    #cal = calendar.month (2023,10)
    text_widget = tk.Text(tab, height=11, width=21, bg='light green')
    text_widget.pack()
    text_widget.tag_config("highlighted", background="yellow", foreground="black")
    text_widget.config(state=tk.DISABLED)
  
    show_calendar() 

#To-Do list
def create_todo_list_tab():
    todo_list_tab = ttk.Frame(tab_control)
    tab_control.add(todo_list_tab, text= 'To-Do')
    todo_list(todo_list_tab)   

def todo_list(tab):
    label = tk.Label(tab, text='To-Do Tasks', bg= 'light pink')
    label.pack()

    task_text= tk.Text(tab, height=11, width=21, bg= 'light pink', state=tk.DISABLED)
    task_text.pack()
    
#add task
    def add_task():
        task=task_entry.get()
        if task:
            task_text.config(state=tk.NORMAL)  # Enable editing
            task_text.insert(tk.END, task + '\n')
            task_entry.delete(0, tk.END)
            task_text.config(state=tk.DISABLED)  # Disable editing

#update task
    def update_selected_task():
        selected_indices = task_text.tag_ranges(tk.SEL)
        if selected_indices:
            selected_start = selected_indices[0]
            selected_end = selected_indices[1]
            new_task = task_entry.get()
            if new_task:
                task_text.config(state=tk.NORMAL)  # Enable editing
                task_text.delete(selected_start, selected_end)
                task_text.insert(selected_start, new_task)
                task_text.config(state=tk.DISABLED)  # Disable editing
#remove task
    def remove_task():
        selected_start = task_text.index(tk.SEL_FIRST)
        selected_end = task_text.index(tk.SEL_LAST)
        if selected_start and selected_end:
            task_text.config(state=tk.NORMAL)  # Enable editing
            task_text.delete(selected_start, selected_end)
            task_text.config(state=tk.DISABLED)  # Disable editing
    
    task_entry = tk.Entry(tab, width=40)
    task_entry.pack ()

#buttons for add, update and remove
    add_button= tk.Button(tab, text='Add Task', command=add_task)
    add_button.pack()
    update_button = tk.Button(tab, text='Update Selected Task', command=update_selected_task)
    update_button.pack()
    remove_button= tk.Button(tab, text='Remove Task', command=remove_task)
    remove_button.pack()

root = tk.Tk()
root.title("My 2023-2024 Student Planner")

tab_control = ttk.Notebook(root)

create_calendar_tab()
create_todo_list_tab()

dashboard_frame = ttk.Frame(root)
dashboard_frame.pack()

tab_control.pack(expand=1, fill='both')

root.mainloop()
