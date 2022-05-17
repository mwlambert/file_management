# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:51:21 2022

@author: m.lambert
"""
import tkinter as tk
from tkinter import filedialog

def browse_for_file():
    """
    Use tkinter to browse for a file

    Returns
    -------
    fpath : str
        Filepath string

    """
    root = tk.Tk()
    root.title('Choose a file')
    root.withdraw() # use to hide tkinter window
    root.attributes("-topmost", True)
    root.after_idle(root.attributes,'-topmost',False)
    
    fpath = filedialog.askopenfilename()
    
    return fpath

def browse_for_files():
    """
    Use tkinter to browse for a file

    Returns
    -------
    fpaths : tuple
        Tuple of filepath strings

    """
    root = tk.Tk()
    root.title('Choose a file')
    root.withdraw() # use to hide tkinter window
    root.attributes("-topmost", True)
    root.after_idle(root.attributes,'-topmost',False)
    
    fpaths = filedialog.askopenfilenames()
    
    return fpaths