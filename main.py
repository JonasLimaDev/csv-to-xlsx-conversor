import flet as ft

from window.functions_structure import (
    add_text_to_container,
    add_input_to_container,
    create_input_configuration,
    create_header,
    create_span_with_url,
)

from conversor.classes_configuration_file import (
    FileDataConfig,)


from conversor.class_data_csv import DataClassCSV


from conversor.class_data_xlsx import DataClassXlsx


from conversor.functions_configuration_file import (
    create_inital_config,
    create_inputs_config
    )


BASE_INPUTS = {
    "save_new_file":[
        "Salvar Novo Arquivo", # label do imput
        "Decidir onde Salvar o Arquivo Processado. \
        Por padrão é salva com o nome do arquivo de origem, assim,\
        novas conversões sempre irão sobreescrever o arquivo de resultado", # helper do imput
        False, # tipo de dado da configuração
        ],
    "encoding_file":[
        "Codificação", # label do imput
        "Tipo de codificação Usada no Arquivo \
        que deseja converter", # helper do imput
        "str", # tipo de dado da configuração
        ],
    "delimiter_file":[
        "Delimitador",
        "Delimitador das colunas do arquivo. padrão ','",
        "str",
    ],
    "rows_contains_partial":[
        "Excluir Linhas Por Conteúdo Parcial",
        "Remove linhas caso em qualquer das celulas que tenham os termos definidos",
        ['list',],
    ],
    "rows_contains_terms":[
        "Excluir Linhas Por Conteúdo",
        "Remove linhas caso em qualquer das celulas que tenha exatamente o(s) termo(s) definido(s)",
        ['list',],
    ],
    "rows_excepty_first":[
        "Excluir Linhas, Exceto Primeiro Caso",
        "Remove linhas caso em qualquer das celulas tenha exatamente o(s)\
        termo(s) definido(s),\n porém mantém o primeiro caso localizado.\
        ideal caso possua cabeçalhos que se repetem",
        ['list',],
    ],
    "rows_empety":[
        "Excluir Linhas Vazias",
        "Remove linhas caso todas as celulas estejam vazias",
        True,
    ],
    "columns_number":[
        "Excluir Colunas",
        "Remove as Colunas, comforme número da posição definido",
        ['list',],
    ],
}    


