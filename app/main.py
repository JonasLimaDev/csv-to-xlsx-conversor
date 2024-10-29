import flet as ft
from conversor.modulos_csv import get_data_csv_file 
from conversor.modulos_xlsx import create_xlsx_file

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

def main(page: ft.Page):
    # configurações iniciais da janela
    page.title = "CONVERSOR: csv => xlsx"
    page.window.width = 600       
    page.window.height = 640
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.update()
    arquivo_selecionado = []

    text_cabecalho = ft.Text("Conversor de Arquivo CSV para XLSX",text_align=ft.TextAlign.CENTER,size=18)
    text_label_converter = ft.Text("Secelcione um Arquivo para iniciar a Conversão",text_align=ft.TextAlign.CENTER,size=14)
    # botão para carregar o arquivo que será convertido
    botao_select_file = ft.ElevatedButton("Selecionar Arquivo...",
        on_click=lambda _: file_picker.pick_files(
        allow_multiple=True, allowed_extensions=["csv"])
    )
    
    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files[0].name)
        botao_converter.data = list(e.files)
        page.update()
        print("Selected file or directory:", e.path)
    file_picker = ft.FilePicker(on_result=on_dialog_result)


    def converter_arquivo(e):
        print(botao_converter.data)
        dados_arquivo = botao_converter.data
        for info_arquivo in dados_arquivo:
            nome_arquivo = info_arquivo.name.split(".")[0]
            
            create_xlsx_file(
                get_data_csv_file(info_arquivo.path,
                encode_file='latin-1'
                ),
                f"{info_arquivo.path.replace(info_arquivo.name,"")}{nome_arquivo}"
                )
    botao_converter = ft.ElevatedButton("Converter",on_click=converter_arquivo)

        
    grupo_texto_coluna = [
        criar_container_texto(text_cabecalho),
        criar_container_texto(ft.Text()),
        criar_container_texto(text_label_converter),
        
    ]

    
    page.add(file_picker)
   
    page.add(
        ft.Column(grupo_texto_coluna))
    page.add(botao_select_file)
    page.add(ft.Container(
        margin=10,
        padding=5,
        
        ))     
    page.add(botao_converter)
    # print(arquivo_selecionado)
    
    # text_numero_sorteado = ft.Text(f"O número Sorteado é: {numero_sorteado}",size=14)
    # label_selecionar_csv = ft.Text(f"O número Sorteado é: {numero_sorteado}",size=14)



if __name__ == "__main__":
    ft.app(main)