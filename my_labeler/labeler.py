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

default_path = os.path.abspath('.')

def test():
	print("you did it!!!")

def load_file(type):
	print("load")
	if type == 'dir':
		ok = 
	pass

# # load file
# def on_load(self, type):
#     self.on_save() 
#     if type == 'dir':
#         ok = self.get_dirs()
#         if ok:
#             self.video_path = self.video_dirs[0]
#     elif type == 'file':
#         ok = self.get_file()

#     if ok:
#         self.init_all()

# # callback for save results
# def on_save(self, event=None):
#     if self.video_path is not None:
#         video_name = self.video_path.split('/')[-1]
#         file_name = video_name.split('.avi')[0] + '_label.txt'

#         data = []
#         for k in sorted(self.results.keys()):
#             boxes = self.results[k]
#             boxes = sorted(boxes, key=lambda x: x[0])
#             data.append('%s, %s\n' % (k, boxes))
#         if len(data) != 0:
#             with open('%s/%s' % (self.root_dir, file_name), 'w+') as f:
#                 f.writelines(data)
#             LOGGER.info('%s saved at %s' % (file_name, self.root_dir))



# # load all video under given directory
# def get_dirs(self):
#     dirs = askdirectory(title='select an image path', initialdir='../')

#     if not dirs:
#         return False
#     else:
#         video_dirs = ["%s/%s" % (dirs, f) for f in os.listdir(dirs) if f[-3:] == 'avi']
#         res = len(video_dirs) > 0
#         LOGGER.info('Load videos - {}'.format(video_dirs))
#         if not res:
#             self.msg('image not in the path ')
#             LOGGER.debug(video_dirs)
#         else:
#             self.video_dirs = video_dirs
#             return True

#     return False

# # load video
# def get_file(self):
#     if os.name == 'nt':
#         path = askopenfilename(
#             title=u'select an image file (.avi)',
#             filetypes=[('video file (*.avi;)', '*.avi;')])
#     else:
#         path = askopenfilename(
#             title=u'select an image file (.avi)')
#     LOGGER.info('Load video - {}'.format(path))

#     if not path:
#         return False
#     else:
#         res = os.path.isfile(path)
#         if not res:
#             self.msg('please select the correct image')
#         else:
#             self.video_path = path
#             return True

#     return False


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


#create a window
window = tk.Tk()
window.title('image labeler')
window.geometry('1380x920')

l = tk.Label(window, text='')
l.pack()


#creating menubar
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu) #add 
filemenu.add_command(label = "load image file path", command = lambda type_ = 'dir': load_file(type = type_))
filemenu.add_command(label = "load image file", command = lambda type_ = 'file': load_file(type = type_))



#topFrame = Frame(window)
#topFrame.pack(expand = True)
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM)

#adding buttons
play_button = Button(bottomFrame, text = "Play", font = 30, fg = "blue", command = play).pack(side = "left")
pause_button = Button(bottomFrame, text = "Pause", font = 30, fg = "red", command = pause).pack(side = "left")
replay_button = Button(bottomFrame, text = "Replay", font = 30,fg = "green", command = replay).pack(side = "left")
prev_button = Button(bottomFrame, text = "<<", font = 30,fg = "black", command = prev_one).pack(side = "left")
next_button = Button(bottomFrame, text = ">>", font = 30,fg = "black", command = next_one).pack(side = "left")


window.config(menu=menubar)
window.mainloop()










# window = tk.Tk()
# window.title('my window')
# window.geometry('1300x900')

# l = tk.Label(window, text='')
# l.pack()


# #creating menubar
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar, tearoff=0)

# menubar = Menu(window)
# filemenu = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label = "File", menu = filemenu) #add 
# filemenu.add_command(label = "load image file path", command = test)
# filemenu.add_command(label = "load image file", command = test)


# ###JK CODE####
# #menu = tk.Menu(self.parent)
# #self.parent.config(menu=menu)

# #menu_file = tk.Menu(menu)
# menu_file.add_command(label='load image file path', command=lambda type_='dir': self.on_load(type=type_))
# menu_file.add_command(label='load image file', command=lambda type_='file': self.on_load(type=type_))
# menu_file.add_command(label='save', command=self.on_save)