def main(page: ft.Page):
    # configurações iniciais da janela
    page.title = "CONVERSOR: csv => xlsx"
    page.window.width = 620       
    page.window.height = 680
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    configuracoes = FileDataConfig()
    arquivo_resultado = None

    #adições
    def load_configuration(e):
        configuracoes.update_config()

    def generic_alert(title, mensagem,cor=1):
        cores = {
            1: ft.colors.GREEN_500,
            2: ft.colors.LIGHT_BLUE_ACCENT_200,
            3: ft.colors.RED_400,
        }
        page.open(ft.AlertDialog(
            title=ft.Text(f"{title}"),
            content=ft.Text(f"{mensagem}"),
            bgcolor = cores[cor]
        ))
     

    def converter_arquivo(e):
        botao_converter.disabled=True
        page.update()
        
        dados_arquivo = botao_converter.data['entrada']
        for info_arquivo in dados_arquivo:
            nome_arquivo = info_arquivo.name.split(".")[0]
            filters = configuracoes.get_filters()
            dados_instance = DataClassCSV(filters=filters,path_file=info_arquivo.path)
            dados_instance.load_csv_file(configuracoes.confi_to_read())
            if dados_instance.erros:
                if str(dados_instance.erros) == "'utf-8' codec can't decode\
                    byte 0xe1 in position 27: invalid continuation byte":
                    generic_alert(
                        "Erro Ao Processar Arquivo",
                        f"Erro de Codificação do arquivo.\
                        \n{dados_instance.erros}\n \
                        experimente trocar a codificação nas configurações",
                        3)
                else:

                    generic_alert(
                        "Erro Ao Processar Arquivo",
                        f"Erro não mapeado\n{dados_instance.erros}",
                        3)
                return
            dados_instance.filters_aplier()

            xlsx_file = DataClassXlsx(dados_instance.data)
            xlsx_file.create_xlsx_file()
            if configuracoes.all['configuration']['result']['save_new_file']:
                seletor_arquivo_salvar.save_file(dialog_title="Salvar Arquivo Processado",allowed_extensions=["xlsx"])
                while True:
                    if  botao_converter.data['saida']:
                        xlsx_file.save_file_xlsx(botao_converter.data['saida'])
                        generic_alert("Processamento Finalizado Com Sucesso","")
                        botao_converter.data['saida']=''
                        break
                page.update()
            else:
                xlsx_file.save_file_xlsx(f"{info_arquivo.path.replace(info_arquivo.name,'')}{nome_arquivo}")
                generic_alert("Processamento Finalizado Com Sucesso","")
        
        
    def selecao_arquivo(e: ft.FilePickerResultEvent):
        botao_converter.data["entrada"] = list(e.files)
        botao_converter.disabled=False
        page.update()
      

    def salvar_arquivo_resultado(e: ft.FilePickerResultEvent):
        if e.path:
            botao_converter.data["saida"]= e.path
        else:
            generic_alert("Erro ao Salvar Arquivo","Nenhum arquivo de destino foi definido",3)
            page.update()
    
    def salvar_arquivo_config(e):
        configuracoes.save_by_input_list(lista_inputs_config, instacias_configs)
        configuracoes.update_config()
        generic_alert("Arquivo Salvo com Sucesso","")
        page.update()

    def abri_link(e):
        page.launch_url('https://github.com/JonasLimaDev/csv-to-xlsx-conversor')


    text_cabecalho = create_header("Conversor de Arquivo CSV para XLSX")

    text_label_converter = ft.Text(
        "Secelcione um Arquivo para iniciar a Conversão",
        text_align=ft.TextAlign.CENTER,
        size=14)

    botao_converter = ft.ElevatedButton("Converter", on_click=converter_arquivo, disabled=True, data={'entrada':'','saida':''})
    # botão para carregar o arquivo que será convertido

    botao_select_file = ft.ElevatedButton("Selecionar Arquivo...",
        on_click=lambda _: seletor_arquivo_abrir.pick_files(
        allow_multiple=True, allowed_extensions=["csv"])
    )

    # instruções para diálogo de salvar arquivo
 
    seletor_arquivo_abrir = ft.FilePicker(on_result=selecao_arquivo)
    
    seletor_arquivo_salvar = ft.FilePicker(on_result=salvar_arquivo_resultado,)


    grupo_texto_coluna = [
        text_cabecalho,
        add_text_to_container(text_label_converter),
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

    instacias_configs = create_inputs_config(
        configuracoes.get_individual_config(),BASE_INPUTS
    )
    lista_inputs_config = []
    for instancia in instacias_configs:
        lista_inputs_config.append(
                create_input_configuration(
                    instancia.label,
                    instancia.helper,
                    instancia.value_display)
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
                    [create_header("Configurações Para Tratamento do Arquivo")]+
                    [add_input_to_container(item) for item in lista_inputs_config ]+[ft.ElevatedButton("Salvar",on_click=salvar_arquivo_config)],
                    scroll="auto",
                    )
                ),
            ),
            ft.Tab(
                text="Sobre",
                icon=ft.icons.INFO_OUTLINE_ROUNDED,
                
                content=ft.Container(
                ft.Column(
                    [create_header("Informações do Programa"),
                    add_text_to_container(ft.Text("Versão: 1.0.0")),
                    add_text_to_container(
                        ft.Text(
                            "Desenvolvido por: ",
                            spans=[
                                create_span_with_url("Jonas Lima","https://github.com/JonasLimaDev/")
                                ]
                            ),
                        ),
                    add_text_to_container(
                        ft.Text(
                            "Código Fonte: ",
                            spans=[
                                create_span_with_url(
                                    "Repositório",
                                    "https://github.com/JonasLimaDev/csv-to-xlsx-conversor")
                                ]
                        ),
                    )],
                    scroll="auto",
                    )
                ),
            ),
        ],
        expand=1,)


    page.add(seletor_arquivo_abrir)
    page.add(seletor_arquivo_salvar)
    page.add(t)


    # page.add(criar_container_input(tb1))


if __name__ == "__main__":
    create_inital_config()
    ft.app(main)