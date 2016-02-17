import Ostap_my_beautiful_soup
import e_tmembers_GUI
import glob
from tkinter import *


def start_extraction():
        path = e_tmembers_GUI.e_sF.get() + "*.html"
        list_of_files = glob.glob(path)
        
        for item in list_of_files:
              Ostap_my_beautiful_soup.extract_members(item)
        


    
    
