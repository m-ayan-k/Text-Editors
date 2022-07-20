from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser


root = Tk()
root.title("Text Editor")
# root.geometry("1200x680")
open_status_name=False#variable to store open file name
selected=False

# changing title
def change_title(Nmae):
    j = 0
    for i in range(len(Nmae) - 1, -1, -1):
        if Nmae[i] == '/':
            j = i
            break
    root.title(f'{Nmae[j + 1:]}')

#Create anew file function
def new_file():
    # delete previous text
    my_text.delete('1.0',END)
    root.title('New File')
    # Update status bar
    status_bar.config(text='New file        ')
    open_status_name=False

def open_file():
    # delete previous text
    my_text.delete("1.0",END)

    #Grab file name
    text_file=filedialog.askopenfilename(initialdir="C:\\Users",title="Open File",
    filetypes=(("Text Files","*.txt"),("Python Files","*.py"),("HTML Files","*.html"),("All Files","*.*")))

    #check to see if there is a file name
    if text_file:
        global open_status_name
        open_status_name=text_file

    #update status bar nd title
    name=text_file
    status_bar.config(text=f'{name}        ')
    change_title(name)

    #open file
    text_file=open(text_file,'r')
    stuff=text_file.read()
    #inserting content of file to text box
    my_text.insert(END,stuff)
    text_file.close()

# Save As file
def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="C:\\Users",title="Save File",
    filetypes=(("Text Files","*.txt"),("Python Files","*.py"),("HTML Files","*.html"),("All Files","*.*")))

    # using if to check that we didn't click on cancel button
    if text_file:
        #updating status bar
        name=text_file
        status_bar.config(text=f'Saved: {name}        ')
        change_title(name)
        # save file
        text_file=open(text_file,'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()

#save file
def save_file():
    global open_status_name
    if open_status_name:
        #save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

        status_bar.config(text=f'Saved: {open_status_name}        ')
    else:
        save_as_file()

def cut_text(e):
    global selected
    if e:
        selected=root.clipboard_get()
    else:
        if my_text.selection_get():
            # grab selected text from text box
            selected=my_text.selection_get()
            #delete selected text from text box
            my_text.delete("sel.first","sel.last")
            root.clipboard_clear()  # to clear all text from clipborad
            root.clipboard_append(selected)

def copy_text(e):
    global selected
    if e:
        selected=root.clipboard_get()# copy all selected text to clipboard

    if my_text.selection_get():
        # grab selected text from text box
        selected=my_text.selection_get()
        root.clipboard_clear()# to clear all text from clipborad
        root.clipboard_append(selected)# to add selected text to clipboard to that when we use ctrl+v we only paste what we had selected

def paste_text(e):
    global selected
    if e:# to check that we use keyboard shortcut ,if yes then enter the if
        selected=root.clipboard_get()
    else:
        if selected:
            position=my_text.index(INSERT)
            my_text.insert(position,selected)

def bold_it():
    # create our font
    bold_font=font.Font(my_text,my_text.cget("font"))
    bold_font.config(weight="bold")

    #configure a tag
    my_text.tag_configure("bold",font=bold_font)

    #define current tags
    current_tags=my_text.tag_names("sel.first")
    #is statement to see if tag has been set
    if "bold" in current_tags:
        my_text.tag_remove("bold","sel.first","sel.last")
    else:
        my_text.tag_add("bold","sel.first","sel.last")

def italics_it():
    # create our font
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.config(slant="italic")

    # configure a tag
    my_text.tag_configure("italic", font=italics_font)

    # define current tags
    current_tags = my_text.tag_names("sel.first")
    # is statement to see if tag has been set
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

#change selected text color
def text_color():
    # pick a color
    my_color=colorchooser.askcolor()[1]
    if my_color:
        # create our font
        color_font = font.Font(my_text, my_text.cget("font"))

        # configure a tag
        my_text.tag_configure("colored", font=color_font,foreground=my_color)

        # define current tags
        current_tags = my_text.tag_names("sel.first")
        # is statement to see if tag has been set
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")

#change color for all text
def all_text_color():
    # pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)

#change bg color
def bg_color():
    # pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

def select_all(e):
    # add sel tag to selct all text
    my_text.tag_add('sel','1.0','end')

def clear_all():
    my_text.delete(1.0,END)

if __name__ == '__main__':

    #create a toolbar frame
    tool_frame=Frame(root)
    tool_frame.pack(fill=X)

    #Create main frame for text
    my_frame = Frame(root)
    my_frame.pack(pady=5)

    # create scroll bar for text box
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    # horizontal scroll bar
    hor_scroll=Scrollbar(my_frame,orient="horizontal")
    hor_scroll.pack(side=BOTTOM,fill=X)

    # create Text box
    my_text = Text(my_frame, width=110, height=26, font=("Helvetica", 16), selectbackground="#0147FA",
                   selectforeground="white", undo=True, yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
    my_text.pack()

    # configure our scrollbar
    text_scroll.config(command=my_text.yview)
    hor_scroll.config(command=my_text.xview)

    # create a menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Add file Menu
    file_menu = Menu(my_menu,tearoff=False)

    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New",command=new_file)
    file_menu.add_command(label="Open",command=open_file)
    file_menu.add_command(label="Save",command=save_file)
    file_menu.add_command(label="Save As",command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit",command=root.quit)

    # Add eidt
    edit_menu = Menu(my_menu,tearoff=False)

    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut",command=lambda: cut_text(False),accelerator="Ctrl+x")
    edit_menu.add_command(label="Copy",command=lambda: copy_text(False),accelerator="Ctrl+c")
    edit_menu.add_command(label="Paste        ",command=lambda: paste_text(False),accelerator="Ctrl+v")
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo",command=my_text.edit_undo,accelerator="Ctrl+z")
    edit_menu.add_command(label="Redo",command=my_text.edit_redo,accelerator="Ctrl+y")
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All", command=lambda :select_all(False), accelerator="Ctrl+a")
    edit_menu.add_command(label="Clear", command=clear_all)


    #Add color menu
    color_menu = Menu(my_menu, tearoff=False)

    my_menu.add_cascade(label="Colors", menu=color_menu)
    color_menu.add_command(label="Changed selected text", command=text_color)
    color_menu.add_command(label="All Text",command=all_text_color)
    color_menu.add_command(label="Background", command=bg_color)

    #add status bar to bottom of app
    status_bar=Label(root,text="Ready       ",anchor=E)
    status_bar.pack(fill=X,side=BOTTOM,ipady=15)

    #edit bindings
    root.bind('<Control-x>',cut_text)
    root.bind('<Control-c>',copy_text)
    root.bind('<Control-v>',paste_text)
    #select bind
    root.bind('<Control-A>',select_all)
    root.bind('<Control-a>',select_all)

    #create bold button
    bold_button=Button(tool_frame,text="Bold",command=bold_it)
    bold_button.grid(row=0,column=0,sticky=W,padx=5)

    #create italic button
    italics_button = Button(tool_frame, text="Italics", command=italics_it)
    italics_button.grid(row=0, column=1,padx=5)

    # undo/redo button
    undo = Button(tool_frame, text="Undo", command=my_text.edit_undo)
    undo.grid(row=0, column=2,padx=5)
    redo = Button(tool_frame, text="Redo", command=my_text.edit_redo)
    redo.grid(row=0, column=3,padx=5)

    #text color button
    color_text_button=Button(tool_frame,text="Text Color",command=text_color)
    color_text_button.grid(row=0, column=4,padx=5)

    root.mainloop()
