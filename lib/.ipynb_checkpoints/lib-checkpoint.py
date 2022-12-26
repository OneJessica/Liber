from .find import LocalFinder
from .view import View
import streamlit as st
def lib():
    
    filenames = LocalFinder.filenames
    viewer = View.show
    st.head('Book Meal')
    filename = viewer(filenames,method = 'select')
    
    contents = LocalFinder.get_file(filename)
    
    
if __name__ == '__main__':
    lib()
lib()