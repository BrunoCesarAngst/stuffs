import streamlit as st
from components.dynamic_text_input import dynamic_text_input

st.set_page_config(page_title="Criar um Stuff", page_icon="🗯️")
st.sidebar.header("Criar um Stuff")
st.title("Criar um Stuff")
st.write(
    """This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters."""
)

# criar um form para criar um stuff com nome e descrição

with st.form(key='form_stuff_initial'):
    st.write('Criar um stuff')
    nome = dynamic_text_input('', 'Nome do stuff')
    name_stuff = st.text_input(placeholder='Nome', label_visibility='collapsed')
    description_stuff = st.text_input(placeholder='Descrição', label_visibility='collapsed')
    st.write('uma stuff tem: ', {name_stuff}, {description_stuff})
    submit_button = st.form_submit_button(label='Criar uma stuff')

# popula o dicionário stuff


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)
