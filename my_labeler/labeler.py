import tkinter as tk
from tkinter import *
import logging
import os
import tkinter as tk
from glob import glob
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.messagebox import askokcancel, showerror, showinfo, showwarning
import cv2
import numpy as np
from PIL import Image, ImageTk

LOGGER = logging.getLogger(__name__)

def play():
    print("play")
    pass

def pause():
    print("pause")
    pass

def replay():
    print("replay")
    pass

def prev_one():
    print("prev")
    pass

def next_one():
    print("next")
    pass

def load_file(type):
	print("load")
	if type == 'dir':
		print("get_dir")
		ok = get_dirs()
	elif type == 'file':
		print("get_file")
		ok = get_file()

# load all video under given directory
def get_dirs():
    dirs = askdirectory(title = 'select an image path', initialdir = '../')

    if not dirs:
        return False

    else:
        video_dirs = ["%s/%s" % (dirs, f) for f in os.listdir(dirs) if f[-3:] == 'avi']
        LOGGER.info('Load vidoes ')
        if not res:
            msg('image not in the path ')
            LOGGER.debug(video_dirs)
        else:
            self.video_dirs = video_dirs
            return True

    return False

 # load video
def get_file():
    if os.name == 'nt':
        path = askopenfilename(
            title=u'select an image file (.jpg)',
            filetypes=[('video file (*.jpg;)', '*.jpg;')])
    else:
        path = askopenfilename(
            title=u'select an image file (.jpg)')
    LOGGER.info('Load video - {}'.format(path))

    if not path:
        return False
    else:
        res = os.path.isfile(path)
        if not res:
            self.msg('please select the correct image')
        else:
            self.video_path = path
            return True

    return False

def on_close():
    if askokcancel('leave', 'You sure you want to leave?'):
        #self.on_save()
        parent.quit()
        parent.destroy()


def create_menu():
    menu = tk.Menu(parent)
    parent.config(menu=menu)

    menu.add_cascade(label='File', menu=menu_file)

    menu_file = tk.Menu(menu, tearoff = 0)
    menu_file.add_command(label='load image file path', command=lambda type_='dir': load_file(type=type_))
    menu_file.add_command(label='load image file', command=lambda type_='file': load_file(type=type_))


def create_ui():
    create_menu()

    parent.grid_rowconfigure(0, weight=1)
    parent.grid_rowconfigure(1, weight=1)
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_columnconfigure(1, weight=1)

    __frame__ = np.zeros((720, 1280, 3), dtype='uint8')
    cv2.putText(__frame__, 'Load Video', (300, 360), 7, 5, (255, 255, 255), 2)
    __orig_frame__ = __frame__.copy()
    __image = ImageTk.PhotoImage(Image.fromarray(__frame__))

    # display panel frame
    display_frame = tk.Frame(parent)
    display_frame.grid(row=0, column=0, padx=10, pady=10)
    display_frame.grid_rowconfigure(0, weight=1)
    display_frame.grid_columnconfigure(0, weight=1)
    display_frame.grid_rowconfigure(1, weight=1)

def update_display(self):
    if self.video_path is not None:
        self.update_frame()
    try:
        self.draw()
        self.__image = ImageTk.PhotoImage(Image.fromarray(self.__frame__))
        self.disply_l.configure(image=self.__image)
    except Exception as e:
        LOGGER.exception(e)

    self.disply_l.after(40, self.update_display)

def update_frame(self):
    self.__video.set(cv2.CAP_PROP_POS_FRAMES, self.n_frame - 1)
    ok, self.__frame__ = self.__video.read()
    self.__orig_frame__ = self.__frame__.copy()


#create a window
window = tk.Tk()
window.title('image labeler')
window.geometry('1680x920') #set a size for the window

tk.Grid.rowconfigure(window, 0 , weight=1)
tk.Grid.columnconfigure(window, 0 , weight=1)
tk.Grid.rowconfigure(window, 1 , weight=1)
tk.Grid.columnconfigure(window, 1 , weight=1)

