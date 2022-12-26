import streamlit as st
class View():
    @classmethod
    def show(text,method = 'default'):
        if not text:
            raise ValueError('Enter some text please.')
        if method == 'default':
            if isinstance(text,str):
                st.markdown(text)
            elif isinstance(text,list):
                st.table(text)
            elif isinstance(text,dict):
                st.json(text)
            else:
                raise ValueError('Ender avaliable text please:str, list or dict.')

        if method == 'select':
            select_text = st.selectbox(
                label = '选择目录',
                options = text
                
            
            )
            return select_text
    
    