from tkinter import *
from tkinter import filedialog
from tkinter import font,ttk
from tkinter import colorchooser
from PIL import Image,ImageTk
from tkinter import messagebox as mb
import traceback

root = Tk()
root.title("Textadept")
root.resizable("true","true")
root.geometry("1200x650")
p1 = PhotoImage(file = './icons2/logo.png')
root.iconphoto(False, p1)
open_status_name=False#variable to store open file name
selected=False
#designate our font
our_font=font.Font(family="Arial",size="16")

def show_error(self, *args):
    err = traceback.format_exception(*args)
    print(err[-1])
    mb.showerror('Exception',err[-1])
# but this works too
Tk.report_callback_exception = show_error

#file icons

new_icon = ImageTk.PhotoImage(file='./icons2/new.png')
open_icon = ImageTk.PhotoImage(file='./icons2/open.png')
save_icon = ImageTk.PhotoImage(file='./icons2/save.png')
save_as_icon = ImageTk.PhotoImage(file='./icons2/save_as.png')
exit_icon = ImageTk.PhotoImage(file='./icons2/exit.png')

#edit icons

copy_icon = ImageTk.PhotoImage(file='./icons2/copy.png')
paste_icon = ImageTk.PhotoImage(file='./icons2/paste.png')
cut_icon = ImageTk.PhotoImage(file='./icons2/cut.png')
clear_all_icon = ImageTk.PhotoImage(file='./icons2/clear_all.png')
redo_icon = ImageTk.PhotoImage(file='./icons2/redo.png')
undo_icon = ImageTk.PhotoImage(file='./icons2/undo.png')
select_all_icon=ImageTk.PhotoImage(file='./icons2/select_all.png')

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
def undo_text():
    try:
        my_text.edit_undo()
    except TclError:
        mb.showerror(title="Error", message="Nothing to Undo")

def redo_text():
    try:
        my_text.edit_redo()
    except TclError:
        mb.showerror(title="Error", message="Nothing to Redo")


#font family and fond size funct
current_font_family = "Arial"
current_font_size = 16

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    print(current_font_family)
    our_font.config(family=current_font_family)

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    our_font.config(size=current_font_size)

def bold_it():
    # create our font
    bold_font=font.Font(my_text,my_text.cget("font"))
    bold_font.config(weight="bold")

    #configure a tag
    my_text.tag_configure("bold",font=bold_font)

    try:
        # define current tags
        current_tags = my_text.tag_names("sel.first")
        # is statement to see if tag has been set
        if "bold" in current_tags:
            my_text.tag_remove("bold", "sel.first", "sel.last")
        else:
            my_text.tag_add("bold", "sel.first", "sel.last")
    except:
        mb.showerror(title="Exception", message="_tkinter.TclError: No text is Selected")
        print("_tkinter.TclError: No text is Selected")

def italics_it():
    # create our font
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.config(slant="italic")

    # configure a tag
    my_text.tag_configure("italic", font=italics_font)

    # define current tags
    try:
        current_tags = my_text.tag_names("sel.first")
        # is statement to see if tag has been set
        if "italic" in current_tags:
            my_text.tag_remove("italic", "sel.first", "sel.last")
        else:
            my_text.tag_add("italic", "sel.first", "sel.last")
    except:
        mb.showerror(title="Exception", message="_tkinter.TclError: No text is Selected")
        print("_tkinter.TclError: No text is Selected")

