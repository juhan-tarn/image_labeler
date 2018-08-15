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

class Labeler(tk.Frame, Utils, KeyHandler):

    def __init__(self, *args, **kwargs):

        # variables for videos
        self.root_dir = None
        self.video_dirs = None
        self.video_path = None
        self.width = 1280
        self.height = 720
        self.fps = None
        self.resolution = None
        self.total_frame = None
        self.n_done_video = 0
        self.__video = None
        self.__frame__ = None
        self.__orig_frame__ = None
        self.__image = None

        # variables for frame
        self._c_width = self._c_height = self._r_width = self._r_height = None
        self.n_frame = 1