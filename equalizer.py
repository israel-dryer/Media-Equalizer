"""
    A simple GUI template for a media equalizer built with Tkinter
    Author: Israel Dryer
    Modified: 2020-05-11
"""

import tkinter as tk
from tkinter import ttk
import ttkthemes


# ------- Equalizer Functions ---------

def on_reset():
    """Reset equalizer values to 50 percent"""
    for obj in eq_sliders:
        obj.set(50)
    presets.set('Normal')
    reset.focus_set()

def on_selection():
    """Set equalizer to preset values based on combo selection"""
    defaults = options[presets.get()]
    for i, val in enumerate(defaults):
        eq_sliders[i].set(val)

def on_save():
    """Save current values to custom preset"""
    options['Custom'] = [val.get() for val in eq_sliders]
    presets.set('Custom')


# ------- Equalizer Window ---------

root = tk.Tk()
root.withdraw()  # hide the window until completely built
root.title('The Great Equalizer')
root.iconbitmap('eqicon.ico')
root.resizable(False, False)

# apply theme
style = ttkthemes.ThemedStyle()
style.theme_use('breeze')
style.configure('title.TLabel', font=('Broadway', 18))

# window frames to contain sliders & buttons
bframe = ttk.Frame(root)
sframe = ttk.Frame(root)
lframe = ttk.Frame(root)

# sliders
eq_names = ['Vol', '63', '125', '250', '500', '1k', '2k', '4k', '8k', '16k']
eq_sliders = [ttk.Scale(sframe, from_=0, to=100, value=50, length=200, orient=tk.VERTICAL) for name in eq_names]
eq_labels = [ttk.Label(lframe, text=name) for name in eq_names]

# default presets [volume, band...]
options = {
    'Normal': [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
    'Pop': [50, 50, 50, 50, 60, 65, 40, 30, 30, 30], 
    'Classic': [50, 50, 50, 20, 50, 55, 50, 80, 80, 80], 
    'Jazz': [50, 50, 50, 75, 25, 40, 60, 45, 45, 45],
    'Rock': [50, 50, 50, 65, 5, 40, 65, 65, 65, 65],
    'Custom': [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
    }

# buttons
presets = ttk.Combobox(bframe, values=list(options.keys()))
presets.bind("<<ComboboxSelected>>", lambda x: on_selection())
presets.set('Normal')
reset = ttk.Button(bframe, text='Reset', command=on_reset)
save = ttk.Button(bframe, text='Save', command=on_save)

# arrange objects in root window
bframe.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
presets.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=tk.YES)
reset.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=tk.YES)
save.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=tk.YES)
sframe.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
lframe.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
for slider in eq_sliders:
    slider.pack(side=tk.LEFT, fill=tk.Y, padx=10, expand=tk.YES)
for label in eq_labels:
    label.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=(0, 15), expand=tk.YES)

# show window and start main loop
root.eval('tk::PlaceWindow . center') 
root.deiconify()  # show screen after all changes have been made
root.mainloop()