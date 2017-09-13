import tkinter as tk
from tkinter import ttk
import os

class KeyHandler(object):

    # change class index
    def on_class_button(self, k):
        if not self.is_mv and k in range(1, 6):
            self.class_ind = k
            for i, b in enumerate(self.class_buttons):
                if (k - 1) != i:
                    b['state'] = 'normal'
                else:
                    b['state'] = 'disabled'

    # set value for frame index scalebar
    def set_n_frame(self, s):
        v = int(float(s))
        self.n_frame = v

    # callback for left mouse click
    def on_l_mouse(self, event=None):
        if not self.is_mv and self.video_path is not None:
            self.p1 = (event.x, event.y)
            self.is_mv = True

    # callback for right mouse click
    def on_r_mouse(self, event=None):
        if self.n_frame in self.results.keys():
            n = len(self.results[self.n_frame])
            if n > 0:
                self.results[self.n_frame].pop()
                if str(n-1) in self.treeview.get_children():
                    self.treeview.delete(str(n-1))
                if len(self.results[self.n_frame]) == 0:
                    del self.results[self.n_frame]
            self.on_class_button(k=self.class_ind-1)

    # callback for mouse move
    def on_mouse_mv(self, event=None):
        if self.is_mv:
            self.mv_pt = (event.x, event.y)
            self.label_xy.configure(text='x: %s y: %s x1: %s, y1: %s' % (event.x, event.y, self.p1[0], self.p1[1]))
        else:
            self.label_xy.configure(text='x: %s y: %s' % (event.x, event.y))
    
    # callback for left mouse release
    def off_mouse(self, event=None):
        if self.is_mv and self.mv_pt is not None:
            self.is_mv = False
            xmin = min(self.p1[0], event.x)
            ymin = min(self.p1[1], event.y)
            xmax = max(self.p1[0], event.x)
            ymax = max(self.p1[1], event.y)
            self.p1 = (xmin, ymin)
            self.mv_pt = (xmax, ymax)
            values = (self.class_ind, self.p1, self.mv_pt)
            if self.n_frame not in self.results.keys():
                self.results[self.n_frame] = [values]
            else:
                self.results[self.n_frame].append(values)

            self.treeview.insert('', 'end', str(len(self.treeview.get_children())), values=values, tags = (str(self.class_ind)))
            self.p1 = self.mv_pt = None
            self.on_class_button(k=self.class_ind+1)

    # callback for delete button of treeview
    def on_delete(self, event=None):
        for v in self.treeview.selection():
            self.treeview.delete(v)

    # callback for select rows in treeview
    def on_select_all(self, event=None):
        if self.video_path is not None:
            for x in self.treeview.get_children():
                self.treeview.selection_add(x)

    # callback for save results
    def on_save(self, event=None):
        if self.video_path is not None:
            video_name = self.video_path.split('/')[-1]
            file_name = video_name.split('.avi')[0] + '_label.txt'

            data = []
            for k in sorted(self.results.keys()):
                boxes = self.results[k]
                data.append('%s, %s\n' % (k, boxes))
            with open('%s/%s' % (self.root_dir, file_name), 'w+') as f:
                f.writelines(data)

    # move to previous frame
    def on_left(self, event=None, step=1):
        if self.video_path is not None:
            if self.n_frame > 1 and (self.n_frame - step) >= 1:
                self.n_frame -= step
                self.on_class_button(k=1)
                self.update_treeview()
            elif (self.n_frame - step) < 0:
                self.n_frame = 1
                self.on_class_button(k=1)
                self.update_treeview()
                self.msg('Already the first frame!')
            else:
                self.msg('Already the first frame!')
    
    # move to next frame
    def on_right(self, event=None, step=1):
        if self.video_path is not None:
            if self.n_frame == self.total_frame:
                self.msg('Already the last frame!')
            elif (self.n_frame + step) > self.total_frame:
                self.n_frame = self.total_frame 
                self.on_class_button(k=1)
                self.update_treeview()
            else:
                self.n_frame += step
                self.on_class_button(k=1)
                self.update_treeview()