# menu_help = tk.Menu(menu)
# menu_help.add_command(label='settings', command=self.on_settings)

# menu.add_cascade(label='File', menu=menu_file)
# menu.add_cascade(label='Help', menu=menu_help)



# # window = tk.Tk()
# # window.title('image labeler')
# # window.geometry('1080x920')



# #topFrame = Frame(window)
# #topFrame.pack(expand = True)
# bottomFrame = Frame(window)
# bottomFrame.pack(side = BOTTOM)

# #adding buttons
# play_button = Button(bottomFrame, text = "Play", font = 30, fg = "blue").pack(side = "left")
# pause_button = Button(bottomFrame, text = "Pause", font = 30, fg = "red").pack(side = "left")
# replay_button = Button(bottomFrame, text = "Replay", font = 30,fg = "green").pack(side = "left")
# prev_button = Button(bottomFrame, text = "<<", font = 30,fg = "black").pack(side = "left")
# next_button = Button(bottomFrame, text = ">>", font = 30,fg = "black").pack(side = "left")






# window.config(menu=menubar)

# window.mainloop()






#class Labeler(tk.Frame, Utils, KeyHandler):

# class Labeler(tk.Frame, Utils, KeyHandler):

#     def __init__(self, *args, **kwargs):
#     	#tk.TK.__init__(self, *args, **kwargs)
#     	#container = tk.Frame(self)
#     	#container.pack(side = "top", fill = "both", expand = True)_



#         # variables for videos
#         self.root_dir = None
#         self.video_dirs = None
#         self.video_path = None
#         self.width = 1280
#         self.height = 720
#         self.fps = None
#         self.resolution = None
#         self.total_frame = None
#         self.n_done_video = 0
#         self.__video = None
#         self.__frame__ = None
#         self.__orig_frame__ = None
#         self.__image = None

#         # variables for frame
#         self._c_width = self._c_height = self._r_width = self._r_height = None
#         self.n_frame = 1


#class Labeler(tk.Tk):
# 	def __init__(self, *args, **kwargs):
# 		tk.Tk.__init__(self, *args, **kwargs)
# 		# window = tk.Tk()
# 		# window.title('my window')
# 		# window.geometry('1300x900')
# 		container = tk.Frame(self, width = 1080, height = 980)
# 		container.pack(side = "top", fill= "both", expand = True)
# 		container.grid_rowconfigure(0, weight=1)
# 		container.grid_columnconfigure(0, weight=1)

# 		self.frames = {}

# 		#creating menubar
# 		menubar = tk.Menu(container)
# 		filemenu = tk.Menu(menubar, tearoff=0)

# 		menubar.add_cascade(label = "File", menu = filemenu) #add 
# 		filemenu.add_command(label = "load image file path", command = qf)
# 		filemenu.add_command(label = "load image file", command = qf)

# 		tk.Tk.config(self, menu=menubar)


# 		frame = StartPage(container, self)
# 		self.frames[StartPage] = frame
# 		frame.grid(row = 0, column = 0, sticky = "nsew")
# 		self.show_frame(StartPage)

# 	def show_frame(self, cont):
# 		frame = self.frames[cont]
# 		frame.tkraise()

# def qf():
# 	print("you did it!")

# class StartPage(tk.Frame):
# 	def __init__(self, parent, controller):
# 		tk.Frame.__init__(self, parent)
# 		label = tk.Label(self, text="start page", font = ("Arial", 12))
# 		label.pack(pady=10, padx=10)

# 		play_button = Button(self, text = "Play", font = 30, fg = "blue", command = qf).pack(side = "left")
# 		pause_button = Button(self, text = "Pause", font = 30, fg = "red", command = qf).pack(side = "left")
# 		replay_button = Button(self, text = "Replay", font = 30,fg = "green", command = qf).pack(side = "left")
# 		prev_button = Button(self, text = "<<", font = 30,fg = "black", command = qf).pack(side = "left")
# 		next_button = Button(self, text = ">>", font = 30,fg = "black", command = qf).pack(side = "left")




		

# app = Labeler()
# app.geometry("1080x980")
# app.mainloop()