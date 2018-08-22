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
root_dir = None
video_dirs = None
video_path = None
width = 1280
height = 720
_video = None
_frame_= None
_orig_frame = None
_image = None

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

def init_video():
    if __video is not None:
        __video.release()
    ok = os.path.isfile(video_path)
    if ok:
        __video = cv2.VideoCapture(video_path)
        width = int(self.__video.get(3))
        height = int(self.__video.get(4))
        #self.fps = int(self.__video.get(5))
        resolution = (width, height)
        #self.total_frame = int(self.__video.get(cv2.CAP_PROP_FRAME_COUNT))
    else:
        string = 'Exist of %s: %s' % (video_path, os.path.isfile(video_path))
        msg(string, type='warning')
        video_path = None

# callback for save results
def on_save():
    if video_path is not None:
        video_name = video_path.split('/')[-1]
        file_name = video_name.split('.png')[0] + '_label.txt'

        data = []
        for k in sorted(results.keys()):
            boxes = results[k]
            boxes = sorted(boxes, key=lambda x: x[0])
            data.append('%s, %s\n' % (k, boxes))
        if len(data) != 0:
            with open('%s/%s' % (root_dir, file_name), 'w+') as f:
                f.writelines(data)
            LOGGER.info('%s saved at %s' % (file_name, root_dir))


def init_all():
    root_dir = "/".join(video_path.split('/')[:-1])
    init_video()

    # load previous label if file exists
    filename = video_path.split('.png')[0] + '_label.txt'
    if os.path.isfile(filename):
        LOGGER.info('Load label history - {}'.format(filename))
        with open(filename, 'r') as f:
            data = f.readlines()
        results = {eval(l)[0]: eval(l)[1] for l in data}
    else:
        results = dict()

    # change class index
    #self.n_frame = 1
    #if self.n_frame in self.results.keys():
#        self.class_reindex()
#    else:
#        self.on_class_button(k=1)

    # update treeview rows
#    self.update_treeview()

    # change scalebar state
#    self.scale_n_frame.state(['!disabled'])
#    self.scale_n_frame['to_'] = self.total_frame

def on_load(type):
    print("load")
    #on_save()
    if type == 'dir':
        print("get_dir")
        ok = get_dirs()
    elif type == 'file':
        print("get_file")
        ok = get_file()
    if ok:
        init_all()


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
            title=u'select an image file (.png)',
            filetypes=[('image file (*.png;)', '*.png;')])
        print(path)
    else:
        path = askopenfilename(
            title=u'select an image file (.png)')
        print(path)
    LOGGER.info('Load image - {}'.format(path))


    if not path:
        return False
    else:
        res = os.path.isfile(path)
        if not res:
            msg('please select the correct image')
        else:
            video_path = path
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
    menu_file.add_command(label='load image file path', command=lambda type_='dir': on_load(type=type_))
    menu_file.add_command(label='load image file', command=lambda type_='file': on_load(type=type_))


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

def update_display():
    if video_path is not None:
        update_frame()
    try:
        #self.draw()
        __image = ImageTk.PhotoImage(Image.fromarray(__frame__))
        disply_l.configure(image=__image)
    except Exception as e:
        LOGGER.exception(e)

    disply_l.after(40, self.update_display)

def update_frame():
    #__video.set(cv2.CAP_PROP_POS_FRAMES, n_frame - 1)
    #ok, __frame__ = __video.read()
    #__orig_frame__ = __frame__.copy()
    pass

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
filemenu =  tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "load image file path", command = lambda type_ = 'dir': on_load(type = type_))
filemenu.add_command(label = "load image file", command = lambda type_ = 'file': on_load(type = type_))


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

#img = ImageTk.PhotoImage(Image.open("TLPAquarium1_screenshot.png"))
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
info_frame.grid(row=0, column=1, rowspan=2, sticky='news', pady=10)
info_frame.grid_columnconfigure(0, weight=1)
info_frame.grid_rowconfigure(0, weight=1)
info_frame.grid_rowconfigure(1, weight=1)
info_frame.grid_rowconfigure(2, weight=1)

#update_display()

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



# import tkinter
# import cv2
# import PIL.Image, PIL.ImageTk
#
#  # Create a window
# window = tkinter.Tk()
# window.title("OpenCV and Tkinter")
#
#  # Load an image using OpenCV
# cv_img = cv2.cvtColor(cv2.imread("TLPAquarium1_screenshot.png"), cv2.COLOR_BGR2RGB)
#
# # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
# height, width, no_channels = cv_img.shape
# # Create a canvas that can fit the above image
# canvas = tkinter.Canvas(window, width = width, height = height)
# canvas.pack()
#
# # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
# photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
#
# # Add a PhotoImage to the Canvas
# canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
#
# # Run the window loop
# window.mainloop()
