# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:51:21 2022

@author: m.lambert
"""

import tkinter as tk
from tkinter import filedialog


def browse_for_file():
    """
    Use tkinter to browse for the file

    Returns
    -------
    fpath : str
        Filepath string

    """
    root = tk.Tk()
    root.withdraw() # use to hide tkinter window
    
    fpath = filedialog.askopenfilename()
    
    return fpath