#creating menubar
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu) #add
filemenu.add_command(label = "load image file path", command = lambda type_ = 'dir': load_file(type = type_))
filemenu.add_command(label = "load image file", command = lambda type_ = 'file': load_file(type = type_))


window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

__frame__ = np.zeros((720, 1080, 3), dtype='uint8')
cv2.putText(__frame__, 'Load Video', (150, 360), 7, 5, (255, 255, 255), 2)
__orig_frame__ = __frame__.copy()
image = ImageTk.PhotoImage(Image.fromarray(__frame__))

# display panel frame
#FIX HERE
display_frame = tk.Frame(window)
display_frame.grid(row=0, column=0, sticky = 'news', padx=10, pady=10)
display_frame.grid_rowconfigure(0, weight=1)
display_frame.grid_columnconfigure(0, weight=1)
display_frame.grid_rowconfigure(1, weight=1)

disply_l = ttk.Label(display_frame, image=image)
disply_l.grid(row=0, column=0, sticky='news')


op_frame = tk.Frame(display_frame)
op_frame.grid(row=1, column=0, padx=10, pady=10)
op_frame.grid_rowconfigure(0, weight=1)
op_frame.grid_rowconfigure(1, weight=1)
op_frame.grid_columnconfigure(0, weight=1)


button_label_frame = Frame(op_frame)
button_label_frame.grid(row=0, column=0, sticky='news')
button_label_frame.grid_rowconfigure(0, weight=1)
button_label_frame.grid_columnconfigure(0, weight=1)

button_frame = Frame(button_label_frame)
button_frame.grid(row=0, column=0)
#font = ("Courier", 30),
play_button = tk.Button(button_frame, text = "Play", font = 30, fg = "green", command = play).grid(row=0, column=1, sticky='news', padx=10, pady=0)
pause_button = tk.Button(button_frame, text = "Pause", font = 30,fg = "red", command = pause).grid(row=0, column=2, sticky='news', padx=10, pady=0)
replay_button = tk.Button(button_frame, text = "Replay", font = 30,fg = "blue", command = replay).grid(row=0, column=3, sticky='news', padx=10, pady=0)
prev_button = tk.Button(button_frame, text = "<<", font = 30,command = prev_one).grid(row=0, column=4, sticky='news', padx=10, pady=0)
next_button = tk.Button(button_frame, text = ">>", font = 30,command = next_one).grid(row=0, column=5, sticky='news', padx=10, pady=0)

info_frame = tk.Frame(window, bg = "yellow")
info_frame.grid(row=0, column=, sticky = 'news', rowspan=2, pady=10)
info_frame.grid_columnconfigure(0, weight=1)
info_frame.grid_rowconfigure(0, weight=1)
info_frame.grid_rowconfigure(1, weight=1)
info_frame.grid_rowconfigure(2, weight=1)


window.config(menu=menubar)
window.mainloop()


###############
#topFrame = Frame(window)
#topFrame.pack(expand = True)
# bottomFrame = Frame(window)
# bottomFrame.grid(row=0, column=0) #FIX HERE TOO

# # #adding buttons
# play_button = Button(bottomFrame, text = "Play", font = 30, fg = "blue", command = play).grid(row=0, column=1, sticky='news', padx=10, pady=0)
# pause_button = Button(bottomFrame, text = "Pause", font = 30, fg = "red", command = pause).grid(row=0, column=2, sticky='news', padx=10, pady=0)
# replay_button = Button(bottomFrame, text = "Replay", font = 30,fg = "green", command = replay).grid(row=0, column=3, sticky='news', padx=10, pady=0)
# prev_button = Button(bottomFrame, text = "<<", font = 30,fg = "black", command = prev_one).grid(row=0, column=4, sticky='news', padx=10, pady=0)
# next_button = Button(bottomFrame, text = ">>", font = 30,fg = "black", command = next_one).grid(row=0, column=5, sticky='news', padx=10, pady=0)

# window.config(menu=menubar)
# window.mainloop()
