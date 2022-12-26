from find import LocalFinder
from view import View
import streamlit as st
def lib():
    
    filenames = LocalFinder.filenames
    viewer = View.show
    st.header('Book Meal',anchor = 'home')
    st.text(filenames)
    filename = viewer(filenames
    ,method = 'select'
    )
    
    contents = LocalFinder.get_file(filename)
    viewer(contents)
    
    
if __name__ == '__main__':
    lib()
# lib()