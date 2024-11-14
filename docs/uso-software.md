# Informações de Uso

## Configurações para leitura do Arquivo de origem

### Codificação

Tipo de codificação Usada no Arquivo de origem o qual deseja converter.

### Delimitador

Delimitador das colunas do arquivo. O padrão ',', mas pode variar para ';' e '|' por exemplo.

## Configurações para Limpeza de Dados


### Excluir Linhas Por Conteúdo

Remove linhas conforme termos buscados, deve ser exatamente como está na célula da linha que se deseja remover. Irá verificar o valor da célula como um todo, não importando a posição da célula na linha.


**Exemplo:**
Usando o termo Maçã

*Valores Originais:*

| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 01  | Maçã            | R$ 3,99  | Frutas     | Maçã Fuji, grande, unidade |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Frutas     | Banana nanica, kg |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| 07  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |
| 08  | Maçã            | R$ 2,99  | Frutas     | Maçã Gala, pequena, pacote com 3 unidades|
| 09  | Banana          | R$ 3,50  | Frutas     | Banana prata, kg, firme e ideal para assar |

*Resultado:*

| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Frutas     | Banana nanica, kg |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| 07  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |
| 09  | Banana          | R$ 3,50  | Frutas     | Banana prata, kg, firme e ideal para assar |



### Excluir Linhas Por Conteúdo Parcial

Remove  linhas conforme termos buscados, pode ser uma palavra completa ou fragmento. Irá verificar o valor contido em cada célula da planilha. Deve ser usado com cuidado pois pode acabar excluindo valores que não deveria

**Exemplo:**
Usando o termo Frut

*Valores Originais:*

| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 01  | Maçã            | R$ 3,99  | Frutas     | Maçã Fuji, grande, unidade |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Frutas     | Banana nanica, kg |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| 07  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |
| 08  | Maçã            | R$ 2,99  | Frutas     | Maçã Gala, pequena, pacote com 3 unidades|
| 09  | Banana          | R$ 3,50  | Frutas     | Banana prata, kg, firme e ideal para assar |

*Resultado:*


| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| 07  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |



### Excluir Linhas, Exceto Primeiro Caso

Remove linhas conforme termos buscados, mantendo a primeira linha encontrada. O valor buscado deve ser exatamente como está na célula da linha que se deseja remover. Irá verificar o valor da célula como um todo, não importando a posição da célula na linha.


**Exemplo:**
Usando o termo: 'Nome do Produto'

*Valores Originais:*

| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 01  | Maçã            | R$ 3,99  | Frutas     | Maçã Fuji, grande, unidade |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Frutas     | Banana nanica, kg |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| 10  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |
| 11  | Maçã            | R$ 2,99  | Frutas     | Maçã Gala, pequena, pacote com 3 unidades|
| 12  | Banana          | R$ 3,50  | Frutas     | Banana prata, kg, firme e ideal para assar |


*Resultado:*


| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 01  | Maçã            | R$ 3,99  | Frutas     | Maçã Fuji, grande, unidade |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Frutas     | Banana nanica, kg |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| 10  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |
| 11  | Maçã            | R$ 2,99  | Frutas     | Maçã Gala, pequena, pacote com 3 unidades|
| 12  | Banana          | R$ 3,50  | Frutas     | Banana prata, kg, firme e ideal para assar |

### Excluir Linhas Vazias

Remove linhas vazias que estejam no meio dos dados da Planilha, todas as células da linha devem estar vazias.

**Exemplo:**

*Valores Originais:*

| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 01  | Maçã            | R$ 3,99  | Frutas     | Maçã Fuji, grande, unidade |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
|   |     |    |       |   |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Frutas     | Banana nanica, kg |
|   |     |    |       |   |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| 07  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |
|   |     |    |       |   |
| 08  | Maçã            | R$ 2,99  | Frutas     | Maçã Gala, pequena, pacote com 3 unidades|
| 09  | Banana          | R$ 3,50  | Frutas     | Banana prata, kg, firme e ideal para assar |


*Resultado*

| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 01  | Maçã            | R$ 3,99  | Frutas     | Maçã Fuji, grande, unidade |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Frutas     | Banana nanica, kg |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| 07  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |
| 08  | Maçã            | R$ 2,99  | Frutas     | Maçã Gala, pequena, pacote com 3 unidades|
| 09  | Banana          | R$ 3,50  | Frutas     | Banana prata, kg, firme e ideal para assar |

### Excluir Colunas

Remove colunas conforme indicação do número da posição da coluna, podem ser fornecidos vários valores.


**Exemplo:**
Usando o número 4 para remover a quarta coluna

*Valores Originais:*

| ID  | Nome do Produto | Preço    | Tipo       | Descrição |
| --- | --------------- | -------- | ---------  | --------- |
| 01  | Maçã            | R$ 3,99  | Frutas     | Maçã Fuji, grande, unidade |
| 02  | Leite Integral  | R$ 4,50  | Laticínios | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Grãos      | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Limpeza    | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Frutas     | Banana nanica, kg |
| 06  | Iogurte Natural | R$ 3,20  | Laticínios | Iogurte natural, 150g |
| 07  | Pão Francês     | R$ 4,00  | Padaria    | Pão francês, unidade |
| 08  | Maçã            | R$ 2,99  | Frutas     | Maçã Gala, pequena, pacote com 3 unidades|
| 09  | Banana          | R$ 3,50  | Frutas     | Banana prata, kg, firme e ideal para assar |

*Resultado*

| ID  | Nome do Produto | Preço    | Descrição |
| --- | --------------- | -------- | --------- |
| 01  | Maçã            | R$ 3,99  | Maçã Fuji, grande, unidade |
| 02  | Leite Integral  | R$ 4,50  | Leite integral, 1 litro |
| 03  | Arroz Branco    | R$ 5,20  | Arroz branco, 5kg |
| 04  | Sabão em Pó     | R$ 12,90 | Sabão em pó, 1kg |
| 05  | Banana Nanica   | R$ 2,99  | Banana nanica, kg |
| 06  | Iogurte Natural | R$ 3,20  | Iogurte natural, 150g |
| 07  | Pão Francês     | R$ 4,00  | Pão francês, unidade |
| 08  | Maçã            | R$ 2,99  | Maçã Gala, pequena, pacote com 3 unidades|
| 09  | Banana          | R$ 3,50  | Banana prata, kg, firme e ideal para assar |

## Configurações de Saída

### Salvar Novo Arquivo

Decidir onde Salvar o Arquivo Processado. Por padrão será salvo com o nome do arquivo de origem.
Ao habilitar essa opção será fornecida uma opção para nomear o arquivo de saída.
Arquivos com mesmo nome serão sobrescritos a cada novo processamento.