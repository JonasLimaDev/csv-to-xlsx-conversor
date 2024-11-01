import flet as ft
from conversor.modulos_csv import (
    get_data_csv_file,
    filters_aplier,

) 
from conversor.modulos_xlsx import create_xlsx_file
from conversor.config_file_data import (
    load_config_file,
    create_inital_config
    )
# from conversor.execute_filters import execultar_filtros



class ConfigurationInput():
    def __init__(self, label, key_to_write, value="",helper=""):
        self.label = label
        self.key_to_write = key_to_write
        self.value = value
        self.helper = helper
    
    def get_data_to_write(self):
        return {self.key_to_write: value }
    


def define_inputs_configuracao(configs):
    {
        "encoding_file":[
            "Condificação",
            "Tipo de codificação Usada no Arquivo \
                que deseja converter"
                ],
        "delimiter_file":[
            "Delimitador",
            "Delimitador das colunas do arquivo. padrão ','"
        ],
        "rows_contains_partial":[],
        "rows_contains_terms":[],
        "rows_excepty_first":[],
        "rows_empety":[],
        "columns_number":[],
    }


def criar_container_texto(componente_texto):
    """
    Retorna uma instancia do comopnete Container,
    com as configurações estabeleciadas para o grupo de texto
    """
    instancia_container = ft.Container(
        content=componente_texto,
        alignment=ft.alignment.center,
        padding=5
        )
    return instancia_container
    

def criar_container_input(componente_input):
    instancia_container = ft.Container(
        content=componente_input,
        alignment=ft.alignment.center,
        margin=10,
        padding=10,
        width=450,
        height=200,
        border_radius=10
    )
    return instancia_container


def create_input_data_config(input_label, input_helper="", input_value=""):
    input_data = ft.TextField(
        label=input_label,
        value=input_value,
        multiline=True,
        min_lines=2,
        max_lines=3,
        label_style = ft.TextStyle(size=22),
        helper_text=input_helper,
        helper_style = ft.TextStyle(size=14),
    )
    return input_data



def pegar_dados_input_list(input_list):
    for input_item in input_list:
        print(input.value)


def main(page: ft.Page):
    # configurações iniciais da janela
    page.title = "CONVERSOR: csv => xlsx"
    page.window.width = 600       
    page.window.height = 640
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.scroll = "adaptive"
    
    # page.update()
    arquivo_selecionado = []
    configs = load_config_file()

    text_cabecalho = ft.Text("Conversor de Arquivo CSV para XLSX",text_align=ft.TextAlign.CENTER,size=18)
    text_label_converter = ft.Text("Secelcione um Arquivo para iniciar a Conversão",text_align=ft.TextAlign.CENTER,size=14)
    # botão para carregar o arquivo que será convertido
    botao_select_file = ft.ElevatedButton("Selecionar Arquivo...",
        on_click=lambda _: file_picker.pick_files(
        allow_multiple=True, allowed_extensions=["csv"])
    )
    
    # instruções para diálogo de salvar arquivo
    def save_file_result(e: ft.FilePickerResultEvent):
        print(e.path)
    save_file_dialog = ft.FilePicker(on_result=save_file_result)
    page.add(save_file_dialog)


    def on_dialog_result(e: ft.FilePickerResultEvent):
        botao_converter.data = list(e.files)
        botao_converter.disabled=False
        page.update()
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.add(file_picker)

    dlg = ft.AlertDialog(
        title=ft.Text("Converssão Finalizada"),
    )

    def load_configuration(e):
        print("acionado")
        print(t.selected_index)

    def converter_arquivo(e):
        botao_converter.disabled=True
        page.update()
        dados_arquivo = botao_converter.data
        for info_arquivo in dados_arquivo:
            nome_arquivo = info_arquivo.name.split(".")[0]
            dados = get_data_csv_file(info_arquivo.path)
            dados = filters_aplier(dados)

            create_xlsx_file(dados,
            f"{info_arquivo.path.replace(info_arquivo.name,'')}{nome_arquivo}")
        # save_file_dialog.save_file()
        page.open(dlg)
        
    botao_converter = ft.ElevatedButton("Converter", on_click=converter_arquivo, disabled=True)

    grupo_texto_coluna = [
        criar_container_texto(text_cabecalho),
        criar_container_texto(ft.Text()),
        criar_container_texto(text_label_converter),
    ]

    layout_conversor = ft.Column(
        [ft.Column(grupo_texto_coluna),
        ft.Container(content=botao_select_file,
            alignment=ft.alignment.center
        ),
        ft.Container(margin=10,padding=5),
        ft.Container(
            content=botao_converter,
            alignment=ft.alignment.center
        ),]
    )

    lista_inputs_config = []
    for i in range(5):
        lista_inputs_config.append(
            criar_container_input(
                create_input_data_config(f"input {i}",input_value=i)
                )
        )

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        on_change=load_configuration,
        
        tabs=[
            ft.Tab(
                text="Conversor",
                icon=ft.icons.FILE_COPY,
                content=ft.Container(
                    layout_conversor
                ),
            ),
            ft.Tab(
                text="Configurações",
                icon=ft.icons.SETTINGS,
                
                content=ft.Container(
                ft.Column(
                    lista_inputs_config+[ft.ElevatedButton("Salvar",  disabled=True)],
                    scroll="auto",
                    )
                ),
            ),
        ],
        expand=1,
    )
    page.add(t)


    # page.add(criar_container_input(tb1))


if __name__ == "__main__":
    create_inital_config()
    ft.app(main)