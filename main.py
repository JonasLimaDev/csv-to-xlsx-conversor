import flet as ft
from conversor.modulos_csv import (
    get_data_csv_file,
    filters_aplier,
) 

from conversor.modulos_xlsx import create_xlsx_file

from conversor.config_file_data import (
    add_configuration,
    create_inital_config,
    get_individual_config,
    load_config_file,
    wirite_config_file,
    )


BASE_INPUTS = {
    "encoding_file":[
        "Condificação",
        "Tipo de codificação Usada no Arquivo \
        que deseja converter"
        ],
    "delimiter_file":[
        "Delimitador",
        "Delimitador das colunas do arquivo. padrão ','"
    ],
    "rows_contains_partial":[
        "Excluir Linhas Por Conteúdo Parcial",
        "Remove linhas caso em qualquer das celulas que tenham os termos definidos"
    ],
    "rows_contains_terms":[
        "Excluir Linhas Por Conteúdo",
        "Remove linhas caso em qualquer das celulas que tenha exatamente o(s) termo(s) definido(s)"
    ],
    "rows_excepty_first":[
        "Excluir Linhas, Exceto Primeiro Caso",
        "Remove linhas caso em qualquer das celulas tenha exatamente o(s)\
        termo(s) definido(s),\n porém mantém o primeiro caso localizado.\
        ideal caso possua cabeçalhos que se repetem"
    ],
    "rows_empety":[
        "Excluir Linhas Vazias",
        "Remove linhas caso todas as celulas estejam vazias"
    ],
    "columns_number":[
        "Excluir Colunas",
        "Remove as Colunas, comforme número da posição definido"
    ],
}


class ConfigurationInput():
    def __init__(self, label, key_to_write, type_config, value="", helper=""):
        self.label = label
        self.key_to_write = key_to_write
        self.value = value
        self.helper = helper
        self.type_config = type_config
        self.value_display = self.value_to_display_view()

    
    def get_data_to_write(self):
        return {self.key_to_write: value }
    
    def value_to_display_view(self):
        if self.type_config != list:
            text_display = str(self.value)
            remove = ['[',']','"',]
            for item in remove:
                text_display =text_display.replace(item,"")
        else:
            # print(self.value)
            text_display = ""
            for item in self.value:
                removes = ['[',']','"',]
                for remove in removes:
                    item = str(item).replace(remove,"")
                text_display += f"{item}; "
            text_display = text_display[:-2]
        # print(text_display)

        return text_display
    
    def get_dict_to_save(self):
        # print(self.type_config)
        if self.type_config == list:
            return {self.key_to_write: str(self.value).split(";")}
        elif self.type_config == bool:
            return {self.key_to_write: bool(self.value)}
        else:
            return {self.key_to_write: self.value}


def definir_inputs_configuracao(configs):
    inputs_data = []
    for config in configs:
        for key_config in config:
            inputs_data.append(
                ConfigurationInput(
                    label=BASE_INPUTS[key_config][0],
                    key_to_write=key_config,
                    value=config[key_config],
                    helper=BASE_INPUTS[key_config][1].replace("       ",""),
                    type_config = type(config[key_config])
                )
            )
    return inputs_data



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
   
        border_radius=10
    )
    return instancia_container


def criar_input_configuracao(input_label, input_helper="", input_value=""):
    input_data = ft.TextField(
        label=input_label,
        value=input_value,
        multiline=True,
        min_lines=1,
        max_lines=4,
        label_style = ft.TextStyle(size=20),
        helper_text=input_helper,
        helper_style = ft.TextStyle(size=12,overflow=ft.TextOverflow.VISIBLE),
    )
    return input_data



def salvar_dados_config(input_list, config_class_list):
    configuracoes = load_config_file()
    
    for input_item in input_list:
        for config_class in config_class_list:
            print(config_class.value)
            if input_item.label == config_class.label:
                 config_class.value = input_item.value
            # print(config_class.value)
            configuracoes = add_configuration(
                configuracoes,
                config_class.get_dict_to_save()
            )
    wirite_config_file(configuracoes)

def main(page: ft.Page):
    # configurações iniciais da janela
    page.title = "CONVERSOR: csv => xlsx"
    page.window.width = 620       
    page.window.height = 680
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.scroll = "adaptive"
    
    # page.update()
    arquivo_selecionado = []

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
        title=ft.Text("Processamento Finalizado"),
    )

    dlg_erro = ft.AlertDialog(
        title=ft.Text("Erro Processar arquivo"),
    
    )
    def load_configuration(e):
        load_config_file()


    def converter_arquivo(e):
        botao_converter.disabled=True
        page.update()
        dados_arquivo = botao_converter.data
        for info_arquivo in dados_arquivo:
            nome_arquivo = info_arquivo.name.split(".")[0]
            dados = get_data_csv_file(info_arquivo.path)
            if type(dados) != list:
                print("erro meu brother")
                if str(dados) == "'utf-8' codec can't decode byte 0xe1 in position 27: invalid continuation byte":
                    dlg_erro.content = ft.Text(f"Erro de Codificação do arquivo.\n{dados}\n experimente trocar a codificação nas configurações")
                    page.open(dlg_erro)
                else:
                    dlg_erro.content = ft.Text(f"Erro não mapeado\n{e}")
                    page.open(dlg_erro)
                return
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

    instacias_configs = definir_inputs_configuracao(get_individual_config())
    lista_inputs_config = []
    for instancia in instacias_configs:
        lista_inputs_config.append(
                criar_input_configuracao(instancia.label,instancia.helper,instancia.value_display)
                )
    def salvar_arquivo_config(e):
        salvar_dados_config(lista_inputs_config, instacias_configs)
        page.update() 

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
                    [criar_container_input(item) for item in lista_inputs_config ]+[ft.ElevatedButton("Salvar",on_click=salvar_arquivo_config)],
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