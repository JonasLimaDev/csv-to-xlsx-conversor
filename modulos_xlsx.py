import string
import xlsxwriter


def decompose_number(number):
    """
    Retorna indicação de duas posições de letras para números maiores que 26,
    conforme calculo de decomposição.
    sendo o primeiro indicador, o número de vezes que a decomposição foi aplicada,
    e o segundo indicador, o resto da decomposição.
    """

    first_indicator = 0
    second_indicator = number
    
    while(second_indicator >= 26):
        second_indicator -= 26
        first_indicator += 1
    
    return first_indicator-1, second_indicator 


def number_to_letter(number):
    """
    Retorna uma letra conforme posição númerica da letra no alfabeto em uma lista.
    caso o número ultrapasse o valor de letras do alfabeto, retorna uma combinação
    de duas letras, sendo, a primeira a posição conforme a quantidade de vezes que o número ultrapassou
    o maximo de letras no alfabeto, e a segunda a posição correponde ao valor
    restante que não ultrapassa o número máximo de letras do alfabeto. 
    
    Exemplos:
        Ex1:
        -- Entrada: 0
        -- Saída A
        Ex2:
        -- Entrada: 27
        -- Saída AB
        Ex3:
        -- Entrada: 56
        -- Saída BE

    O limite máximo é de 701 que irá retornar ZZ
    Depende da função: decompose_number.
    """

    letters = list(string.ascii_uppercase)
    if number >= 26:
        first_index, second_index = decompose_number(number)
        return f"{letters[first_index]}{letters[second_index]}"
    else:
        return f"{letters[number]}"


def get_dict_letters(limit):
    """
    Criar um dicionário com o número correspondente da posição de cada letra do alfabeto
    """

    letters_dict = {}
    for index in range(limit):
        letters_dict[index] = number_to_letter(index)
    return letters_dict



def create_xlsx_file(data_to_save):

    workbook = xlsxwriter.Workbook('temp_file_data.xlsx')
    worksheet = workbook.add_worksheet()
    row_index=0
    for row_data in data_to_save:
        dic_index_colunm = get_dict_letters(len(row_data))
        for cell_data in row_data:
            worksheet.write(f'{dic_index_colunm[row_data.index(cell_data)]}{row_index}', cell_data)
        row_index += 1
    workbook.close()