def underline_it():
    underline_font = font.Font(my_text, my_text.cget("font"))
    underline_font.config(underline=1)

    # configure a tag
    my_text.tag_configure("underline", font=underline_font)

    # define current tags
    try:
        current_tags = my_text.tag_names("sel.first")
        # is statement to see if tag has been set
        if "underline" in current_tags:
            my_text.tag_remove("underline", "sel.first", "sel.last")
        else:
            my_text.tag_add("underline", "sel.first", "sel.last")
    except:
        mb.showerror(title="Exception", message="_tkinter.TclError: No text is Selected")
        print("_tkinter.TclError: No text is Selected")

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
        try:
            current_tags = my_text.tag_names("sel.first")
            # is statement to see if tag has been set
            if "colored" in current_tags:
                my_text.tag_remove("colored", "sel.first", "sel.last")
            else:
                my_text.tag_add("colored", "sel.first", "sel.last")
        except:
            mb.showerror(title="Exception", message="_tkinter.TclError: No text is Selected")
            print("_tkinter.TclError: No text is Selected")

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
    #freeze frame in place
    my_frame.grid_propagate(False)
    # create scroll bar for text box
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    # horizontal scroll bar
    hor_scroll=Scrollbar(my_frame,orient="horizontal")
    hor_scroll.pack(side=BOTTOM,fill=X)

    # create Text box
    my_text = Text(my_frame, width=110, height=100, font=our_font, selectbackground="#0147FA",
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

    my_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="New",image=new_icon,compound="left", accelerator="Ctrl+N", command=new_file)
    file_menu.add_command(label="Open", image=open_icon,compound="left", accelerator="Ctrl+O",command=open_file)
    file_menu.add_command(label="Save", image=save_icon,compound="left",accelerator="Ctrl+S",command=save_file)
    file_menu.add_command(label="Save As", image=save_as_icon,compound="left",accelerator="Ctrl+Alt+S",command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", image=exit_icon,compound="left",accelerator="Ctrl+Q",command=root.quit)

    # Add eidt
    edit_menu = Menu(my_menu,tearoff=False)

    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut",image=cut_icon,compound="left",command=lambda: cut_text(False),accelerator="Ctrl+X")
    edit_menu.add_command(label="Copy",image=copy_icon,compound="left",command=lambda: copy_text(False),accelerator="Ctrl+C")
    edit_menu.add_command(label="Paste        ",image=paste_icon,compound="left",command=lambda: paste_text(False),accelerator="Ctrl+V")
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo",image=undo_icon,compound="left",command=undo_text,accelerator="Ctrl+Z")
    edit_menu.add_command(label="Redo",image=redo_icon,compound="left",command=my_text.edit_redo,accelerator="Ctrl+Y")
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All",image=select_all_icon,compound="left", command=lambda :select_all(False), accelerator="Ctrl+A")
    edit_menu.add_command(label="Clear",image=clear_all_icon,compound="left", command=clear_all)


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

    #file bind
    root.bind('<Control-n>',new_file)
    root.bind('<Control-o>',open_file)
    root.bind('<Control-s>',save_file)
    root.bind('<Control-Alt-s>',save_as_file)

    font_tuple = font.families()
    font_family = StringVar()
    font_box = ttk.Combobox(tool_frame, width=30, textvariable=font_family, state='readonly')
    font_box['values'] = font_tuple
    font_box.current(font_tuple.index('Arial'))
    font_box.grid(row=0, column=0, padx=5)

    #size box
    size_var = IntVar()
    font_size = ttk.Combobox(tool_frame, width=14, textvariable=size_var, state='readonly')
    font_size['values'] = tuple(range(6, 60,2))
    font_size.current(12)
    font_size.grid(row=0, column=1, padx=5)

    font_box.bind("<<ComboboxSelected>>", change_font)
    font_size.bind("<<ComboboxSelected>>", change_fontsize)

    #create bold button
    # bold_icon = ImageTk.PhotoImage(file='./icons2/bold.png')
    bold_button=Button(tool_frame,text="Bold",command=bold_it)
    bold_button.grid(row=0,column=2,sticky=W,padx=5)

    #create italic button
    # italic_icon = ImageTk.PhotoImage(file='./icons2/italic.png')
    italics_button = Button(tool_frame, text="Italics",command=italics_it)
    italics_button.grid(row=0, column=3,padx=5)

    #underline button
    underline_button = Button(tool_frame, text="Underline", command=underline_it)
    underline_button.grid(row=0, column=4, padx=5)

    # undo/redo button
    undo = Button(tool_frame, text="Undo", command=my_text.edit_undo)
    undo.grid(row=0, column=5,padx=5)
    redo = Button(tool_frame, text="Redo", command=my_text.edit_redo)
    redo.grid(row=0, column=6,padx=5)

    #text color button
    color_text_button=Button(tool_frame,text="Text Color",command=text_color)
    color_text_button.grid(row=0, column=7,padx=5)

    root.mainloop()
