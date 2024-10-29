from modulos_csv import get_data_csv_file
from modulos_xlsx import create_xlsx_file
import gi
import shutil

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Conversor de CSV para XLSX")

        self.set_border_width(40) # margem dos objetos
        try:
            self.set_icon_from_file("./logo-img-in-docx.ico")
        except:
            pass

        self.set_default_size(250, 100) # tamnaho da janela
        self.set_resizable(True) # desabilita o redimensionamento da janela

        self.files_list = None


        button_click = Gtk.Button.new_with_label("Gerar Arquivo")
        button_click.connect("clicked", self.on_click_me_clicked)


        title = Gtk.Label(label="Converter de CSV para XLSX")
        label = Gtk.Label(label="")
        span = Gtk.Label(label="")
        span2 = Gtk.Label(label="")
        span3 = Gtk.Label(label="")
        buttonFile = Gtk.Button(label="Escolha os Arquivos")
        buttonFile.set_label("Selecionar Arquivo CSV")
        buttonFile.connect("clicked", self.on_file_clicked)

        buttonFileSave = Gtk.Button(label="Salve o Arquivo")
        buttonFileSave.set_label("Salvar Arquivo Convertido")
        buttonFileSave.connect("clicked", self.on_file_save)

        grid = Gtk.Grid()

        grid.add(title)


        grid.attach_next_to(span, title, Gtk.PositionType.BOTTOM, 2, 3)
        grid.attach_next_to(buttonFile, span, Gtk.PositionType.BOTTOM,1, 1)
        grid.attach_next_to(span2, buttonFile,Gtk.PositionType.BOTTOM,1, 1)
        grid.attach_next_to(button_click,span2,Gtk.PositionType.BOTTOM,1, 1)
        grid.attach_next_to(span3,button_click,Gtk.PositionType.BOTTOM,1, 1)
        grid.attach_next_to(buttonFileSave,span3,Gtk.PositionType.BOTTOM,1, 1)

        self.add(grid)


    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Selecione o Arquivo Para Converter", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )
        dialog.set_select_multiple(False)
        dialog.set_default_size(800, 600)
        self.add_filters_csv(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.files_list = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            pass

        dialog.destroy()


    def on_file_save(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Selecione o Arquivo Para Converter", parent=self, action=Gtk.FileChooserAction.SAVE
        )
        
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE,
            Gtk.ResponseType.OK,
        )
        # dialog.set_select_multiple(False)
        dialog.set_default_size(800, 600)
        self.add_filters_xlsx(dialog)
        

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print(dialog.get_filename())
            shutil.copyfile("./temp_file_data.xlsx",f"{dialog.get_filename()}.xlsx")
            # self.files_list = 
        elif response == Gtk.ResponseType.CANCEL:
            pass

        dialog.destroy()



    def add_filters_csv(self, dialog):
        filter_plan_csv = Gtk.FileFilter()
        filter_plan_csv.set_name("Comma Separated Values (CSV)")
        filter_plan_csv.add_mime_type("text/csv")#
        dialog.add_filter(filter_plan_csv)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
        
        
        
    def add_filters_xlsx(self, dialog):
        filter_plan_xlsx = Gtk.FileFilter()
        filter_plan_xlsx.set_name("Microsoft Excel")
        filter_plan_xlsx.add_mime_type("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")#
        dialog.add_filter(filter_plan_xlsx)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)



    def alert_finished_process(self):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="O Processo Finalizado",
        )

        dialog.format_secondary_text(
            "O processo terminou e o arquivo foi convertido com sucesso."
        )
        dialog.run()

        dialog.destroy()


    def alert_fall_process(self,falha):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text="O Processo Não Foi Execultado",
        )

        dialog.format_secondary_text(
            f"O processo NÃO Foi Executado!!\n\nMotivo:\n{falha}"
        )
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()


    def on_click_me_clicked(self, button):
        print('"Click me" button was clicked')
        print(self.files_list)
        if not self.files_list:
            self.alert_fall_process("Nenum arquivo Selecionado")
            return
        create_xlsx_file(get_data_csv_file(self.files_list,"latin-1"))
        self.alert_finished_process()


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()