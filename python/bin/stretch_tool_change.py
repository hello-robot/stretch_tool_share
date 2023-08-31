#!/usr/bin/env python3
import tkinter as tk
from PIL import Image, ImageTk
import os


class ToolChangeDashboard():
    def __init__(self):
        self.window = tk.Tk()
        light_pink = "#FDF1F5"
        med_pink = "#FBCCDB"
        self.window.title("Tool Changer")
        self.window.configure(bg=light_pink)

        self.suggested_grid = tk.Frame(self.window,bg=light_pink)
        self.suggested_grid.pack(side=tk.TOP)

        self.tools_grid = tk.Frame(self.window,bg=light_pink)
        self.tools_grid.pack(side=tk.BOTTOM)

        self.im_path = os.path.expanduser('~/repos/stretch_tool_share/tool_share/')
        self.imgs_dict = {}
        self.suggested_imgs_dict = {}
        self.curr_grid = [0, 1]
        self.curr_suggested_grid = [0,1]
        self.max_in_row = 3

        self.suggested_logo = ImageTk.PhotoImage(Image.open(self.im_path+"suggested.png").resize((300,80)))
        self.suggested_label = tk.Label(self.suggested_grid,image=self.suggested_logo,bg="#FDF1F5")
        self.suggested_label.grid(row=0,column=0)

        self.all_logo = ImageTk.PhotoImage(Image.open(self.im_path+"all.png").resize((100,80)))
        self.all_label = tk.Label(self.tools_grid,image=self.all_logo,bg="#FDF1F5")
        self.all_label.grid(row=0,column=0)

    def mainloop(self):
        self.window.mainloop()

    def inc_grid_arrange(self):
        if self.curr_grid[1] == self.max_in_row - 1:
            self.curr_grid[0] = self.curr_grid[0] + 1
            self.curr_grid[1] = 0
        else:
            self.curr_grid[1] = self.curr_grid[1] + 1

    def inc_suggested_grid_arrange(self):
        if self.curr_suggested_grid[1] == self.max_in_row - 1:
            self.curr_suggested_grid[0] = self.curr_suggested_grid[0] + 1
            self.curr_suggested_grid[1] = 0
        else:
            self.curr_suggested_grid[1] = self.curr_suggested_grid[1] + 1

    def add_suggested_tool(self, tool_name, image, tool_file):
        def launch():
            print('hey add_suggested_tool button')

        im = Image.open(self.im_path + image).resize((372,242))
        self.suggested_imgs_dict[str(self.curr_suggested_grid)] = ImageTk.PhotoImage(im)
        button = tk.Button(self.suggested_grid,
                           text=tool_name,
                           image=self.suggested_imgs_dict[str(self.curr_suggested_grid)],
                           command=launch,
                           font=("Arial", 14),
                           pady=10,
                           compound=tk.BOTTOM,
                           bg="#FFFFFF")
        button.grid(row=self.curr_suggested_grid[0], column=self.curr_suggested_grid[1])
        self.inc_suggested_grid_arrange()

        self.window.update_idletasks()

    def add_tool(self, tool_name, image, tool_file):
        def launch():
            print('hey add_tool button')

        im = Image.open(self.im_path + image).resize((372,242))
        self.imgs_dict[str(self.curr_grid)] = ImageTk.PhotoImage(im)
        button = tk.Button(self.tools_grid,
                           text=tool_name,
                           image=self.imgs_dict[str(self.curr_grid)],
                           command=launch,
                           font=("Arial", 14),
                           pady=10,
                           compound=tk.BOTTOM,
                           bg="#FFFFFF")
        button.grid(row=self.curr_grid[0], column=self.curr_grid[1])
        self.inc_grid_arrange()

        self.window.update_idletasks()


if __name__ == "__main__":
    dashboard = ToolChangeDashboard()

    dashboard.add_suggested_tool(tool_name='Standard Gripper',
                       image='standard_gripper.png',
                       tool_file='')

    dashboard.add_suggested_tool(tool_name='Standard Gripper w/Teleop Kit',
                       image='stretch_teleop_kit/images/teleop_kit_full.jpg',
                       tool_file='')

    dashboard.add_tool(tool_name='Standard Dex Wrist',
                       image='stretch_dex_wrist/images/dex_wrist_A.png',
                       tool_file='')

    dashboard.add_tool(tool_name='Standard Dex Wrist w/Teleop Kit',
                       image='stretch_teleop_kit/images/teleop_kit_full.jpg',
                       tool_file='')

    dashboard.add_tool(tool_name='Inspection Cam',
                       image='wrist_USB_board_camera/images/wrist_camera_A.png',
                       tool_file='')

    dashboard.add_tool(tool_name='Dry Erase Marker',
                       image='dry_erase_holder_V1/images/dry_erase_A.PNG',
                       tool_file='')

    dashboard.add_tool(tool_name='Swiffer Tool',
                       image='swiffer_mount_V1/images/swiffer_A.PNG',
                       tool_file='')

    dashboard.add_tool(tool_name='Tray Cup Holder',
                       image='tray_cup_holder_V1/images/tray_cup_holder_C.PNG',
                       tool_file='')

    dashboard.mainloop()
