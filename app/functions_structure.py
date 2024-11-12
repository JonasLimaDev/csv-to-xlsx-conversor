from flet import (
    alignment,
    colors,
    Container,
    Text,
    TextAlign,
    TextDecoration,
    TextField,
    TextOverflow,
    TextStyle,
    TextSpan,
)

def add_text_to_container(text_component):
    """
    Retorna uma instancia do comopnete Container,
    com as configurações estabeleciadas para o grupo de texto
    """
    return  Container(
        content=text_component,
        alignment=alignment.center,
        padding=5)

def add_input_to_container(input_component):
    return Container(
        content=input_component,
        alignment=alignment.center,
        margin=10,
        padding=10,
        border_radius=10)


def create_input_configuration(input_label, input_helper="", input_value=""):
    return TextField(
        label = input_label,
        value = input_value,
        helper_text = input_helper,
        multiline = True,
        min_lines = 1,
        max_lines = 4,
        label_style = TextStyle(size=20),
        helper_style = TextStyle(size=12, overflow=TextOverflow.VISIBLE),
    )


def create_header(text):
    return Container(
        content=Text(
            text,
            text_align=TextAlign.CENTER,
            size=18),
        alignment=alignment.center,
        margin=10,
        padding=15,
    )

def create_span_with_url(text,url):
    return TextSpan(
        text,
        TextStyle(
            decoration_color=colors.BLUE,
            color=colors.BLUE
        ),
        url=url)