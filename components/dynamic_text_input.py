import streamlit as st

# criar um input dinâmico com o Streamlit que limpa o valor do input quando o usuário pressiona Enter


def dynamic_text_input(
        label,
        value="",
        max_chars=None,
        key=None,
        type="default",
        help=None,
        autocomplete=None,
        on_change=None,
        args=None,
        kwargs=None,
        placeholder=None,
        disabled=False,
        label_visibility="visible"
):
    """
    Função para criar um input dinâmico com o Streamlit.

    Args:
        label (str): O rótulo do input.
        value (str, optional): Valor inicial do input. Padrão é "".
        max_chars (int, optional): Número máximo de caracteres permitidos.
        key (str/int, optional): Chave única para o widget.
        type (str, optional): Tipo do input, pode ser "default" ou "password". Padrão é "default".
        help (str, optional): Tooltip opcional exibido ao lado do input.
        autocomplete (str, optional): Valor para o atributo 'autocomplete' do input.
        on_change (callable, optional): Callback invocado quando o valor do input muda.
        args (tuple, optional): Argumentos para passar para o callback.
        kwargs (dict, optional): Argumentos nomeados para passar para o callback.
        placeholder (str, optional): String exibida quando o input está vazio.
        disabled (bool, optional): Se True, o input é desativado. Padrão é False.
        label_visibility (str, optional): Visibilidade do rótulo. Pode ser "visible", "hidden" ou "collapsed". Padrão é "visible".

    Returns:
        str: O valor atual do input.
    """
    return st.text_input(
        label=label,
        value=value,
        max_chars=max_chars,
        key=key,
        type=type,
        help=help,
        autocomplete=autocomplete,
        on_change=on_change,
        args=args if args else (),
        kwargs=kwargs if kwargs else {},
        placeholder=placeholder,
        disabled=disabled,
        label_visibility=label_visibility
    )





# def dynamic_text_input(
#         label,
#         value="",
#         max_chars=None,
#         key=None,
#         type="default",
#         help=None,
#         autocomplete=None,
#         on_change=None,
#         args=None,
#         kwargs=None,
#         placeholder=None,
#         disabled=False,
#         label_visibility="visible"
# ):
#     """
#     Função para criar um input dinâmico com o Streamlit.
#
#     Args:
#         label (str): O rótulo do input.
#         value (str, optional): Valor inicial do input. Padrão é "".
#         max_chars (int, optional): Número máximo de caracteres permitidos.
#         key (str/int, optional): Chave única para o widget.
#         type (str, optional): Tipo do input, pode ser "default" ou "password". Padrão é "default".
#         help (str, optional): Tooltip opcional exibido ao lado do input.
#         autocomplete (str, optional): Valor para o atributo 'autocomplete' do input.
#         on_change (callable, optional): Callback invocado quando o valor do input muda.
#         args (tuple, optional): Argumentos para passar para o callback.
#         kwargs (dict, optional): Argumentos nomeados para passar para o callback.
#         placeholder (str, optional): String exibida quando o input está vazio.
#         disabled (bool, optional): Se True, o input é desativado. Padrão é False.
#         label_visibility (str, optional): Visibilidade do rótulo. Pode ser "visible", "hidden" ou "collapsed". Padrão é "visible".
#
#     Returns:
#         str: O valor atual do input.
#     """
#     return st.text_input(
#         label=label,
#         value=value,
#         max_chars=max_chars,
#         key=key,
#         type=type,
#         help=help,
#         autocomplete=autocomplete,
#         on_change=on_change,
#         args=args if args else (),
#         kwargs=kwargs if kwargs else {},
#         placeholder=placeholder,
#         disabled=disabled,
#         label_visibility=label_visibility
#     )
